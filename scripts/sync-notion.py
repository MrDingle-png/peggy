#!/usr/bin/env python3
"""
One-way publish from local markdown files to Notion Knowledge Hub.

Git (Peggy repo) is the source of truth. This script pushes local changes
to Notion as a read-only mirror. It never pulls from Notion.

Usage:
    python3 scripts/sync-notion.py              # publish all changes
    python3 scripts/sync-notion.py --dry-run    # preview without changes
    python3 scripts/sync-notion.py --status     # show what would be published
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

SYNC_DIRS = ["Knowledge"]


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


# --- Markdown to Notion block conversion ---

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
            i += 1
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
        r"(\*\*\*(.+?)\*\*\*)"
        r"|(\*\*(.+?)\*\*)"
        r"|(\*(.+?)\*)"
        r"|(`(.+?)`)"
        r"|(\[([^\]]+)\]\(([^)]+)\))"
    )
    pos = 0
    for m in pattern.finditer(text):
        if m.start() > pos:
            segments.append({"type": "text", "text": {"content": text[pos:m.start()]}})

        if m.group(2):
            segments.append({"type": "text", "text": {"content": m.group(2)},
                             "annotations": {"bold": True, "italic": True}})
        elif m.group(4):
            segments.append({"type": "text", "text": {"content": m.group(4)},
                             "annotations": {"bold": True}})
        elif m.group(6):
            segments.append({"type": "text", "text": {"content": m.group(6)},
                             "annotations": {"italic": True}})
        elif m.group(8):
            segments.append({"type": "text", "text": {"content": m.group(8)},
                             "annotations": {"code": True}})
        elif m.group(10):
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


# --- Publish logic ---

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
    return None


def get_file_mapping(manifest, local_path):
    """Find existing mapping for a local path."""
    for entry in manifest["files"]:
        if entry["local_path"] == local_path:
            return entry
    return None


def has_local_changes(manifest, local_path):
    """Check if local file has changed since last publish."""
    mapping = get_file_mapping(manifest, local_path)
    filepath = WORKSPACE / local_path
    current_hash = file_hash(filepath)
    if not mapping or mapping.get("last_sync_hash") is None:
        return True
    return current_hash != mapping["last_sync_hash"]


def publish_file_to_notion(token, manifest, local_path, dry_run=False):
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


def run_publish(dry_run=False, status_only=False):
    token = load_config()
    manifest = load_manifest()
    actions = []

    print(f"{'[DRY RUN] ' if dry_run else ''}Publishing to Notion Knowledge Hub...")
    print(f"Hub: {manifest['notion_hub_id']}")
    print()

    local_files = find_local_md_files(manifest)
    mapped_paths = {e["local_path"] for e in manifest["files"]}
    new_local = [f for f in local_files if f not in mapped_paths]
    existing = [f for f in local_files if f in mapped_paths]

    for local_path in existing:
        changed = has_local_changes(manifest, local_path)

        if status_only:
            label = "changed" if changed else "up to date"
            print(f"  {label:>14}  {local_path}")
            continue

        if changed:
            result, page_id = publish_file_to_notion(token, manifest, local_path, dry_run)
            actions.append(f"  → Notion  {local_path}  ({result})")
            print(f"  → Notion  {local_path}")
        else:
            print(f"  ✓ up to date  {local_path}")

        time.sleep(0.15)

    if status_only:
        for f in new_local:
            print(f"  {'new':>14}  {f}")
        print(f"\n{len(existing)} mapped | {len(new_local)} new")
        return

    for local_path in new_local:
        result, page_id = publish_file_to_notion(token, manifest, local_path, dry_run)
        actions.append(f"  + Notion  {local_path}  ({result})")
        print(f"  + Notion  {local_path}  ({result})")
        time.sleep(0.15)

    if not dry_run:
        save_manifest(manifest)

    print(f"\n--- Summary ---")
    print(f"Files checked: {len(existing) + len(new_local)}")
    print(f"Published: {len(actions)}")
    for a in actions:
        print(a)
    print()


def main():
    parser = argparse.ArgumentParser(description="Publish local markdown files to Notion Knowledge Hub (one-way)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without publishing")
    parser.add_argument("--status", action="store_true", help="Show publish status only")
    args = parser.parse_args()

    if not MANIFEST_PATH.exists():
        print(f"ERROR: Manifest not found at {MANIFEST_PATH}")
        sys.exit(1)

    if args.status:
        run_publish(status_only=True)
    else:
        run_publish(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
