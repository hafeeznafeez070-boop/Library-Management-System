import pdfplumber
import json, os
from dotenv import load_dotenv
from openai import OpenAI



load_dotenv()


client = OpenAI(
    base_url="",
    api_key= os.environ[""]
)

def extract_pdf_text(file):
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def structured_data(text):
    prompt = f""

    response = client.chat.completions.create(
        model="",
        messages=[{"role":"user","content":prompt}]
    )

    clean_text = response.choices[0].message.content.strip().replace("```json","").replace("```","")
    return json.loads(clean_text)