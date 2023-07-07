from fastapi import FastAPI
import random
import time

app = FastAPI()

@app.get("/")
def read_root():
    processing_time = random.randint(1, 3)
    time.sleep(processing_time)
    return {
        "Method": "/",
        "Processing time": processing_time}


@app.post("/send")
def send():
    processing_time = random.randint(1, 3)
    time.sleep(processing_time)
    return {
        "Method": "/send",
        "Processing time": processing_time}