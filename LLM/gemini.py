import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyCFoO5Dv5nQ9JRM-Q3AaEYRvsVoGB3ArHo")

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a one sentence story about a magic backpack.")
print(response.text)