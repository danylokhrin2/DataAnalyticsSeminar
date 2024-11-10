import google.generativeai as genai
import re
from google.generativeai.types import HarmCategory, HarmBlockThreshold

def send_requestGemini(model, system_promt, text):
    genai.configure(api_key="AIzaSyCFoO5Dv5nQ9JRM-Q3AaEYRvsVoGB3ArHo")
    
    model = genai.GenerativeModel(model)
    response = model.generate_content(system_promt + "\n" + text, safety_settings={
                                                            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                                                            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE})
    return re.sub(r'\D', '', response.text)