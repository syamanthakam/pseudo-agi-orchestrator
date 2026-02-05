from fastapi import FastAPI

app = FastAPI(title="Pseudo-AGI Orchestrator API")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/chat")
async def chat_stub(payload: dict):
    """Minimal placeholder endpoint.

    This will eventually:
    - run the agent loop
    - call tools
    - update memory
    For now it just echoes the payload so the API shape is visible.
    """
    return {"echo": payload}
