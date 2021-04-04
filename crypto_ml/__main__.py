from crypto_ml.api.twitter import TwitterApi


for sample in TwitterApi(keyword='bitcoin', max_sample_count=5).iterate():
    print(sample)
