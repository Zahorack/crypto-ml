import datetime
import time

from pytrends.request import TrendReq  # pip install pytrends - Written for both Python 2.7+ and Python 3.3+
from supported_coins import supported_coins
from datetime import date
import os

key_phrases_kernel = [
    [],
    ['should', 'I', 'sell', 'now'],
    ['should', 'I', 'buy', 'now'],
    ['falling'],
    ['going up'],
    ['losing value'],
    ['increase'],
    ['increasing value'],
    ['stagnation'],
    ['getting up'],
    ['up'],
    ['down']
]

for coin in supported_coins:

    os.makedirs(coin, exist_ok=True)

    for key_phrase in key_phrases_kernel:
        key_phrase.append(coin)

        dir_name = coin + '/' + "_".join(str(part) for part in key_phrase)

        os.makedirs(dir_name, exist_ok=True)

        start_date = datetime.date(2020, 11, 14)
        end_date = date.today()

        print("writing data to dir -> " + dir_name)

        while start_date <= end_date:
            try:
                api_request = str(start_date) + "T00 "

                start_date += datetime.timedelta(days=1)

                api_request += str(start_date) + "T00"

                api = TrendReq(timeout=30)

                api.build_payload(kw_list=key_phrase, timeframe=api_request)

                print("writing to csv name -> " + api_request)

                data_taken = api.interest_over_time()

                data_taken.to_csv(dir_name + "/" + api_request)

                break
            except Exception as error:
                print(error)
                time.sleep(30)
                continue

        key_phrase.pop()

