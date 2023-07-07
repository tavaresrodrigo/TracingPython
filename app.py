from fastapi import FastAPI
import random
import time
import socket
import os

ports=[4317, 4318, 5775, 6831, 6832, 5778, 16686, 14250, 14267, 14268, 9411]
host=os.getenv("JAEGER_SERVICE")
app = FastAPI()

print("Checking connection to Jaeger TCP ports")
for port in ports:
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the connection (optional)
        sock.settimeout(5)

        # Connect to the host and port
        sock.connect((host, port))

        # If the connection was successful, print a message
        print("Connected to", host, "on port", port)

    except socket.error as e:
        # If an error occurs, print the error message
        print("Connection error:",port,str(e))

    finally:
        # Close the socket
        sock.close()

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