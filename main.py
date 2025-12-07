from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

# Configure Gemini API key
client=OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

    prompt = prompt = f"""
Explain the following term in a simple and clear way suitable for students.
Include:

1. Definition: Simple and clear (1–2 sentences)
2. Explanation: Easy to understand (3-4 sentences)
3. Daily Life Example: One practical example
4. Summary: A short 2-line summary

Term: {data.question}
"""


     try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        answer = response.choices[0].message["content"]
        return {"answer": answer}

    except Exception as e:
        return {"error": str(e)}






