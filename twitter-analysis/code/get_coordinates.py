import json
from pandas.core.indexes import multi
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
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    place_df = pd.read_csv('../data/processed_dataset/2021_march_april_coordinates.tsv', delimiter='\t')
    coordinates = []
    ids = place_df['place_id'].values

    multiplier = 1
    for id in ids:
        coordinates.append(api.geo_id(id).centroid)
        if len(coordinates) >= multiplier * 300:
            coordinates_df = pd.DataFrame.from_dict({'centroid': coordinates})
            coordinates_df.to_csv('../data/processed_dataset/2021_march_april_coordinates.tsv', index=False, sep='\t')
            print('Finished {} entries out of {} entries'.format(multiplier * 300, len(coordinates)))
            multiplier += 1

