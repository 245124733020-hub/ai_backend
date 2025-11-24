from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

app = FastAPI()

# Configure Gemini API key
genai.configure(api_key="AIzaSyC9X7kDzrwAXgdsV5-IIAR-ve7o3qhlQ1k")

# Input model
class Question(BaseModel):
    question: str

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/ask")
def ask(data: Question):

    prompt = f"Give a clear, simple explanation for: {data.question}"

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)

        return {"answer": response.text}

    except Exception as e:
        return {"error": str(e)}

