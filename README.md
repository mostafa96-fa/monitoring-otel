# Monitoring Setup with OpenTelemetry

This project demonstrates how to set up and monitor a Flask web application using OpenTelemetry, Docker, and Jaeger. This project consists of a Flask web server that exposes health check endpoints and a Requests-Script, which does requests against the web server. The server is instrumented with OpenTelemetry for tracing, and Jaeger is used to visualize the traces. The application is deployed within Docker containers, and Docker Compose is used to orchestrate containers.

# Prerequisites

Before you begin, ensure that you have the following software installed:

1. Python 3  
2. Docker
3. Docker Compose   
   