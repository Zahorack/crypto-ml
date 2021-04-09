import time
from datetime import datetime

date_in_history = "01/01/2015"
seconds_in_day = 86400


def oversized_timestamp_to_date(timestamp):
    return datetime.utcfromtimestamp(timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')


def to_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def history_date_as_timestamp():
    return time.mktime(datetime.strptime(date_in_history, "%d/%m/%Y").timetuple())


def get_one_day_interval():
    now = datetime.timestamp(datetime.now())
    return [now - seconds_in_day, now]


class TimeChain:
    one_dat_interval = []
    ninety_days_interval = []
    past_interval = []

    def __init__(self):
        [day_back, now] = get_one_day_interval()

        self.one_dat_interval = [day_back, now]

        ninety_days_back = day_back - 89 * seconds_in_day

        self.ninety_days_interval = [ninety_days_back, day_back]

        self.past_interval = [history_date_as_timestamp(), ninety_days_back]
