import pandas as pd

if __name__ == '__main__':
    data_path = '../data/processed_dataset/2021_march_april_geo.tsv'
    data_geo_path = '../data/processed_dataset/2021_march_april_geo_coo.csv'
    data_country_path = '../data/processed_dataset/2021_march_april_geo_country.csv'
    geo_path = '../data/countries.csv'

    df_data = pd.read_csv(data_path, sep='\t')
    df_geo = pd.read_csv(geo_path)
    dict_lat = {row['short_name']: row['center_lat'] for index, row in df_geo.iterrows()}
    dict_lng = {row['short_name']: row['center_lng'] for index, row in df_geo.iterrows()}

    df_data['lat'] = df_data['country_place'].map(dict_lat)
    df_data['lng'] = df_data['country_place'].map(dict_lng)
    df_data.to_csv(data_geo_path)

    counts = df_data.groupby(by=['country_place']).count()
    counts['country_place'] = counts.index
    counts.reset_index(drop=True, inplace=True)
    df_country = pd.DataFrame()
    df_country[['country_place', 'pop']] = counts[['country_place', 'tweet_id']]
    df_country['lat'] = df_country['country_place'].map(dict_lat)
    df_country['lng'] = df_country['country_place'].map(dict_lng)
    df_country.dropna(inplace=True)
    df_country = df_country[['lat', 'lng', 'pop']]
    df_country.to_csv(data_country_path, index=False)
