from fastapi import FastAPI

app = FastAPI(title="CLECMAS", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "clecmas-api",
        "mode": "repository-initialization",
    }
