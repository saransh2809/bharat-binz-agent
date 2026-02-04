from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "agent-core alive"}

@app.post("/analyze")
def analyze(data: dict):
    text = data.get("text", "")
    return {
        "summary": f"Received: {text}",
        "requires_confirmation": True,
        "action_id": "demo_123"
    }
