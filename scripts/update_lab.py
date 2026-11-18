#!/usr/bin/env python3
"""Update the LAB section in README.md from data/lab.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data" / "lab.json").read_text(encoding="utf-8"))

def item(value):
    if isinstance(value, dict):
        title = value.get("title", "Untitled")
        url = value.get("url", "").strip()
        return f"[{title}]({url})" if url else title
    return str(value)

def joined(values):
    return " · ".join(item(v) for v in values) if values else "Add details in data/lab.json"

experiment = item(data.get("recent_experiment", {}))
note = item(data.get("latest_note", {}))
today = item(data.get("today_i_learned", {}))

rows = [
    "| Area | Current Focus / Live Pulse |",
    "|---|---|",
    f"| 🚀 **Building** | {joined(data.get('building', []))} |",
    f"| 🔍 **Exploring** | {joined(data.get('exploring', []))} |",
    f"| 🧪 **Latest Experiment** | {experiment} |",
    f"| 📝 **Engineering Note** | {note} |",
]

if today and today != "Untitled":
    rows.append(f"| 💡 **Today I Learned** | {today} |")

section = "\n".join(rows)

readme_path = ROOT / "README.md"
readme = readme_path.read_text(encoding="utf-8")
start, end = "<!-- LAB:START -->", "<!-- LAB:END -->"
if start not in readme or end not in readme:
    raise SystemExit("README is missing LAB markers.")
before, rest = readme.split(start, 1)
_, after = rest.split(end, 1)
readme_path.write_text(before + start + "\n" + section + "\n" + end + after, encoding="utf-8")
print("Updated README lab section.")
