# setx OPENAI_API_KEY ""
from openai import OpenAI

def send_requestGPT(model, system_prompt, text):
    client = OpenAI()
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )
    return completion.choices[0].message.content