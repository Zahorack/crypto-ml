from pycoingecko import CoinGeckoAPI
import numpy as np
import pandas as pd
import itertools
import time_data
import os


def to_numpy_array(data):
    ret_val = list(list())
    
    print("Unpacking data")

    [prices, market_caps, total_volumes] = [list(zip(*data["prices"])), list(zip(*data["market_caps"])),
                                            list(zip(*data["total_volumes"]))]

    if data_are_corrupted([prices, market_caps, total_volumes]):
        return []
    for (timestamp, price, market_cap, volume) in itertools.zip_longest(prices[0], prices[1], market_caps[1],
                                                                        total_volumes[1], fillvalue='empty'):
        ret_val.append([time_data.oversized_timestamp_to_date(timestamp), timestamp / 1000.0, price, market_cap, volume])
    
    print("Unpacked successfully")
    
    return np.array(ret_val)


def data_are_corrupted(data):
    [prices, market_caps, total_volumes] = data

    return len(prices) == 0 or len(market_caps) == 0 or len(total_volumes) == 0

def unzip_coin_gecko_data(coin_gecko_data):
    if data_are_corrupted(coin_gecko_data):
        print("Data Corrupted")
        return {}
    
    print("Data OK")
    
    return to_numpy_array(coin_gecko_data)


def create_csv(data, coin_name, address, from_date_timestamp, to_date_timestamp):
    addr = address

    os.makedirs(addr, exist_ok=True)
    
    print("Creating .csv on address " + addr)

    data.to_csv(addr + '/' + coin_name +
                '_from_' + time_data.to_date(float(from_date_timestamp)) +
                '_to_' + time_data.to_date(float(to_date_timestamp))
                )


class LearningDataCreator:
    coin_gecko: CoinGeckoAPI
    currency_using: str
    last_used_timestamp: str

    data_empty: bool
    def __init__(self, currency_using):
        self.coin_gecko = CoinGeckoAPI()
        self.currency_using = currency_using

    def get_data_in_time_interval(self, from_t, to_t, coin):
        print("Requesting server")
        
        result = self.coin_gecko.get_coin_market_chart_range_by_id(
            id=coin,
            vs_currency=self.currency_using,
            from_timestamp=from_t,
            to_timestamp=to_t
        )
        
        print("Request Ok")

        return unzip_coin_gecko_data(result)

    def create_csv_from_data_interval(self, address, coin, time_interval):
        [from_t, to_t] = time_interval

        data = self.get_data_in_time_interval(from_t=from_t, to_t=to_t, coin=coin)

        if len(data) == 0:
            return
        data_frame = self.get_standard_data_frame(data=data)

        create_csv(data=data_frame, coin_name=coin, address=address, from_date_timestamp=from_t, to_date_timestamp=to_t)

    def get_standard_data_frame(self, data):  
        data_frame = pd.DataFrame(data, columns=["date", "timestamp", "price in: " + self.currency_using, "market_cap", "volume"])
        data_frame.sort_values(by="timestamp")
        
        print("Creating sorted data frame")

        last_date = data_frame["date"].to_numpy()
        last_timestamp = data_frame["timestamp"].to_numpy()

        self.last_used_timestamp = last_date[len(last_date) - 1] + ',' + str(last_timestamp[len(last_timestamp) - 1])

        return data_frame
