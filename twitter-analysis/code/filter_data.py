import pandas as pd

# This function is created to filter the full_dataset_clean.tsv.gz
# downloaded from: https://zenodo.org/record/5637848, the size
# of the file is over 3GB and over 15GB when decompressed, thus
# it's not included in this GitHub repository.

def filter_big_dataset():
    print('Starting to filter data from the full dataset...')
    # define chunksize for a single read
    chunksize = 10 ** 6
    # create iterator
    df_iterator = pd.read_csv(
        '../data/full_dataset/full_dataset_clean.tsv',
        delimiter='\t',
        chunksize=chunksize
    )
    # create df with 2021 data only
    df_2021 = pd.DataFrame()
    for chunk in df_iterator:
        valid_chunk = chunk.dropna(subset=['date'])
        valid_chunk = chunk.loc[chunk['date'] >= '2021-01-01']
        if len(valid_chunk) != 0:
            df_2021 = df_2021.append(valid_chunk)
    # save df with 2021 data only
    df_2021.to_csv('../data/full_dataset/2021_cleaned_dataset.tsv', sep='\t', index=False)
    # save df with geo location
    df_2021_geo = df_2021.dropna(subset=['country_place'])
    df_2021_geo.to_csv('../data/full_dataset/2021_cleaned_dataset_geo.tsv', sep='\t', index=False)
    print('Data filtering finished. Files saved to ../data/full_dataset/')

def filter_march_april_data():
    print('Starting to filter data from the 2021 dataset...')
    start_date = '2021-03-15'
    end_date = '2021-04-30'
    df = pd.read_csv('../data/full_dataset/2021_cleaned_dataset.tsv', delimiter='\t')
    df_march_april = df.loc[(df['date'] >= start_date) & (df['date'] <= end_date)]
    df_march_april.to_csv('../data/processed_dataset/2021_march_april_full.tsv', sep='\t', index=False)
    df_march_april_geo = df_march_april.dropna(subset=['country_place'])
    df_march_april_geo.to_csv('../data/processed_dataset/2021_march_april_geo.tsv', sep='\t', index=False)
    print('Data filtering finished. Files saved to ../data/processed_data/')

if __name__ == '__main__':
    filter_march_april_data()
