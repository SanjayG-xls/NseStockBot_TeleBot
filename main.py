from nsepython import nse_eq
import requests
import os 
import datetime

bot_token = os.environ['XLSXNSE_BOT_TOKEN']
chat_id = os.environ['XLSXNSE_CHAT_ID']

stocks = ['SOUTHBANK', 'IDFCFIRSTB', 'PGINVIT', 'GOLDBEES', 'MRF']

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': msg,
        'parse_mode': 'Markdown'
    }
    response = requests.post(url, data=payload)
    print("Telegram response:", response.text)

    get_stock_prices()


