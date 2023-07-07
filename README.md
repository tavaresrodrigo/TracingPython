# TracingPython

A FastAPI App that demonstrates distributed tracing with OpenTelemetry and Jaeger.

## Instrumentation with OpenTelemetry

For applications to be observed and be able to send Spans to Jaeger, they must be instrumented. The instrumentation process consist of applying OpenTelemetry API, SDK, and tools for generating and collecting application telemetry data such as metrics, logs, and traces, there are three types of Instrumentation: 

* Automatic instrumentation: 
* Manual instrumentation
* Exporting data

## Automatic Instrumentation with Python

Automatic Instrumentation allows dynamically injection of bytecode to capture telemetry in Python. 

This App was automatically instrumented using the OpenTelemetry Libraries below, see the [requirements.txt](requirements.txt) for all libraries installed:

* **opentelemetry-distro**: Contains the OpenTelemetry API, SDK and tools such as opentelemetry-instrument that we are going to use to enable automatic instrumentation.
* **opentelemetry-exporter-otlp-proto-grpc**: Allows to export data to the OpenTelemetry Collector using the OpenTelemetry Protocol using Protobuf over gRPC

The **opentelemetry-instrument** agent was used so automatic instrumentation can generate telemetry data on our behalf.