# 📈 Telegram Stock Bot

This is a scheduled Python bot that fetches stock prices using Yahoo Finance and sends updates to a Telegram chat via a bot.

💖 Support This Project
If you found this project useful or want to support its development, consider contributing:

👉 [![Support via Linktree](https://img.shields.io/badge/Support-Linktree-blueviolet?logo=buymeacoffee&style=flat-square)](https://linktr.ee/Sanjay_xlsX)

Every little bit helps! 🙌
---

## 🚀 Features

- ✅ Gets real-time stock prices using `yfinance`  
- ✅ Sends formatted messages to a Telegram chat  
- ✅ Scheduled to run at **9:30 AM** and **2:00 PM IST** daily via **GitHub Actions**  
- ✅ Securely uses **GitHub Secrets** for bot token and chat ID  

---

## 🛠️ Technologies Used

- Python 3.11  
- [yfinance](https://github.com/ranaroussi/yfinance) for stock data  
- Telegram Bot API  
- GitHub Actions for automation  

---

## 📦 Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/telegram-stock-bot.git
cd telegram-stock-bot

📤 Environment Variables
Make sure to set the following secrets in your GitHub repository:

XLSXNSE_BOT_TOKEN – Your Telegram bot token

XLSXNSE_CHAT_ID – Your Telegram chat ID (can be user or group)

These are passed automatically to the bot through GitHub Actions using the env section.

📆 GitHub Actions
The bot is automatically executed by a GitHub Action based on this schedule:

🕘 9:30 AM IST – 0 4 * * * (UTC)

🕑 2:00 PM IST – 30 8 * * * (UTC)

You can also manually trigger the workflow from the Actions tab in your repo.

💡 Example Message Sent

----------> 📈 NSE STOCKS INFO 📈<----------
TCS: ₹3575.25
INFY: ₹1455.10
RELIANCE: ₹2811.65
