import pandas as pd

from LLM.gpt import send_requestGPT
from LLM.gemini import send_requestGemini


def test():
    df = pd.read_csv("./data/preprocessed/MLMA-hate-speech/en_dataset_TEST.csv")
    #df['gpt-4o-mini'] = df['text'].apply(lambda x: send_requestGPT("gpt-4o-mini", x))
    df.loc[:9, 'gpt-4o-mini'] = df.loc[:9, 'text'].apply(lambda x: send_requestGPT("gpt-4o-mini", x))
    df.to_csv("./data/result/MLMA-hate-speech/en_dataset_TEST_gpt_4o_mini.csv", index=False)

def unique_values_MASTER():
    df = pd.read_csv("./data/preprocessed/MASTER.csv")
    unique_text_count = df['text'].nunique()
    print(f"Number of unique values in 'text' column: {unique_text_count}")

def fill_MASTER():
    df = pd.read_csv("./data/result/MASTER.csv")
    
    system_prompt = "You are an assistant trained to identify if text contains sexism. Answer ONLY with '1' for Yes or '0' for No."
    
    #df.loc[:9, 'gpt-4o'] = df.loc[:9, 'text'].apply(lambda x: send_requestGPT("gpt-4o", x))
    
    df.loc[5:10, 'gpt-4o-mini'] = df.loc[5:10, 'text'].apply(lambda x: send_requestGPT("gpt-4o-mini", system_prompt, x))
    #df.loc[:5, 'gpt-4-0125-preview'] = df.loc[:5, 'text'].apply(lambda x: send_requestGPT("gpt-4-0125-preview", system_prompt, x))
    #df.loc[:5, 'gpt-3.5-turbo-0125'] = df.loc[:5, 'text'].apply(lambda x: send_requestGPT("gpt-3.5-turbo-0125", system_prompt, x))
    
    #df.loc[:5, 'gemini-1.5-flash'] = df.loc[:5, 'text'].apply(lambda x: send_requestGemini("gemini-1.5-flash", system_prompt, x))
    
    
        
    df.to_csv("./data/result/MASTER.csv", index=False)
    
#fill_MASTER()


def MASTER_to_Integer():
    df = pd.read_csv("./data/result/MASTER.csv")
    
    print(df)
    
    
    #df.to_csv("./data/result/MASTER.csv", index=False)
    
MASTER_to_Integer()


