# ⚔️ Matrix Raid Attendance Bot

[![Linting Status](https://github.com/icey2488/matrix-raid-bot/actions/workflows/lint.yml/badge.svg)](https://github.com/icey2488/matrix-raid-bot/actions)

A professional-grade Matrix bot for WoW Guilds, featuring automatic scheduling, character verification via Warcraft Logs, and real-time attendance tracking with class-colored UI.

---

## ✨ Features

* **Verified Rosters:** Link Matrix accounts to WoW characters via Warcraft Logs V2 API.
* **Auto-Scheduling:** Automatically posts raid matrices 7 days before the start time.
* **Smart UI:** Uses HTML formatting for a clean "wowaudit" look with official Blizzard class colors.
* **Auto-Locking:** Signups close automatically exactly when the raid starts.
* **Robust Storage:** Powered by SQLite with Docker persistence.

---

## 🏗 System Architecture



The bot utilizes an asynchronous event loop to handle Matrix messages and reactions, while a background task monitors the SQLite database to manage raid lifecycle events.

---

## 🚀 Quick Start

### 1. Prerequisites
* A Matrix account for the bot (User ID and Password).
* A [Warcraft Logs API Client](https://www.warcraftlogs.com/api/clients/).
* Docker & Docker Compose installed.

### 2. Configuration
Clone the repository and create your environment file:
```bash
git clone [https://github.com/yourusername/matrix-raid-bot.git](https://github.com/yourusername/matrix-raid-bot.git)
cd matrix-raid-bot
cp .env.example .env