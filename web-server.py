from flask import Flask
import opentelemetry
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
import os

resource = Resource(attributes={
    SERVICE_NAME: "web-app"
})
provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

# Sets the global default tracer provider
trace.set_tracer_provider(provider)

# Creates a tracer from the global tracer provider
tracer = trace.get_tracer("server.trace")


app = Flask(__name__)


@app.route('/')
@tracer.start_as_current_span("healthy_server")
def hello_geek():
    return "<h1>Hello World!</h1>", 200


@app.route('/bad')
@tracer.start_as_current_span("Badgateway_server")
def stimulate_502():
    return "<h1>Bad Gateway</h1>", 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
    