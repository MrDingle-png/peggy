#!/usr/bin/env python3
"""
Bidirectional sync between local markdown files and Notion Knowledge Hub.

Usage:
    python3 scripts/sync-notion.py              # full sync
    python3 scripts/sync-notion.py --dry-run    # preview without changes
    python3 scripts/sync-notion.py --status     # show sync status only
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
from dotenv import load_dotenv

SCRIPT_DIR = Path(__file__).parent
WORKSPACE = SCRIPT_DIR.parent
MANIFEST_PATH = SCRIPT_DIR / ".sync-manifest.json"
ENV_PATH = SCRIPT_DIR / ".env"

NOTION_API_BASE = "https://api.notion.com/v1"
NOTION_VERSION = "2022-06-28"

SYNC_DIRS = ["Knowledge", "Tasks"]


def load_config():
    load_dotenv(ENV_PATH)
    token = os.getenv("NOTION_API_TOKEN")
    if not token or token == "ntn_your_token_here":
        print("ERROR: Set NOTION_API_TOKEN in scripts/.env")
        print("See scripts/.env.example for instructions.")
        sys.exit(1)
    return token


def notion_headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Notion-Version": NOTION_VERSION,
        "Content-Type": "application/json",
    }


def load_manifest():
    with open(MANIFEST_PATH) as f:
        return json.load(f)


def save_manifest(manifest):
    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")


def file_hash(filepath):
    content = filepath.read_text(encoding="utf-8")
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def file_mtime_utc(filepath):
    ts = filepath.stat().st_mtime
    return datetime.fromtimestamp(ts, tz=timezone.utc)


def format_page_id(raw_id):
    """Convert a 32-char hex ID to Notion's 8-4-4-4-12 UUID format."""
    raw = raw_id.replace("-", "")
    return f"{raw[:8]}-{raw[8:12]}-{raw[12:16]}-{raw[16:20]}-{raw[20:]}"


def title_from_filename(filename):
    """Convert kebab-case filename to a readable title."""
    name = Path(filename).stem
    words = name.replace("-", " ").replace("_", " ").split()
    small_words = {"a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for", "of", "vs", "v1", "v2", "v3"}
    titled = []
    for i, w in enumerate(words):
        if w.lower() in ("prd",):
            titled.append(w.upper())
        elif i == 0 or w.lower() not in small_words:
            titled.append(w.capitalize())
        else:
            titled.append(w.lower())
    return " ".join(titled)


# --- Notion API helpers ---

def notion_get_page(token, page_id):
    url = f"{NOTION_API_BASE}/pages/{format_page_id(page_id)}"
    resp = requests.get(url, headers=notion_headers(token))
    resp.raise_for_status()
    return resp.json()


def notion_get_blocks(token, block_id):
    """Retrieve all child blocks of a page/block, handling pagination."""
    blocks = []
    url = f"{NOTION_API_BASE}/blocks/{format_page_id(block_id)}/children"
    params = {"page_size": 100}
    while True:
        resp = requests.get(url, headers=notion_headers(token), params=params)
        resp.raise_for_status()
        data = resp.json()
        blocks.extend(data.get("results", []))
        if not data.get("has_more"):
            break
        params["start_cursor"] = data["next_cursor"]
    return blocks


def notion_delete_block(token, block_id):
    url = f"{NOTION_API_BASE}/blocks/{format_page_id(block_id)}"
    resp = requests.delete(url, headers=notion_headers(token))
    resp.raise_for_status()


def notion_append_blocks(token, parent_id, blocks):
    """Append blocks to a page, batching in groups of 100."""
    url = f"{NOTION_API_BASE}/blocks/{format_page_id(parent_id)}/children"
    for i in range(0, len(blocks), 100):
        batch = blocks[i:i + 100]
        resp = requests.patch(
            url, headers=notion_headers(token), json={"children": batch}
        )
        resp.raise_for_status()


def notion_create_page(token, parent_id, title, blocks=None):
    url = f"{NOTION_API_BASE}/pages"
    payload = {
        "parent": {"page_id": format_page_id(parent_id)},
        "properties": {
            "title": [{"text": {"content": title}}]
        },
    }
    if blocks:
        payload["children"] = blocks[:100]
    resp = requests.post(url, headers=notion_headers(token), json=payload)
    resp.raise_for_status()
    result = resp.json()
    new_id = result["id"].replace("-", "")
    if blocks and len(blocks) > 100:
        notion_append_blocks(token, new_id, blocks[100:])
    return new_id


def notion_get_child_pages(token, page_id):
    """Get child pages of a parent page."""
    blocks = notion_get_blocks(token, page_id)
    pages = []
    for b in blocks:
        if b["type"] == "child_page":
            pages.append({
                "id": b["id"].replace("-", ""),
                "title": b["child_page"]["title"],
            })
    return pages


# --- Markdown <-> Notion block conversion ---

def markdown_to_blocks(md_text):
    """Convert markdown text to Notion API block objects."""
    blocks = []
    lines = md_text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        if line.startswith("# "):
            blocks.append(heading_block(1, line[2:].strip()))
            i += 1
        elif line.startswith("## "):
            blocks.append(heading_block(2, line[3:].strip()))
            i += 1
        elif line.startswith("### "):
            blocks.append(heading_block(3, line[4:].strip()))
            i += 1
        elif line.startswith("```"):
            lang = line[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            blocks.append(code_block("\n".join(code_lines), lang or "plain text"))
        elif line.startswith("- ") or line.startswith("* "):
            blocks.append(bullet_block(line[2:].strip()))
            i += 1
        elif re.match(r"^\d+\.\s", line):
            text = re.sub(r"^\d+\.\s", "", line).strip()
            blocks.append(numbered_block(text))
            i += 1
        elif line.startswith("> "):
            blocks.append(quote_block(line[2:].strip()))
            i += 1
        elif line.strip() == "---":
            blocks.append(divider_block())
            i += 1
        else:
            blocks.append(paragraph_block(line.strip()))
            i += 1

    return blocks


def rich_text(text):
    """Convert markdown inline formatting to Notion rich_text array."""
    segments = []
    pattern = re.compile(
        r"(\*\*\*(.+?)\*\*\*)"       # bold+italic
        r"|(\*\*(.+?)\*\*)"           # bold
        r"|(\*(.+?)\*)"               # italic
        r"|(`(.+?)`)"                 # inline code
        r"|(\[([^\]]+)\]\(([^)]+)\))" # link
    )
    pos = 0
    for m in pattern.finditer(text):
        if m.start() > pos:
            segments.append({"type": "text", "text": {"content": text[pos:m.start()]}})

        if m.group(2):  # bold+italic
            segments.append({"type": "text", "text": {"content": m.group(2)},
                             "annotations": {"bold": True, "italic": True}})
        elif m.group(4):  # bold
            segments.append({"type": "text", "text": {"content": m.group(4)},
                             "annotations": {"bold": True}})
        elif m.group(6):  # italic
            segments.append({"type": "text", "text": {"content": m.group(6)},
                             "annotations": {"italic": True}})
        elif m.group(8):  # inline code
            segments.append({"type": "text", "text": {"content": m.group(8)},
                             "annotations": {"code": True}})
        elif m.group(10):  # link
            segments.append({"type": "text", "text": {"content": m.group(10), "link": {"url": m.group(11)}}})

        pos = m.end()

    if pos < len(text):
        segments.append({"type": "text", "text": {"content": text[pos:]}})

    if not segments:
        segments.append({"type": "text", "text": {"content": text}})

    return segments


def heading_block(level, text):
    key = f"heading_{level}"
    return {"type": key, key: {"rich_text": rich_text(text)}}


def paragraph_block(text):
    return {"type": "paragraph", "paragraph": {"rich_text": rich_text(text)}}


def bullet_block(text):
    return {"type": "bulleted_list_item", "bulleted_list_item": {"rich_text": rich_text(text)}}


def numbered_block(text):
    return {"type": "numbered_list_item", "numbered_list_item": {"rich_text": rich_text(text)}}


def quote_block(text):
    return {"type": "quote", "quote": {"rich_text": rich_text(text)}}


def code_block(code, language="plain text"):
    return {"type": "code", "code": {"rich_text": [{"type": "text", "text": {"content": code}}], "language": language}}


def divider_block():
    return {"type": "divider", "divider": {}}


def blocks_to_markdown(blocks):
    """Convert Notion API blocks back to markdown text."""
    lines = []
    for block in blocks:
        btype = block["type"]
        if btype == "heading_1":
            lines.append(f"# {extract_text(block['heading_1']['rich_text'])}")
        elif btype == "heading_2":
            lines.append(f"## {extract_text(block['heading_2']['rich_text'])}")
        elif btype == "heading_3":
            lines.append(f"### {extract_text(block['heading_3']['rich_text'])}")
        elif btype == "paragraph":
            text = extract_text(block["paragraph"]["rich_text"])
            lines.append(text if text else "")
        elif btype == "bulleted_list_item":
            lines.append(f"- {extract_text(block['bulleted_list_item']['rich_text'])}")
        elif btype == "numbered_list_item":
            lines.append(f"1. {extract_text(block['numbered_list_item']['rich_text'])}")
        elif btype == "quote":
            lines.append(f"> {extract_text(block['quote']['rich_text'])}")
        elif btype == "code":
            lang = block["code"].get("language", "")
            code_text = extract_text(block["code"]["rich_text"])
            lines.append(f"```{lang}")
            lines.append(code_text)
            lines.append("```")
        elif btype == "divider":
            lines.append("---")
        elif btype == "child_page":
            pass  # skip child page references
        elif btype == "toggle":
            lines.append(f"**{extract_text(block['toggle']['rich_text'])}**")
        elif btype == "callout":
            lines.append(f"> {extract_text(block['callout']['rich_text'])}")
        elif btype == "to_do":
            checked = block["to_do"].get("checked", False)
            marker = "[x]" if checked else "[ ]"
            lines.append(f"- {marker} {extract_text(block['to_do']['rich_text'])}")
        else:
            pass  # skip unsupported block types

        lines.append("")

    # Clean up trailing blank lines
    while lines and not lines[-1].strip():
        lines.pop()

    return "\n".join(lines) + "\n"


def extract_text(rich_text_array):
    """Convert Notion rich_text array back to markdown-formatted text."""
    parts = []
    for seg in rich_text_array:
        text = seg.get("plain_text", seg.get("text", {}).get("content", ""))
        ann = seg.get("annotations", {})
        href = seg.get("href") or seg.get("text", {}).get("link", {})
        if isinstance(href, dict):
            href = href.get("url")

        if href:
            text = f"[{text}]({href})"
        elif ann.get("code"):
            text = f"`{text}`"
        elif ann.get("bold") and ann.get("italic"):
            text = f"***{text}***"
        elif ann.get("bold"):
            text = f"**{text}**"
        elif ann.get("italic"):
            text = f"*{text}*"

        parts.append(text)
    return "".join(parts)


# --- Sync logic ---

def find_local_md_files(manifest):
    """Find all .md files in sync directories, excluding skip_files."""
    skip = set(manifest.get("skip_files", []))
    files = []
    for sync_dir in SYNC_DIRS:
        dir_path = WORKSPACE / sync_dir
        if not dir_path.exists():
            continue
        for md_file in sorted(dir_path.rglob("*.md")):
            rel = str(md_file.relative_to(WORKSPACE))
            if rel not in skip:
                files.append(rel)
    return files


def find_section_for_file(manifest, local_path):
    """Determine which Notion section a local file belongs to."""
    parts = Path(local_path).parts
    if len(parts) >= 2:
        section_key = str(Path(parts[0]) / parts[1])
        return manifest["sections"].get(section_key)
    elif parts[0] in ("Tasks",):
        return manifest["sections"].get("Tasks")
    return None


def get_file_mapping(manifest, local_path):
    """Find existing mapping for a local path."""
    for entry in manifest["files"]:
        if entry["local_path"] == local_path:
            return entry
    return None


def sync_file_to_notion(token, manifest, local_path, dry_run=False):
    """Push local file content to its Notion page."""
    mapping = get_file_mapping(manifest, local_path)
    filepath = WORKSPACE / local_path
    content = filepath.read_text(encoding="utf-8")
    blocks = markdown_to_blocks(content)

    if mapping and mapping.get("notion_page_id"):
        page_id = mapping["notion_page_id"]
        if not dry_run:
            existing_blocks = notion_get_blocks(token, page_id)
            for b in existing_blocks:
                if b["type"] != "child_page":
                    notion_delete_block(token, b["id"].replace("-", ""))
                    time.sleep(0.1)
            if blocks:
                notion_append_blocks(token, page_id, blocks)
            mapping["last_sync_hash"] = file_hash(filepath)
            mapping["last_sync_time"] = datetime.now(timezone.utc).isoformat()
        return "updated", mapping["notion_page_id"]
    else:
        section_id = find_section_for_file(manifest, local_path)
        if not section_id:
            return "skipped (no section)", None
        title = title_from_filename(local_path)
        if not dry_run:
            new_id = notion_create_page(token, section_id, title, blocks)
            new_mapping = {
                "local_path": local_path,
                "notion_page_id": new_id,
                "last_sync_hash": file_hash(filepath),
                "last_sync_time": datetime.now(timezone.utc).isoformat(),
            }
            manifest["files"].append(new_mapping)
            return "created", new_id
        return "would create", None


def sync_notion_to_local(token, manifest, local_path, dry_run=False):
    """Pull Notion page content to local file."""
    mapping = get_file_mapping(manifest, local_path)
    if not mapping or not mapping.get("notion_page_id"):
        return "skipped (no mapping)"

    page_id = mapping["notion_page_id"]
    if not dry_run:
        blocks = notion_get_blocks(token, page_id)
        md_content = blocks_to_markdown(blocks)
        filepath = WORKSPACE / local_path
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(md_content, encoding="utf-8")
        mapping["last_sync_hash"] = file_hash(filepath)
        mapping["last_sync_time"] = datetime.now(timezone.utc).isoformat()
    return "updated"


def discover_new_notion_pages(token, manifest):
    """Find Notion pages under the hub that aren't mapped to local files."""
    new_pages = []
    mapped_ids = {e["notion_page_id"] for e in manifest["files"]}

    for section_dir, section_id in manifest["sections"].items():
        child_pages = notion_get_child_pages(token, section_id)
        for page in child_pages:
            if page["id"] not in mapped_ids:
                new_pages.append({
                    "notion_page_id": page["id"],
                    "title": page["title"],
                    "section_dir": section_dir,
                })
    return new_pages


def pull_new_notion_page(token, manifest, page_info, dry_run=False):
    """Create a local file from a new Notion page."""
    slug = page_info["title"].lower().replace(" ", "-")
    slug = re.sub(r"[^a-z0-9\-]", "", slug)
    slug = re.sub(r"-+", "-", slug).strip("-")
    local_path = f"{page_info['section_dir']}/{slug}.md"

    filepath = WORKSPACE / local_path
    if filepath.exists():
        return local_path, "skipped (file exists)"

    if not dry_run:
        blocks = notion_get_blocks(token, page_info["notion_page_id"])
        md_content = blocks_to_markdown(blocks)
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.write_text(md_content, encoding="utf-8")
        manifest["files"].append({
            "local_path": local_path,
            "notion_page_id": page_info["notion_page_id"],
            "last_sync_hash": file_hash(filepath),
            "last_sync_time": datetime.now(timezone.utc).isoformat(),
        })
    return local_path, "created"


def determine_sync_direction(token, manifest, local_path):
    """Decide whether to push local→Notion or pull Notion→local."""
    mapping = get_file_mapping(manifest, local_path)
    filepath = WORKSPACE / local_path

    if not mapping or not mapping.get("notion_page_id"):
        return "push"

    current_hash = file_hash(filepath)
    local_changed = mapping.get("last_sync_hash") is None or current_hash != mapping["last_sync_hash"]

    try:
        page = notion_get_page(token, mapping["notion_page_id"])
        notion_edited = datetime.fromisoformat(page["last_edited_time"].replace("Z", "+00:00"))
    except requests.HTTPError:
        return "push" if local_changed else "skip"

    if mapping.get("last_sync_time"):
        last_sync = datetime.fromisoformat(mapping["last_sync_time"])
        notion_changed = notion_edited > last_sync
    else:
        notion_changed = True

    if local_changed and notion_changed:
        local_mtime = file_mtime_utc(filepath)
        return "push" if local_mtime > notion_edited else "pull"
    elif local_changed:
        return "push"
    elif notion_changed:
        return "pull"
    return "skip"


def run_sync(dry_run=False, status_only=False):
    token = load_config()
    manifest = load_manifest()
    actions = []

    print(f"{'[DRY RUN] ' if dry_run else ''}Syncing with Notion Knowledge Hub...")
    print(f"Hub: {manifest['notion_hub_id']}")
    print()

    local_files = find_local_md_files(manifest)
    mapped_paths = {e["local_path"] for e in manifest["files"]}
    new_local = [f for f in local_files if f not in mapped_paths]
    existing = [f for f in local_files if f in mapped_paths]

    for local_path in existing:
        direction = determine_sync_direction(token, manifest, local_path)
        if status_only:
            status_label = {"push": "local newer", "pull": "Notion newer", "skip": "in sync"}
            print(f"  {status_label.get(direction, direction):>14}  {local_path}")
            continue

        if direction == "push":
            result, page_id = sync_file_to_notion(token, manifest, local_path, dry_run)
            actions.append(f"  → Notion  {local_path}  ({result})")
            print(f"  → Notion  {local_path}")
        elif direction == "pull":
            result = sync_notion_to_local(token, manifest, local_path, dry_run)
            actions.append(f"  ← Notion  {local_path}  ({result})")
            print(f"  ← Notion  {local_path}")
        else:
            print(f"  ✓ in sync  {local_path}")

        time.sleep(0.15)

    if status_only:
        for f in new_local:
            print(f"  {'new local':>14}  {f}")
        print(f"\n{len(existing)} mapped | {len(new_local)} new local")
        return

    for local_path in new_local:
        result, page_id = sync_file_to_notion(token, manifest, local_path, dry_run)
        actions.append(f"  + Notion  {local_path}  ({result})")
        print(f"  + Notion  {local_path}  ({result})")
        time.sleep(0.15)

    print("\nChecking for new Notion pages...")
    new_notion_pages = discover_new_notion_pages(token, manifest)
    for page_info in new_notion_pages:
        local_path, result = pull_new_notion_page(token, manifest, page_info, dry_run)
        actions.append(f"  + Local   {local_path}  ({result})")
        print(f"  + Local   {local_path}  ({result})")
        time.sleep(0.15)

    if not dry_run:
        save_manifest(manifest)

    print(f"\n--- Summary ---")
    print(f"Files checked: {len(existing) + len(new_local)}")
    print(f"Actions taken: {len(actions)}")
    if new_notion_pages:
        print(f"New from Notion: {len(new_notion_pages)}")
    for a in actions:
        print(a)
    print()


def main():
    parser = argparse.ArgumentParser(description="Sync local markdown files with Notion Knowledge Hub")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without syncing")
    parser.add_argument("--status", action="store_true", help="Show sync status only")
    args = parser.parse_args()

    if not MANIFEST_PATH.exists():
        print(f"ERROR: Manifest not found at {MANIFEST_PATH}")
        sys.exit(1)

    if args.status:
        run_sync(status_only=True)
    else:
        run_sync(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
