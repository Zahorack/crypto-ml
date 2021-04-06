import sys
import arguments
import time
from time_data import TimeChain

from crypto_ml import config
from crypto_ml.config.constants import constants


if __name__ == '__main__':

    args = arguments.Args(sys.argv)

    time_chain = TimeChain()

    supported_coins = config.get('supported_coins')

    if args.use_std_coins:

        if args.data_policy == 'create_new':

            for coin in supported_coins:
                updater = data_updater.DataUpdater(address=args.to_address, coin=coin, used_currency='usd')

                updater.create_new_data_base()

                time.sleep(3)

        if args.data_policy == 'push_to_existing':

            for coin in supported_coins:
                updater = data_updater.DataUpdater(address=args.to_address, coin=coin, used_currency='usd')

                updater.update()

                time.sleep(3)

    else:

        if args.data_policy == 'create_new':

            for coin in args.for_coins:
                updater = data_updater.DataUpdater(address=args.to_address, coin=coin, used_currency='usd')

                updater.create_new_data_base()

                time.sleep(3)

        if args.data_policy == 'push_to_existing':

            for coin in args.for_coins:
                updater = data_updater.DataUpdater(address=args.to_address, coin=coin, used_currency='usd')

                updater.update()

                time.sleep(3)
