# Yashika's Engineering Lab — setup

This folder is a starter kit for the profile repository `Yashika-Agrawal/Yashika-Agrawal`.

## Install

1. Create (or open) the GitHub repository named exactly `Yashika-Agrawal`.
2. Copy the contents of this folder into the repository root.
3. Commit and push to the default branch.
4. In **Settings → Actions → General → Workflow permissions**, allow GitHub Actions to read and write repository contents.
5. Run **Actions → Generate contribution snake → Run workflow** once.
6. After it succeeds, the `output` branch will contain the snake SVGs. The README references those assets.

## Update the lab dashboard

Edit `data/lab.json` and commit the change. The `Update engineering lab section` workflow updates the marked section in `README.md`.

Example:

```json
{
  "building": ["RailRush", "IncidentCopilot"],
  "exploring": ["PostgreSQL indexing", "HTTP internals", "Docker networking"],
  "recent_experiment": {
    "title": "Understanding database indexes",
    "url": "https://github.com/Yashika-Agrawal/engineering-playground"
  },
  "latest_note": {
    "title": "My notes on B-tree indexes",
    "url": "https://github.com/Yashika-Agrawal/engineering-playground"
  }
}
```

Use real links for your notes and experiments. The example links above are placeholders to replace with the exact file URLs.

## Important notes

- GitHub README does not run arbitrary JavaScript. The terminal and concept map are SVG images, not interactive web apps.
- The terminal SVG has a subtle blinking cursor. If GitHub's image sanitizer suppresses SVG animation, it will still render as a static terminal.
- GitHub Actions schedules can be delayed by GitHub during high load.
- The GitHub stats cards are served by a third-party service. If they become unavailable, remove that section rather than adding more stats providers.
- Add repository links for RailRush and IncidentCopilot only when you have the correct public URLs.
- No personal portrait is used.
