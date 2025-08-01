from nsepython import nse_eq
import requests
import os
import datetime

bot_token = os.environ['XLSXNSE_BOT_TOKEN']
chat_id = os.environ['XLSXNSE_CHAT_ID']

stocks = ['SOUTHBANK', 'IDFCFIRSTB', 'PGINVIT', 'GOLDBEES', 'MRF']

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': msg}
    response = requests.post(url, data=payload)
    
    print("Status Code:", response.status_code)
    print("Response:", response.text)  # TEMP: Debug only



