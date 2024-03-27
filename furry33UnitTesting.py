import requests
from datetime import datetime
import pytz
import time

IST = pytz.timezone('UTC')
raw_TS = datetime.now(IST)
cur_date = raw_TS.strftime('%d-%m-%Y')
cur_time = raw_TS.strftime('%H-%M-%S')

tele_token = '7044142802:AAENqoKd-jUX3yJdcdSEiPm5VsGd5G26Ybk'
tele_group = 'unitTesting_furry33'

msg = f'Message Received on {cur_date} at {cur_time}'

def send_message(message):
    tele_api_url = f'https://api.telegram.org/bot{tele_token}/sendMessage?chat_id=@{tele_group}&text={message}'
    tele_resp = requests.get(tele_api_url)

    if tele_resp.status_code == 200:
        print('[!]Successfully Send a message')
    else:
        print('[x]Failed')

try:
    while True:
        send_message(msg)
        time.sleep(3)
except KeyboardInterrupt:
    print('program exit')