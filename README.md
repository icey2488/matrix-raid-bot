# matrix-raid-bot

A modular Matrix bot for managing World of Warcraft raid signups, attendance, and roster validation. Built for operational automation and open-source scalability.

---

## 🧱 Architecture Overview
matrix_raid_bot/ ├── commands/         # Handles bot commands (signup, roster, attendance) ├── database/         # SQLite persistence layer ├── services/         # External integrations (WoWAudit, WCL, scheduler) ├── util/             # Formatting and Matrix helpers ├── entrypoint.py     # Main wiring for services and commands ├── Dockerfile        # Containerized deployment ├── docker-compose.yml ├── requirements.txt

---

## 🚀 Getting Started

### 1. Clone and install dependencies

```bash
git clone https://github.com/yourname/matrix-raid-bot.git
cd matrix-raid-bot
pip install -r requirements.txt

2. Set environment variables
Create a .env file or export manually


WCL_API_KEY=your_wcl_token
WOWAUDIT_API_KEY=your_wowaudit_token

3. Run the bot

python matrix_raid_bot/entrypoint.py

🧩 Features
- Signup tracking: Raid signups with status updates and roster validation
- Roster sync: Pulls guild roster from WoWAudit
- Attendance summaries: Parses WCL logs for raid participation
- Modular services: Easy to extend and maintain
- SQLite backend: Lightweight and audit-friendly

🛠️ Development
Linting

flake8 matrix_raid_bot/

Docker
docker-compose up --build

📄 License
MIT — see LICENSE


