
import hashlib,json,os
from utils.pdf_reader import extract_pdf_text
from ai.gemini import analyze_resume
CACHE_DIR="cache"
os.makedirs(CACHE_DIR,exist_ok=True)
def analyze_uploaded_resume(uploaded_file,job_role):
    txt=extract_pdf_text(uploaded_file)
    key=hashlib.md5((txt+job_role).encode()).hexdigest()
    fp=os.path.join(CACHE_DIR,key+".json")
    if os.path.exists(fp):
        with open(fp) as f:return json.load(f)
    res=analyze_resume(txt,job_role)
    with open(fp,"w") as f: json.dump(res,f)
    return res
