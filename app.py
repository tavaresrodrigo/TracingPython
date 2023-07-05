from flask import Flask, jsonify, request
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# Create Flask application
app = Flask(__name__)

# Initialize OpenTelemetry components
trace.set_tracer_provider(TracerProvider())
jaeger_exporter = JaegerExporter(service_name="backend-python")
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Instrument Flask application
FlaskInstrumentor().instrument_app(app)

# Define routes
@app.route('/')
def hello():
    return jsonify({'message': 'Hello, World!'})

@app.route('/data', methods=['POST'])
def process_data():
    data = request.get_json()
    # Process the data
    return jsonify({'message': 'Data processed successfully'})
