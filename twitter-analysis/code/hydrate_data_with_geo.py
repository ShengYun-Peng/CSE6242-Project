import json
import tweepy
import math
import pandas as pd

if __name__ == '__main__':
    # twitter api credentials
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    BEARER_TOKEN = ''
    ACCESS_TOKEN = ''
    ACCESS_SECRET = ''

    # read credentials from api_keys.json
    with open('api_keys.json', 'r') as f:
        data = json.load(f)
        CONSUMER_KEY = data['consumer_key']
        CONSUMER_SECRET = data['consumer_secret']
        BEARER_TOKEN = data['bearer_token']
        ACCESS_TOKEN = data['access_token']
        ACCESS_SECRET = data['access_secret']

    # set up auth and api client
    auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    client = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        consumer_key=CONSUMER_KEY,
        consumer_secret=CONSUMER_SECRET,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_SECRET,
        wait_on_rate_limit=True
    )

    tweet_id = "1371249868715347968"
    tweet = client.get_tweet(
        id=tweet_id,
        place_fields=['geo'],
        tweet_fields=['geo'],
    )

    print(tweet.data)

    # # read the file to be hydrated
    # geo_df = pd.read_csv('../data/full_dataset/2021_cleaned_dataset_geo.tsv', delimiter='\t')
    # geo_df['geo'] = None
    # N = len(geo_df)
    # print('Current data has {} entries.'.format(N))

    # # batch query to twitter api
    # batch_size = 100
    # batches = int(math.ceil(N / batch_size))

    # valid_ids = []
    # valid_contents = []

    # print('Hydrating...')
    # for i in range(batches):
    #     if (i + 1) * batch_size <= N:
    #         tweet_ids = geo_df['tweet_id'].values[i * batch_size: (i + 1) * batch_size]
    #     else:
    #         tweet_ids = geo_df['tweet_id'].values[i * batch_size:]

    #     # construct twitter api parameter
    #     query = ''
    #     for id in tweet_ids:
    #         query += str(id)
    #         query += ','
    #     query = query[0: -1]

    #     tweets = client.get_tweets(
    #         ids=query,
    #         places_fields).data

    #     for tweet in tweets:
    #         if tweet is not None:
    #             valid_ids.append(tweet.id)
    #             valid_contents.append(tweet.text.replace('\n', '\\n'))
    #     print('Progress: {:.4%}'.format((i + 1) / (batches)))

    # # clean up and output
    # hydrated_df = geo_df[geo_df['tweet_id'].isin(valid_ids)]
    # hydrated_df.loc[:, 'text'] = valid_contents
    # nan_value = float('NaN')
    # hydrated_df.replace('', nan_value, inplace=True)
    # hydrated_df = hydrated_df.dropna(subset=['text'])
    # hydrated_df.to_csv('../data/processed_dataset/2021_march_april_geo_hydrated.tsv', index=False, sep='\t')
    # print('Finished hydrating')