from fastapi import FastAPI
import time

app = FastAPI()

def write_log():
    time.sleep(5)
    with open("background.log", "a") as f: f.write("task completed\n")

@app.post("/write-log-sync")
def write():
    write_log()
    return {"status": "written"}
