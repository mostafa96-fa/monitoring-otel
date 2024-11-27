import requests
import time
from datetime import datetime


def check_server():
    try:
        response = requests.get("http://localhost:8000/bad", timeout=2)
        if response.status_code == 200:
            print(response.status_code)
            print(f"{datetime.now()} [OK] Server is up")
        elif response.status_code == 502:
            print(f"{datetime.now()} [ERROR] Bad Gateway")
        else:
            print(f"{datetime.now()} [ERROR] Unexpected response")
    except requests.exceptions.RequestException as e:
        print(f"{datetime.now()} [ERROR] Server is down: {e}")

if __name__ == "__main__":
    print("Starting server monitoring...")
    while True:
        check_server()
        time.sleep(1)
