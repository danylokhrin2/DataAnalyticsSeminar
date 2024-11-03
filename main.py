# setx OPENAI_API_KEY ""

from openai import OpenAI
client = OpenAI()


def send_request(text):
    
    prompt = f"Does the following text contain hate speech, especially focusing on sexism? Answer ONLY with 1 for Yes or 0 for No. Nothing else.\n\nText: '{text}'"
    
    completion = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4o-mini",
        # model= "gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return completion.choices[0].message.content


print(send_request("This is a sample text"))