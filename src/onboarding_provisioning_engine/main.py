from fastapi import FastAPI

app = FastAPI(title="Automated Onboarding & Environment Provisioning Engine")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
