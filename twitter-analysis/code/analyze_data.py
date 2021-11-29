import os.path

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import pycountry
from langcodes import Language

if __name__ == '__main__':
    plt.rcParams['font.family'] = 'Times New Roman'
    figure_folder = '../figure'
    top_terms = 10
    figure_size = (3.5, 3)

    for gram in ['term', 'bigram', 'trigram']:
        gram_file = '../data/frequent_words_dataset/frequent_' + gram + 's.csv'
        df_gram = pd.read_csv(gram_file)
        df_gram.sort_values(by='counts', ascending=False, inplace=True, ignore_index=True)
        df_gram.iloc[(top_terms - 1)::-1].plot.barh(x='term', y='counts', figsize=figure_size, legend=False)
        # plt.xlabel('Count')
        plt.ylabel('')
        plt.tight_layout()
        plt.savefig(os.path.join(figure_folder, gram + 's.pdf'))
        plt.close()

    countries = {}
    for country in pycountry.countries:
        if 'Venezuela' in country.name:
            countries[country.alpha_2] = 'Venezuela'
        else:
            countries[country.alpha_2] = country.name

    geo_file = '../data/processed_dataset/2021_march_april_geo.tsv'
    df_geo = pd.read_csv(geo_file, sep='\t')

    top_countries = 10
    df_country = df_geo['country_place'].value_counts(normalize=True)
    df_country.index = df_country.index.map(countries)
    ax_country = df_country[(top_countries - 1)::-1].plot.barh(figsize=figure_size)
    ax_country.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    # plt.xlabel('Percentage')
    # plt.ylabel('Country')
    plt.tight_layout()
    plt.savefig(os.path.join(figure_folder, 'countries.pdf'))
    plt.close()

    top_languages = 10
    df_lang = df_geo['lang'].value_counts(normalize=True)
    df_lang.drop('und', inplace=True)
    df_lang.index = df_lang.index.map(lambda code: Language.get(code).display_name())
    ax_lang = df_lang[(top_languages - 1)::-1].plot.barh(figsize=figure_size)
    ax_lang.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1))
    # plt.xlabel('Percentage')
    # plt.ylabel('Language')
    plt.tight_layout()
    plt.savefig(os.path.join(figure_folder, 'languages.pdf'))
    plt.close()
