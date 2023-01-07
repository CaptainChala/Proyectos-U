from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "tu mama es mi mama "}