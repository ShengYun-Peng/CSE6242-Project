import os.path

import matplotlib.pyplot as plt
import pandas as pd
import pycountry

if __name__ == '__main__':
    figure_folder = '../figure'
    top_terms = 20

    for gram in ['terms', 'bigrams', 'trigrams']:
        gram_file = '../data/frequent_words_dataset/frequent_' + gram + '.csv'
        df_gram = pd.read_csv(gram_file)
        df_gram.sort_values(by='counts', ascending=False, inplace=True, ignore_index=True)
        df_gram.iloc[(top_terms - 1)::-1].plot.barh(x='term', y='counts', figsize=(5, 5))
        plt.legend(loc='lower right')
        plt.tight_layout()
        plt.savefig(os.path.join(figure_folder, gram + '.pdf'))
        plt.close()

    countries = {}
    for country in pycountry.countries:
        countries[country.alpha_2] = country.name

    top_countries = 20
    geo_file = '../data/processed_dataset/2021_march_april_geo.tsv'
    df_geo = pd.read_csv(geo_file, sep='\t')
    df_country = df_geo['country_place'].value_counts()
    df_country.index = df_country.index.map(countries)
    df_country[(top_countries - 1)::-1].plot.barh(figsize=(5, 5))
    plt.tight_layout()
    plt.savefig(os.path.join(figure_folder, 'countries.pdf'))
    plt.close()
