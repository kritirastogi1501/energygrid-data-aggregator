import time
import json
from api import send_batch


def generate_serials():

    serials = []

    for i in range(500):
        serials.append(f"SN-{i:03d}")

    return serials


def create_batches(serials, size=10):

    batches = []

    for i in range(0, len(serials), size):
        batches.append(serials[i:i + size])

    return batches


def main():

    print("⚡ EnergyGrid Client Started")

    serials = generate_serials()
    print(f"Generated {len(serials)} serial numbers")

    batches = create_batches(serials)
    print(f"Created {len(batches)} batches")

    all_results = []

    for i, batch in enumerate(batches):

        print(f"📡 Sending batch {i+1}/{len(batches)}")

        result = send_batch(batch)

        if result and "data" in result:
            all_results.extend(result["data"])

        time.sleep(1)

    with open("output.json", "w") as f:
        json.dump(all_results, f, indent=4)

    print("✅ Completed!")
    print(f"Saved {len(all_results)} records to output.json")


if __name__ == "__main__":
    main()
