from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Platform engineering lab available now"}


@app.get("/healthz")
def health_check():
    return {"status": "All Good Bro"}

@app.get("/version")
def get_version():
    return {"app current version": "0.1.0"}