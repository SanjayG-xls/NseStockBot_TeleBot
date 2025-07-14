# ALZAPWVD1W9W74ASJXE2PQYA   recovry

from nsepython import nse_eq
from twilio.rest import Client
import schedule
import time

account_sid = 'ACce508ff0e6e99f5a186506de8f4aca67'
auth_token = '8d1a4c16530ab95104c7a0647734064'
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+917806878387'

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
