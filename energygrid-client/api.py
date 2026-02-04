import requests
import time
from utils import get_timestamp, generate_signature

BASE_URL = "http://localhost:3000"
ENDPOINT = "/device/real/query"


def send_batch(batch, retries=3):

    url = BASE_URL + ENDPOINT

    for attempt in range(retries):

        timestamp = get_timestamp()

        signature = generate_signature(ENDPOINT, timestamp)

        headers = {
            "Content-Type": "application/json",
            "timestamp": timestamp,
            "signature": signature,
        }

        payload = {
            "sn_list": batch
        }

        try:
            response = requests.post(
                url,
                json=payload,
                headers=headers,
                timeout=5
            )

            if response.status_code == 200:
                return response.json()

            else:
                print(f"❌ Error: HTTP {response.status_code}. Retrying...")
                time.sleep(1)

        except Exception as e:
            print("❌ Request failed:", e)
            time.sleep(1)

    return None
