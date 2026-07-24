
import os,time
from pathlib import Path
import google.generativeai as genai
from dotenv import load_dotenv
from ai.parser import parse_gemini_response
BASE_DIR=Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR/".env")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-flash-latest")
def analyze_resume(resume_text,job_role):
    resume_text=" ".join(resume_text.split()[:1800])
    if len(resume_text)<100:
        raise Exception("No readable text found.")
    prompt=f"Analyze this resume for {job_role}. Return ONLY JSON with keys resume_score, ats_score, strengths, weaknesses, missing_skills, suggestions, interview_questions. Resume:\n{resume_text}"
    last=None
    for i in range(2):
        try:
            r=model.generate_content(prompt,request_options={"timeout":30})
            return parse_gemini_response(r.text)
        except Exception as e:
            last=e
            time.sleep(2)
    raise last
