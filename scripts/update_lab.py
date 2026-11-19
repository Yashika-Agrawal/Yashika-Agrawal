#!/usr/bin/env python3
"""Update the LAB section in README.md and regenerate assets/terminal.svg with live GitHub commit data."""
from html import escape
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
USERNAME = os.environ.get("GITHUB_USERNAME", "Yashika-Agrawal")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "").strip()


def github_get(url: str):
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": f"{USERNAME}-engineering-lab",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


def is_bot_commit(author: str, message: str) -> bool:
    author_l = (author or "").lower()
    msg_l = (message or "").strip().lower()
    if "[bot]" in author_l or "github-actions" in author_l:
        return True
    if msg_l.startswith("chore: update engineering lab") or msg_l.startswith("chore: update 3d"):
        return True
    return False


def truncate(text: str, limit: int) -> str:
    clean = " ".join((text or "").splitlines()[0].split())
    return clean if len(clean) <= limit else clean[: limit - 1].rstrip() + "…"


def fetch_latest_commit():
    """Fetch the most recent non-bot public commit across the user's repositories."""
    candidates = []

    # 1. Try public events first for immediate push activity
    try:
        events = github_get(f"https://api.github.com/users/{USERNAME}/events/public?per_page=30")
        for event in events:
            if event.get("type") != "PushEvent":
                continue
            repo_full = event.get("repo", {}).get("name", "")
            repo_short = repo_full.split("/")[-1] if "/" in repo_full else repo_full
            payload = event.get("payload", {})
            commits = payload.get("commits") or []
            for commit in reversed(commits):
                author = commit.get("author", {}).get("name", "")
                message = commit.get("message", "")
                sha = commit.get("sha", "")
                if not sha or is_bot_commit(author, message):
                    continue
                candidates.append({
                    "repo": repo_short,
                    "repo_full": repo_full,
                    "sha": sha[:7],
                    "message": truncate(message, 68),
                    "url": f"https://github.com/{repo_full}/commit/{sha}",
                })
                break
            if candidates:
                # Prefer a non-profile repo if we already found one; otherwise keep looking once
                if any(c["repo"].lower() != USERNAME.lower() for c in candidates):
                    break
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        pass

    # Prefer a project repo over the profile repo itself if available
    for c in candidates:
        if c["repo"].lower() != USERNAME.lower():
            return c
    if candidates:
        return candidates[0]

    # 2. Fallback: inspect recently pushed public repos directly
    try:
        repos = github_get(f"https://api.github.com/users/{USERNAME}/repos?sort=pushed&per_page=10")
        # Order non-profile repos first, then profile repo
        ordered = [r for r in repos if r.get("name", "").lower() != USERNAME.lower()] + [
            r for r in repos if r.get("name", "").lower() == USERNAME.lower()
        ]
        for repo in ordered:
            repo_full = repo.get("full_name", "")
            repo_short = repo.get("name", "")
            if not repo_full:
                continue
            try:
                commits = github_get(f"https://api.github.com/repos/{repo_full}/commits?per_page=5")
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
                continue
            for c in commits:
                commit_info = c.get("commit", {})
                author = commit_info.get("author", {}).get("name", "")
                message = commit_info.get("message", "")
                sha = c.get("sha", "")
                if not sha or is_bot_commit(author, message):
                    continue
                return {
                    "repo": repo_short,
                    "repo_full": repo_full,
                    "sha": sha[:7],
                    "message": truncate(message, 68),
                    "url": c.get("html_url") or f"https://github.com/{repo_full}/commit/{sha}",
                }
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        pass

    return None


def render_terminal_svg(commit):
    repo_label = escape(commit["repo"]) if commit else "engineering-playground"
    commit_sha = escape(commit["sha"]) if commit else "main"
    commit_msg = escape(commit["message"]) if commit else "building full-stack projects & DevOps experiments"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="920" height="380" viewBox="0 0 920 380" fill="none">
  <defs>
    <linearGradient id="termBg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0b0f17"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="headerBorder" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#34d399" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#818cf8" stop-opacity="0.2"/>
    </linearGradient>
    <style>
      @keyframes blink {{
        0%, 49% {{ opacity: 1; }}
        50%, 100% {{ opacity: 0; }}
      }}
      @keyframes line1 {{
        0% {{ opacity: 0; }}
        4% {{ opacity: 1; }}
        100% {{ opacity: 1; }}
      }}
      @keyframes out1 {{
        0%, 7% {{ opacity: 0; transform: translateY(4px); }}
        10% {{ opacity: 1; transform: translateY(0); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes line2 {{
        0%, 16% {{ opacity: 0; }}
        19% {{ opacity: 1; }}
        100% {{ opacity: 1; }}
      }}
      @keyframes out2 {{
        0%, 23% {{ opacity: 0; transform: translateY(4px); }}
        26% {{ opacity: 1; transform: translateY(0); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes line3 {{
        0%, 35% {{ opacity: 0; }}
        38% {{ opacity: 1; }}
        100% {{ opacity: 1; }}
      }}
      @keyframes out3 {{
        0%, 42% {{ opacity: 0; transform: translateY(4px); }}
        45% {{ opacity: 1; transform: translateY(0); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes line4 {{
        0%, 53% {{ opacity: 0; }}
        56% {{ opacity: 1; }}
        100% {{ opacity: 1; }}
      }}
      @keyframes out4 {{
        0%, 60% {{ opacity: 0; transform: translateY(4px); }}
        63% {{ opacity: 1; transform: translateY(0); }}
        100% {{ opacity: 1; transform: translateY(0); }}
      }}

      .cursor {{
        animation: blink 0.9s infinite;
      }}
      .l1 {{ animation: line1 14s infinite; }}
      .o1 {{ animation: out1 14s infinite; }}
      .l2 {{ animation: line2 14s infinite; }}
      .o2 {{ animation: out2 14s infinite; }}
      .l3 {{ animation: line3 14s infinite; }}
      .o3 {{ animation: out3 14s infinite; }}
      .l4 {{ animation: line4 14s infinite; }}
      .o4 {{ animation: out4 14s infinite; }}

      .mono {{
        font-family: 'SF Mono', 'Fira Code', 'JetBrains Mono', Menlo, Consolas, monospace;
      }}
    </style>
  </defs>

  <!-- Window Chrome -->
  <rect x="1" y="1" width="918" height="378" rx="14" fill="url(#termBg)" stroke="#1e293b" stroke-width="1.5"/>
  <rect x="1" y="1" width="918" height="42" rx="14" fill="#0f172a" fill-opacity="0.9"/>
  <line x1="1" y1="42" x2="919" y2="42" stroke="url(#headerBorder)" stroke-width="1"/>

  <!-- Traffic Lights -->
  <circle cx="24" cy="21" r="6" fill="#ef4444"/>
  <circle cx="44" cy="21" r="6" fill="#f59e0b"/>
  <circle cx="64" cy="21" r="6" fill="#10b981"/>

  <text x="460" y="26" text-anchor="middle" fill="#64748b" class="mono" font-size="13">yashika@engineering-lab:~ (zsh)</text>

  <!-- Line 1: whoami -->
  <g class="l1">
    <text x="32" y="80" fill="#38bdf8" class="mono" font-size="15" font-weight="600">yashika@lab:~$</text>
    <text x="165" y="80" fill="#f8fafc" class="mono" font-size="15">whoami</text>
  </g>
  <g class="o1">
    <text x="32" y="108" fill="#34d399" class="mono" font-size="15" font-weight="600">➜</text>
    <text x="56" y="108" fill="#f1f5f9" class="mono" font-size="15" font-weight="700">Yashika Agrawal</text>
    <text x="210" y="108" fill="#94a3b8" class="mono" font-size="14">· Software Engineer (Full Stack)</text>
  </g>

  <!-- Line 2: current focus -->
  <g class="l2">
    <text x="32" y="152" fill="#38bdf8" class="mono" font-size="15" font-weight="600">yashika@lab:~$</text>
    <text x="165" y="152" fill="#f8fafc" class="mono" font-size="15">cat current_focus.json</text>
  </g>
  <g class="o2">
    <text x="32" y="180" fill="#cbd5e1" class="mono" font-size="14">{{</text>
    <text x="52" y="180" fill="#a5b4fc" class="mono" font-size="14">"stack":</text>
    <text x="115" y="180" fill="#fef08a" class="mono" font-size="14">"Full Stack (.NET, React, Node.js, PostgreSQL)"</text>
    <text x="525" y="180" fill="#cbd5e1" class="mono" font-size="14">, </text>
    <text x="545" y="180" fill="#a5b4fc" class="mono" font-size="14">"learning":</text>
    <text x="640" y="180" fill="#fef08a" class="mono" font-size="14">"Linux &amp; DevOps"</text>
    <text x="795" y="180" fill="#cbd5e1" class="mono" font-size="14">}}</text>
  </g>

  <!-- Line 3: live git log -->
  <g class="l3">
    <text x="32" y="226" fill="#38bdf8" class="mono" font-size="15" font-weight="600">yashika@lab:~$</text>
    <text x="165" y="226" fill="#f8fafc" class="mono" font-size="15">git log --oneline -1 {repo_label}</text>
  </g>
  <g class="o3">
    <text x="32" y="254" fill="#fbbf24" class="mono" font-size="14" font-weight="bold">{commit_sha}</text>
    <text x="110" y="254" fill="#e2e8f0" class="mono" font-size="14">{commit_msg}</text>
  </g>

  <!-- Line 4: status -->
  <g class="l4">
    <text x="32" y="300" fill="#38bdf8" class="mono" font-size="15" font-weight="600">yashika@lab:~$</text>
    <text x="165" y="300" fill="#f8fafc" class="mono" font-size="15">./lab-status.sh</text>
  </g>
  <g class="o4">
    <rect x="32" y="318" width="10" height="10" rx="2" fill="#10b981"/>
    <text x="52" y="328" fill="#34d399" class="mono" font-size="14" font-weight="600">ONLINE</text>
    <text x="120" y="328" fill="#94a3b8" class="mono" font-size="14">· Building full-stack systems &amp; exploring how software works under the hood</text>
    <rect x="765" y="316" width="9" height="16" fill="#34d399" class="cursor"/>
  </g>

</svg>
"""


def item(value):
    if isinstance(value, dict):
        title = value.get("title", "Untitled")
        url = value.get("url", "").strip()
        return f"[{title}]({url})" if url else title
    return str(value)


def joined(values):
    return " · ".join(item(v) for v in values) if values else "Add details in data/lab.json"


def main():
    data = json.loads((ROOT / "data" / "lab.json").read_text(encoding="utf-8"))
    latest_commit = fetch_latest_commit()

    # 1. Regenerate assets/terminal.svg with live commit
    terminal_path = ROOT / "assets" / "terminal.svg"
    if latest_commit or not terminal_path.exists():
        terminal_path.write_text(render_terminal_svg(latest_commit), encoding="utf-8")
        if latest_commit:
            print(f"Updated terminal.svg with {latest_commit['repo']}@{latest_commit['sha']}: {latest_commit['message']}")
        else:
            print("GitHub API unavailable; wrote default terminal.svg.")

    # 2. Update LAB section in README.md
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

    if latest_commit:
        msg_escaped = latest_commit["message"].replace("|", "\\|")
        rows.append(
            f"| 🕒 **Latest Commit** | [`{latest_commit['sha']}`]({latest_commit['url']}) {msg_escaped} (`{latest_commit['repo']}`) |"
        )

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


if __name__ == "__main__":
    main()
