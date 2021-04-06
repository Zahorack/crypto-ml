from dataclasses import dataclass
from typing import Iterator, Optional
from pycoingecko import CoinGeckoAPI
import logging
import json
import itertools

from crypto_ml.api import ApiHandler, ApiSample

LOG = logging.getLogger(__name__)


@dataclass
class CryptoGeckoSample(ApiSample):
    timestamp: str
    price: float
    market: float
    volume: float


class CryptoGeckoApi(ApiHandler):
    """
    Coin gecko API handler used for cryptocurrency historical data downloading
    """

    def iterate(self) -> Iterator[ApiSample]:

        try:
            api = CoinGeckoAPI()

            timestamp_from = '1605056000'
            timestamp_to = '1605099600'

            samples = api.get_coin_market_chart_range_by_id(
                id='bitcoin',
                vs_currency='usd',
                from_timestamp=timestamp_from,
                to_timestamp=timestamp_to
            )

            for (price, market, volume) in zip(samples['prices'], samples['market_caps'], samples['total_volumes']):
                yield CryptoGeckoSample(timestamp=price[0],
                                        price=price[1],
                                        market=market[1],
                                        volume=volume[1])

        except Exception as e:
            LOG.error(f"Error while requesting CoinGeckoApi {e}")


