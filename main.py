from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI
from pipeline import run_pipeline

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/research")
async def research(topic: str):
    result = run_pipeline(topic)

    return {
        "topic": topic,
        "result": str(result)
    }