using:

example:
    args:
        for_coins=bitcoin { creates database for bitcoin }
        for_coins=bitcoin,ethereum { creates database for bitcoin and eth } // for more supported coins see "supported_coins.py"
        for_coins=supported { creates database for all supported coins [takes some time]

        to_address { address where to create database }

        data_policy=create_new { creates new database }
        data_policy=push_to_existing { pushes to existing data directories }


python3 main.py for_coins=bitcoin to_address=/home/fkafka/Documents/crypto_ml/crypto-ml/crypto_ml/crypto_data_creator/ data_policy=create_new
