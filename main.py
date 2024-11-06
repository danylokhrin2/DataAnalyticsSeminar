import pandas as pd


from LLM.gpt import send_requestGPT
from LLM.gemini import send_requestGemini

prompt = "Does the following text contain hate speech, especially focusing on sexism? Answer ONLY with 1 for Yes or 0 for No. Nothing else.\n\nText: "

def MLMA_en_response():
    df = pd.read_csv("./data/preprocessed/MLMA-hate-speech/en_dataset.csv")
    df['test'] = df['text'].apply(lambda x: len(x)%2)
    
    #df.loc[:9, 'gpt-4o-mini'] = df.loc[:9, 'text'].apply(lambda x: send_request(x))


    #Gemini
    #df["gemini-1.5-flash"] = df['text'].apply(lambda x: send_requestGemini("gemini-1.5-flash", x))
    df.loc[:9, 'gemini-1.5-flash'] = df.loc[:9, 'text'].apply(lambda x: send_requestGemini("gemini-1.5-flash", prompt + x))

    
    
    df.to_csv("./data/result/MLMA-hate-speech/en_dataset.csv", index=False)



MLMA_en_response()








