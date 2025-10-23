from prometheus_client import start_http_server, Gauge
# Start Prometheus metrics server on port 8000
start_http_server(8000)

# Define metrics
temperature_gauge = Gauge("temperature", "Temperature from sensor")
gas_leak_gauge = Gauge("gas_leak_detected", "Gas leak detected flag")

from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI()

@app.get("/data")
def get_sensor_data():
    data = {
        "temperature": round(random.uniform(20.0, 80.0), 2),
        "pressure": round(random.uniform(900, 1100), 2),
        "humidity": round(random.uniform(20.0, 90.0), 2),
        "gas_leak_detected": random.choice([True, False]),
        "timestamp": datetime.utcnow().isoformat()
    }
    # Update Prometheus metrics
    temperature_gauge.set(data["temperature"])
    gas_leak_gauge.set(1 if data["gas_leak_detected"] else 0)

    return data
