import pandas as pd


# MLMA-hate-speech dateset
files = ["MLMA-hate-speech/en_dataset.csv", "MLMA-hate-speech/ar_dataset.csv", "MLMA-hate-speech/fr_dataset.csv", "MLMA-hate-speech/en_dataset_with_stop_words.csv"]
for file in files:
    df = pd.read_csv("./data/" + file)
    df['SEXISM'] = df['target'].apply(lambda x: 1 if x == 'gender' else 0)
    df = df.rename(columns={"tweet": "text"})
    df = df[['text', 'SEXISM']]
    df.to_csv("./preprocessedData/" + file, index=False)
    df['gpt-4o-mini'] = None
    df = df[['text', 'SEXISM', 'gpt-4o-mini']]
    
                 

# Ethos dataset
df = pd.read_csv("./data/ethos/Ethos_Dataset_Multi_Label.csv", delimiter=";")
df['SEXISM'] = df['gender'].round()
df = df.rename(columns={"comment": "text"})
df = df[['text', 'SEXISM']]
df.to_csv("./preprocessedData/ethos/Ethos_Dataset_Multi_Label.csv", index=False)