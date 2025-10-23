import requests
import time

SENSOR_API = "http://sensor_service:5000/data"  # This will work inside docker-compose
CHECK_INTERVAL = 5  # seconds

def check_sensor_data():
    try:
        response = requests.get(SENSOR_API)
        data = response.json()
        alerts = []

        if data["temperature"] > 70:
            alerts.append(f"High temperature alert: {data['temperature']}")
        if data["gas_leak_detected"]:
            alerts.append("Gas leak detected!")

        if alerts:
            print(f"ALERTS at {data['timestamp']}:")
            for alert in alerts:
                print(f"- {alert}")
        else:
            print(f"{data['timestamp']}: All normal")
    except Exception as e:
        print(f"Error fetching sensor data: {e}")

if __name__ == "__main__":
    while True:
        check_sensor_data()
        time.sleep(CHECK_INTERVAL)
