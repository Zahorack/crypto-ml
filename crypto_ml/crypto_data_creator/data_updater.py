import coin_gecko_api_data_creator
import time_data
from time_data import TimeChain

class DataUpdater:
    address: str
    coin: str
    address: str
    currency: str
    last_timestamp: str

    def get_last_timestamp(self):
        print("Collecting last time capsule")
        file = open(self.address + "/last_timestamp", "r")
        [date, timestamp] = file.readline().split(',')

        self.last_timestamp = timestamp

    def __init__(self, address, coin, used_currency):
        self.address = address + "__" + coin
        self.coin = coin
        self.currency = used_currency

    def update(self):
    
        self.get_last_timestamp()
        
        print("Creating .csv data for 1 day with 4 minutes precision for " + self.coin)

        dc = coin_gecko_api_data_creator.LearningDataCreator('usd')

        time = time_data.get_one_day_interval()

        dc.create_csv_from_data_interval(address=self.address,
                                         coin=self.coin,
                                         time_interval=[self.last_timestamp, time[1]]
                                         )

        self.create_last_hitpoint(data_creator=dc)

    def create_last_hitpoint(self, data_creator):
        file = open(self.address + "/last_timestamp", "w")

        file.write(data_creator.last_used_timestamp)


    def create_new_data_base(self):
        time_chain = TimeChain()

        dc = coin_gecko_api_data_creator.LearningDataCreator('usd')

        dc.create_csv_from_data_interval(address=self.address, coin=self.coin, time_interval=time_chain.past_interval)
        
        print("Creating .csv data for past for " + self.coin)

        dc.create_csv_from_data_interval(address=self.address, coin=self.coin, time_interval=time_chain.ninety_days_interval)
        
        print("Creating .csv data for 90 days with hour precision for " + self.coin)

        dc.create_csv_from_data_interval(address=self.address, coin=self.coin, time_interval=time_chain.one_dat_interval)
        
        print("Creating .csv data for 1 day with 4 minutes precision for " + self.coin)

        self.create_last_hitpoint(data_creator=dc)


