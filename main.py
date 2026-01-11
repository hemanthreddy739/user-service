from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "user-service up"}

@app.get("/users/{id}")
def get_user(id: int):
    return {"id": id, "name": "Demo User"}
