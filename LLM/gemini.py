import google.generativeai as genai
import re
from google.generativeai.types import HarmCategory, HarmBlockThreshold

def send_requestGemini(model, text):
    genai.configure(api_key="AIzaSyCFoO5Dv5nQ9JRM-Q3AaEYRvsVoGB3ArHo")

    model = genai.GenerativeModel(model)
    response = model.generate_content(text, safety_settings={HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                                                            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE})
    return re.sub(r'[^0-9]', '', response.text)


#print(send_requestGemini("gemini-1.5-flash", "Does the following text contain hate speech, especially focusing on sexism? Answer ONLY with 1 for Yes or 0 for No. Nothing else.\n\nText: I love you"))