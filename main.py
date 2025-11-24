from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI()
client = OpenAI(api_key="AIzaSyC9X7kDzrwAXgdsV5-IIAR-ve7o3qhlQ1k")

class Question(BaseModel):
    question: str

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
        response = client.chat.completions.create(
            model="gemini-3-pro-preview",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content
        return {"answer": answer}

    except Exception as e:
        return {"error": str(e)}
