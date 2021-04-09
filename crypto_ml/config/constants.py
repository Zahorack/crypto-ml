from singleton_decorator import singleton

from crypto_ml.config import loader


@singleton
class Constants:
    def __init__(self):
        """
        Place for all global constants.

        Tip: Secret credentials, developer custom settings should be stored in config.json
        """

        # ------------- Project settings ------------
        self.VERSION = loader.get('version')

        # ---------- General constants --------------
        self.SECONDS_IN_DAY = 86400

        self.BATCH_SIZE = loader.get('batch_size')

        # -------- Paths and directories -------------
        self.LOG_DIR = loader.get('log_dir')
        self.DATA_STORAGE_DIR = loader.get('data_storage_dir')

        # --------------- Twitter --------------------
        self.TWITTER_CONSUMER_KEY = loader.get('consumer_key')
        self.TWITTER_CONSUMER_SECRET = loader.get('consumer_secret')
        self.TWITTER_ACCESS_TOKEN = loader.get('access_token')
        self.TWITTER_ACCESS_TOKEN_SECRET = loader.get('access_token_secret')

        # ----------- Crypto constants --------------
        self.DEFAULT_FIAT_CURRENCY = 'usd'

        self.SUPPORTED_COINS = [
            "bitcoin",
            "ethereum",
            "binancecoin",
            "tether",
            "polkadot",
            "cardano",
            "ripple",
            "uniswap",
            "litecoin",
            "chainlink",
            "theta-fuel",
            "theta-token",
            "filecoin",
            "bitcoin-cash",
            "klay-token",
            "drep-new",
            "stellar",
            "dogecoin",
            "tron",
            "bittorrent-2",
            "solana",
            "vechain",
            "eos",
            "aave",
            "monero",
            "cosmos",
            "iota",
            "bitcoin-cash-sv",
            "holotoken",
            "binance-usd",
            "tezos",
            "kusama",
            "avalanche-2",
            "neo",
            "creditcoin-2",
            "algorand",
            "nem",
            "huobi-token",
            "chiliz",
            "dash",
            "decred",
            "maker",
            "chiliz",
            "pancakeswap-token"
        ]
