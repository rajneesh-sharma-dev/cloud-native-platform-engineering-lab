from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Platform engineering lab"}


@app.get("/healthz")
def health_check():
    return {"status": "ok"}

@app.get("/version")
def get_version():
    return {"version": "0.1.0"}