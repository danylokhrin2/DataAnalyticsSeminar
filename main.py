# setx OPENAI_API_KEY ""
import pandas as pd
from openai import OpenAI



def send_request(text):
    client = OpenAI()
    
    prompt = f"Does the following text contain hate speech, especially focusing on sexism? Answer ONLY with 1 for Yes or 0 for No. Nothing else.\n\nText: '{text}'"
    
    completion = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4o-mini",
        # model= "gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant trained to identify if text contains sexist content."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content


def MLMA_en_response():
    df = pd.read_csv("./preprocessedData/MLMA-hate-speech/en_dataset.csv")
    #df['gpt-4o-mini'] = df['text'].apply(lambda x: len(x)%2)
    df.loc[:9, 'gpt-4o-mini'] = df.loc[:9, 'text'].apply(lambda x: send_request(x))
    df.to_csv("./preprocessedData/MLMA-hate-speech/en_dataset.csv", index=False)
    
#print(send_request("This is a sample text"))
MLMA_en_response()