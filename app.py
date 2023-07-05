from flask import Flask, jsonify, request
from opentelemetry.instrumentation.flask import FlaskInstrumentor
import random
import time

# Create Flask application
app = Flask(__name__)

# Instrument Flask application
FlaskInstrumentor().instrument_app(app)

# Define routes
@app.route('/')
def hello():
    processing_time = random.randint(1, 3)
    time.sleep(processing_time)
    return jsonify({'message': 'Hello, World!', 'Processing time in seconds': processing_time})

@app.route('/data', methods=['POST'])
def process_data():
    data = request.get_json()
    #sleeping random time to simulate processing time
    processing_time = random.randint(1, 3)
    time.sleep(processing_time)
    # Process the data
    return jsonify({'message': 'Data processed successfully', 'data': data, 'Processing time in seconds': processing_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)