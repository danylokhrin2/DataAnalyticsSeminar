# setx OPENAI_API_KEY ""

from openai import OpenAI

def send_requestGPT(model, text):
    client = OpenAI()
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are an assistant trained to identify if text contains sexist content."},
            {
                "role": "user",
                "content": text
            }
        ]
    )
    return completion.choices[0].message.content