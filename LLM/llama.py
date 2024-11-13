from openai import OpenAI
import re

client = OpenAI(
        api_key = "LA-5965848939324f758edd1a618be2a86b195392459c8a4b9e948a057663ae0b2c",
        base_url = "https://api.llama-api.com"
    )

def send_requestLlama(model, system_prompt, text):

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": text}
        ]
    )
    
    return re.sub(r'\D', '', completion.choices[0].message.content)