from dataclasses import dataclass
from typing import Iterator, Optional
from pycoingecko import CoinGeckoAPI
import logging


from crypto_ml.api import ApiIterator, ApiSample
from crypto_ml import config

LOG = logging.getLogger(__name__)


@dataclass
class CryptoGeckoSample(ApiSample):
    timestamp: str
    price: float
    market: float
    volume: float


class CryptoGeckoApi(ApiIterator):
    """
    Coin gecko API handler used for cryptocurrency historical data downloading
    """
    def __init__(self,
                 coin: str,
                 from_timestamp: str,
                 to_timestamp: str):
        self.coin = coin
        self.from_timestamp = from_timestamp
        self.to_timestamp = to_timestamp

    @property
    def api_type(self) -> str:
        return 'CRYPTOCURRENCY'

    @property
    def api_platform(self) -> str:
        return 'GECKO'

    def iterate(self) -> Iterator[ApiSample]:

        try:
            api = CoinGeckoAPI()

            samples = api.get_coin_market_chart_range_by_id(
                id=self.coin,
                vs_currency=config.constants.DEFAULT_FIAT_CURRENCY,
                from_timestamp=self.from_timestamp,
                to_timestamp=self.to_timestamp
            )

            for (price, market, volume) in zip(samples['prices'], samples['market_caps'], samples['total_volumes']):
                yield CryptoGeckoSample(timestamp=price[0],
                                        price=price[1],
                                        market=market[1],
                                        volume=volume[1])

        except Exception as e:
            LOG.error(f"Error while requesting CoinGeckoApi {e}")


