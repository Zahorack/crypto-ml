import click
import logging
import os

from crypto_ml.api.social.twitter import TwitterApi
from crypto_ml.api.cryptocurrency.coin_gecko import CryptoGeckoApi
from crypto_ml import config

from logging.handlers import RotatingFileHandler

LOG = logging.getLogger(__name__)


@click.group()
def cli():
    if __name__ == '__main__':
        logging.basicConfig(level=0)
        log_dir = config.get('log_dir')

        if not os.path.isabs(log_dir):
            log_dir = os.path.join(os.path.dirname(__file__), log_dir)

        handler = RotatingFileHandler(os.path.join(log_dir, 'main.log'),
                                      maxBytes=10000000,
                                      backupCount=50)
        formatter = logging.Formatter(
            '%(asctime)-23s %(process)-6d %(threadName)-16s %(name)-24s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logging.getLogger('').handlers[0].setFormatter(formatter)
        logging.getLogger('').addHandler(handler)

        # Set optional loggers to WARNING level
        logging.getLogger('tweepy').setLevel(logging.WARN)
        logging.getLogger('requests').setLevel(logging.WARN)
        logging.getLogger('requests_oauthlib').setLevel(logging.WARN)
        logging.getLogger('oauthlib').setLevel(logging.WARN)
        logging.getLogger('urllib3').setLevel(logging.WARN)

        LOG.debug("Crypto-ML application begin.")


@cli.command()
@click.argument('keyword', required=True)
@click.option('--max-sample-count', '-m', type=int, required=True)
def create_twitter_dataset(keyword, **kwargs):
    try:
        for sample in TwitterApi(keyword=keyword,
                                 max_sample_count=kwargs['max_sample_count'],
                                 request_rate_timeout=15,
                                 should_wait_for_requests=True).iterate():
            print(sample)

    except Exception as e:
        LOG.error(f'Cannot create twitter dataset {e}')
        return


@cli.command()
@click.option('--coin', '-c', type=str, required=True)
@click.option('--from-timestamp', '-f', type=int, required=True)
@click.option('--to-timestamp', '-t', type=int, required=True)
def create_crypto_dataset(**kwargs):
    try:
        for sample in CryptoGeckoApi(coin=kwargs['coin'],
                                     from_timestamp=kwargs['from_timestamp'],
                                     to_timestamp=kwargs['to_timestamp']).iterate():
            print(sample)

    except Exception as e:
        LOG.error(f'Cannot create twitter dataset {e}')
        return


if __name__ == '__main__':
    cli()
