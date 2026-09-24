from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Restockr"}

@app.get("/about")
def about():
    return {"description": "Restockr is a grocery purchase tracking application"}

@app.get("/status")
def status():
    return {"status": "Restockr is Running"}