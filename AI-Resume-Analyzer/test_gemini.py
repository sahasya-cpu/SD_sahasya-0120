import os
from pathlib import Path
from dotenv import load_dotenv
import google.generativeai as genai

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-flash-latest")

response = model.generate_content("Say Hello")

print(response.text)