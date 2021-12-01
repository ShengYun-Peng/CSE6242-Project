import pandas as pd

if __name__ == '__main__':
    file_coo = '../data/processed_dataset/2021_march_april_coordinates.tsv'
    file_processed_coo = '../data/processed_dataset/2021_march_april_processed_coordinates.tsv'
    df_coo = pd.read_csv(file_coo, sep='\t')
    df_coo['lat'] = df_coo['centroid'].apply(lambda coo: coo[1:-1].split(',')[1])
    df_coo['lng'] = df_coo['centroid'].apply(lambda coo: coo[1:-1].split(',')[0])
    df_coo['pop'] = 1
    df_coo.drop(columns=['centroid'], inplace=True)
    df_coo.to_csv(file_processed_coo, index=False)
