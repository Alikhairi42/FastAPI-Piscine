from fastapi import FastAPI , HTTPException , Depends , Header
app = FastAPI()

calls: int = 0

def verify_api_key(
    api_key: str | None = None,
    x_api_key: str | None = Header(default=None)
):
    if api_key != "piscine-key" and x_api_key != "piscine-key":
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key"
        )

@app.get('/reports')
def report(key = Depends(verify_api_key)):
    global calls
    calls += 1
    return {"resource": "reports"}

@app.get('/audit')
def audit(key = Depends(verify_api_key)):
    global calls
    calls += 1
    return {"resource": "audit"}

@app.get('/admin')
def admin(key = Depends(verify_api_key)):
    global calls
    calls += 1
    return {"resource": "admin"}

@app.get('/metrics')
def get_calls():
    return {"calls":calls}