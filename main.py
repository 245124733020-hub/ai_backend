from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key="AIzaSyC9X7kDzrwAXgdsV5-IIAR-ve7o3qhlQ1k")   # Replace

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.get("/ask")
def ask(question: str):
    prompt = f"Give a clear, simple explanation for: {question}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content
        return {"answer": answer}

    except Exception as e:
        return {"error": str(e)}




