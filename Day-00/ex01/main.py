from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def Response():
    return {"status": "operational", "message": "Service in running"}