from fastapi import FastAPI , HTTPException , Depends
app = FastAPI()

calls: int = 0

def verify_api_key(api_key: str | None = None):
    if api_key != "piscine-key":
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

@app.get('/secure')
def secure_endpoint(key = Depends(verify_api_key)):
    global calls
    calls += 1
    return {"access": "granted"}

@app.get('/metrics')
def ali():
    return {"calls": calls}