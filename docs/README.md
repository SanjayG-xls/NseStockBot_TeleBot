# 📈 Telegram Stock Bot

This is a scheduled Python bot that fetches stock prices using **Yahoo Finance** and sends updates to a **Telegram chat** via a bot.

## 🚀 Features

- Gets real-time stock prices using `yfinance`
- Sends formatted messages to a Telegram chat
- Scheduled to run at **9:30 AM** and **2:00 PM IST** daily via **GitHub Actions**
- Securely uses GitHub Secrets for bot token and chat ID

## 🛠️ Technologies Used

- Python 3.11
- `yfinance` for stock data
- Telegram Bot API
- GitHub Actions for automation

## 📦 Installation

Clone this repository:

```bash
git clone https://github.com/yourusername/telegram-stock-bot.git
cd telegram-stock-bot
