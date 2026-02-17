# Contributing to matrix-raid-bot

Thanks for your interest in contributing! This bot is built for modularity, maintainability, and community collaboration. Whether you're fixing a bug, adding a feature, or improving documentation — you're welcome here.

---

## 🧰 Project Structure

matrix_raid_bot/ ├── commands/         # Bot commands (signup, roster, attendance) ├── database/         # SQLite logic ├── services/         # External APIs (WoWAudit, WCL, scheduler) ├── util/             # Formatting and Matrix helpers ├── entrypoint.py     # Main wiring


---

## 🚀 Setup

1. Clone the repo:

```bash
git clone https://github.com/yourname/matrix-raid-bot.git
cd matrix-raid-bot

2. Install dependencies:

pip install -r requirements.txt

3.  Set environment variables: 

export WCL_API_KEY=your_wcl_token
export WOWAUDIT_API_KEY=your_wowaudit_token

🧪 Development Workflow
- Use feature branches: git checkout -b feature/my-new-command
- Follow modular patterns: keep logic isolated in commands/, services/, etc.
- Run lint checks before committing:

flake8 matrix_raid_bot/

Use clear, conventional commit messages:

git commit -m "feat: add signup status filter"

🧼 Code Style
- Python 3.11+
- PEP8 compliant
- Prefer async for I/O-bound services
- Avoid cross-module coupling — use dependency injection

🧪 Testing
Unit tests coming soon. For now, test manually by running:

python matrix_raid_bot/entrypoint.py

🤝 How to Contribute
- Fork the repo
- Create a feature branch
- Make your changes
- Commit with a descriptive message
- Push and open a pull request

📄 License
MIT — see LICENSE




