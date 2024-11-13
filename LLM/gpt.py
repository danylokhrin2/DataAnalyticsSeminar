# setx OPENAI_API_KEY ""
# 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
from openai import OpenAI

client = OpenAI()

def send_requestGPT(model, system_prompt, text):
    
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )
    return completion.choices[0].message.content