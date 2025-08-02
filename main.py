import yfinance as yf
import requests
import os


bot_token = os.getenv("XLSXNSE_BOT_TOKEN")
chat_id = os.getenv("XLSXNSE_CHAT_ID")

stocks = {
    'SOUTHBANK.NS': 'SOUTHBANK',
    'IDFCFIRSTB.NS': 'IDFCFIRSTB',
    'PGINVIT.NS': 'PGINVIT',
    'GOLDBEES.NS': 'GOLDBEES',
    'MRF.NS': 'MRF'
}

def get_stock_prices():
    message = "----------> 📈 NSE STOCKS INFO 📈<----------\n"
    for symbol, name in stocks.items():
        try:
            stock = yf.Ticker(symbol)
            price = stock.info['regularMarketPrice']
            message += f"{name}: ₹{price}\n"
        except Exception as e:
            print(f"Error fetching {name} ({symbol}): {e}")
            message += f"{name}: ❌ Error fetching data\n"

    send_telegram(message)

def send_telegram(msg):
    if not bot_token or not chat_id:
        print("Missing bot token or chat ID")
        return
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': msg}
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print(f"Failed to send Telegram message: {response.text}")

if __name__ == "__main__":
    get_stock_prices()

