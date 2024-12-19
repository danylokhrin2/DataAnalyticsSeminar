import pandas as pd
import csv

# MLMA-hate-speech dateset
def mlma_preprocess():
    files = ["MLMA-hate-speech/en_dataset.csv", "MLMA-hate-speech/ar_dataset.csv", "MLMA-hate-speech/fr_dataset.csv", "MLMA-hate-speech/en_dataset_with_stop_words.csv"]
    for file in files:
        df = pd.read_csv("./data/raw/" + file)
        df['SEXISM'] = df['target'].apply(lambda x: 1 if x == 'gender' else 0)
        df = df.rename(columns={"tweet": "text"})
        df = df[['text', 'SEXISM']]
        df.to_csv("./data/preprocessed/" + file, index=False)
        df['gpt-4o-mini'] = None
        df = df[['text', 'SEXISM', 'gpt-4o-mini']]              

# Ethos dataset
def ethos_preprocess():
    df = pd.read_csv("./data/raw/ethos/Ethos_Dataset_Multi_Label.csv", delimiter=";")
    df['SEXISM'] = df['gender'].round()
    df = df.rename(columns={"comment": "text"})
    df = df[['text', 'SEXISM']]
    df.to_csv("./data/preprocessed/ethos/Ethos_Dataset_Multi_Label.csv", index=False)
    
# TOXIGEN does not work since it only has 20 unique entries
def text_to_csv():
    # Read the entire text file
    with open("./data/raw/toxigen/hate_women_1k.txt", 'r', encoding='utf-8') as file:
        text = file.read()
        
    text = text.replace("\\n", "")
    text = text.replace("\"", "")
    entries = text.split("-")

    # Write the entries to a CSV file
    with open("./data/preprocessed/TOXIGEN/hate_women_1k.csv", 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["text", "SEXISM"])
        # Write header if needed, e.g., `writer.writerow(["Entry", "Label"])`
        for entry in entries:
            entry = entry.strip()
            entry = entry.replace("\"", "")
            if entry != "":
                writer.writerow([entry, 1])

    print(f"Data successfully written to")

def combine_csv_files():
    combined_data = []  # List to hold data from each file
    id_counter = 1      # Start ID counter
    
    files = ["./data/preprocessed/ethos/Ethos_Dataset_Multi_Label.csv", "./data/preprocessed/MLMA-hate-speech/en_dataset.csv", "./data/preprocessed/MLMA-hate-speech/en_dataset_with_stop_words.csv"]#, "./data/preprocessed/MLMA-hate-speech/ar_dataset.csv", "./data/preprocessed/MLMA-hate-speech/fr_dataset.csv"]

    # Iterate over all CSV files in the input folder
    for filename in files:
        if filename.endswith(".csv"):
            # Read the CSV file
            df = pd.read_csv(filename)

            # Add the ID and dataset columns
            df['ID'] = range(id_counter, id_counter + len(df))
            df['dataset'] = filename.split("/")[-1].split(".")[0]  # Get filename without extension
            
            # Update the ID counter
            id_counter += len(df)
            
            # Reorder columns to match the desired structure
            df = df[['ID', 'dataset', 'SEXISM', 'text']]
            
            # Append the DataFrame to the list
            combined_data.append(df)

    # Concatenate all DataFrames
    combined_df = pd.concat(combined_data, ignore_index=True)

    # Save to a new CSV file
    combined_df.to_csv("./data/preprocessed/MASTER.csv", index=False)
    print(f"Combined CSV file saved as MASTER.csv")


def add_directness():
    df = pd.read_csv("./data/raw/MLMA-hate-speech/en_dataset.csv")
    df['DIRECTNESS'] = df['directness'].apply(lambda x: 1 if x == 'direct' else 0)
    df = df.rename(columns={"tweet": "text"})
    df = df[['text', 'DIRECTNESS']]
    df.to_csv("./data/preprocessed/MLMA-hate-speech/en_dataset_DIRECTNESS.csv" , index=False)


def combine_directness_and_master():
    df = pd.read_csv("./data/preprocessed/MLMA-hate-speech/en_dataset_DIRECTNESS.csv")
    df2 = pd.read_csv("./data/result/MASTER.csv")
    
    merged_df = pd.merge(df, df2, on="text", how="outer")
    
    
    # reorder the columns text,DIRECTNESS,ID,dataset,SEXISM,gpt-4o-mini,gpt-4-0125-preview,gpt-3.5-turbo-0125,llama3.2-3b,llama3.1-8b,llama3-8b,gemini-1.5-flash
    merged_df = merged_df[['ID', 'dataset', 'SEXISM', 'DIRECTNESS', 'gpt-4o-mini', 'gpt-4-0125-preview', 'gpt-3.5-turbo-0125', 'llama3.2-3b', 'llama3.1-8b', 'llama3-8b', 'gemini-1.5-flash', 'text']]
    
    # Save the result to a new CSV file (optional)
    merged_df.to_csv("./data/result/MASTER_DIRECT.csv", index=False)
    
    
    
    

combine_directness_and_master()