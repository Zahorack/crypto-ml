from crypto_ml.api.twitter import TwitterApi


for sample in TwitterApi(keyword='bitcoin',
                         max_sample_count=None,
                         request_rate_timeout=15,
                         should_wait_for_requests=True).iterate():
    print(sample)
