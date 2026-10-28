from fastapi import FastAPI

app = FastAPI(title="Fitness Center Information System")


@app.get("/")
def home():
    return {"message": "Fitness Center API"}
