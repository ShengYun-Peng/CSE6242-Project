import pandas as pd
import pycountry
from langcodes import Language

if __name__ == '__main__':
    file_data = '../data/processed_dataset/2021_march_april_geo.tsv'
    file_coo = '../data/processed_dataset/2021_march_april_coordinates.tsv'
    file_country = '../data/processed_dataset/2021_march_april_countries.csv'
    file_language = '../data/processed_dataset/2021_march_april_languages.csv'
    file_processed_coo = '../data/processed_dataset/2021_march_april_processed_coordinates.tsv'

    # df_coo = pd.read_csv(file_coo, sep='\t')
    # df_coo['lat'] = df_coo['centroid'].apply(lambda coo: coo[1:-1].split(',')[1])
    # df_coo['lng'] = df_coo['centroid'].apply(lambda coo: coo[1:-1].split(',')[0])
    # df_coo['pop'] = 1
    # df_coo.drop(columns=['centroid'], inplace=True)
    # df_coo.to_csv(file_processed_coo, index=False)

    countries = {}
    for country in pycountry.countries:
        if 'Venezuela' in country.name:
            countries[country.alpha_2] = 'Venezuela'
        else:
            countries[country.alpha_2] = country.name

    df_data = pd.read_csv(file_data, sep='\t')

    counts = df_data.groupby(by=['country_place']).count()
    counts['country_place'] = counts.index
    counts.reset_index(drop=True, inplace=True)

    df_country = pd.DataFrame()
    df_country[['country_place', 'pop']] = counts[['country_place', 'tweet_id']]
    df_country.dropna(inplace=True)
    df_country['country_place'] = df_country['country_place'].map(countries)
    df_country.sort_values(by=['pop'], ascending=False, inplace=True)
    df_country.rename(columns={'country_place': 'Country', 'pop': 'Value'}, inplace=True)
    df_country.head(10).to_csv(file_country, index=False)

    counts = df_data.groupby(by=['lang']).count()
    counts.drop('und', inplace=True)
    counts['lang'] = counts.index
    counts.reset_index(drop=True, inplace=True)

    df_lang = pd.DataFrame()
    df_lang[['lang', 'pop']] = counts[['lang', 'tweet_id']]
    df_lang.dropna(inplace=True)
    df_lang['lang'] = df_lang['lang'].map(lambda code: Language.get(code).display_name())
    df_lang.sort_values(by=['pop'], ascending=False, inplace=True)
    df_lang.rename(columns={'lang': 'Language', 'pop': 'Value'}, inplace=True)
    df_lang.head(10).to_csv(file_language, index=False)
