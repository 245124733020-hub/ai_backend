from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai_api_key = "YOUR_API_KEY_HERE"
client = OpenAI(api_key=openai_api_key)

@app.get("/")
def home():
    return {"message": "AI Backend Running Successfully"}

@app.get("/ask")
def ask_ai(question: str):
    prompt = f"Give a clear, detailed, and easy-to-understand answer to: {question}"

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Give simple and clear answers for students."},
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message["content"].strip()

    return {"answer": answer}
