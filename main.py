# ALZAPWVD1W9W74ASJXE2PQYA   recovry

from nsepython import nse_eq
from twilio.rest import Client
import schedule
import time
import os

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
from_whatsapp_number = os.getenv('FROM_WHATSAPP_NUMBER')
to_whatsapp_number = os.getenv('TO_WHATSAPP_NUMBER')

client = Client(account_sid, auth_token)

stocks = ['SOUTHBANK', 'IDFCFIRSTB', 'HDFCBANK' , 'SUZLON' , 'RPOWER']

def get_stock_prices():
    message = "📈 NSE Stock Prices Update:\n"
    for stock in stocks:
        try:
            data = nse_eq(stock)
            ltp = data['priceInfo']['lastPrice']
            message += f"{stock}: ₹{ltp}\n"
        except Exception as e:
            message += f"{stock}: Error fetching data\n"
    print(message)

    client.messages.create(
        body=message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    print("✅ WhatsApp message sent.")

# Schedule every 6 hours
schedule.every(6).hours.do(get_stock_prices)

print("Bot Started... You'll get WhatsApp every 6 hours.")
get_stock_prices()  # Send first message immediately

while True:
    schedule.run_pending()
    time.sleep(1)
