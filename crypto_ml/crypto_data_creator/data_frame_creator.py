import pandas as pd


def from_data_creator_get_standard_data_frame(data):
    data_frame = pd.DataFrame(data, columns=["date", "timestamp", "price", "market_cap", "volume"])
    data_frame.sort_values(by="timestamp")

    return data_frame
