from nsepython import nse_eq
import requests
import os 
import datetime

bot_token = os.environ['XLSXNSE_BOT_TOKEN']
chat_id = os.environ['XLSXNSE_CHAT_ID']

stocks = ['SOUTHBANK', 'IDFCFIRSTB', 'PGINVIT', 'GOLDBEES', 'MRF']

def get_stock_prices():
    message = "----------> 📈 NSE STOCKS INFO 📈<----------\n"
    for stock in stocks:
        try:
            data = nse_eq(stock)
            ltp = data['priceInfo']['lastPrice']
            message += f"{stock}: ₹{ltp}\n"
        except Exception as e:
            message += f"{stock}: ❌ Error fetching data\n"

    send_telegram(message)

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': msg}
    requests.post(url, data=payload)

if __name__ == "__main__":
    get_stock_prices()

