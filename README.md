New README.md

```md
# EnergyGrid Data Aggregator

This project is a client-server system that fetches and aggregates real-time telemetry data from 500 solar inverters while following strict API constraints such as rate limiting, batching, and security authentication.

It was developed as part of a coding assignment to demonstrate API integration, request throttling, and secure communication.

---

## Project Overview

The EnergyGrid API allows fetching data for a limited number of devices per request and enforces strict rate limits.  
This project implements a Python-based client that communicates with a Node.js mock server and efficiently collects data for all devices.

Key challenges handled in this project:

- Maximum 10 devices per request
- Only 1 request per second allowed
- Custom MD5-based request signature
- Handling failed requests and retries
- Aggregating responses into a final report

---

## Folder Structure

```

energygrid-project/
├── energygrid-client/   # Python client
│   ├── main.py
│   ├── api.py
│   ├── utils.py
│   └── output.json
│
└── mock-api/            # Mock backend server (Node.js)
├── server.js
└── package.json

````

---

## Features

- Generates 500 dummy serial numbers
- Splits them into batches of 10
- Sends secure API requests
- Respects 1 request/second limit
- Automatically retries on failure
- Aggregates all responses
- Saves final output in JSON format

---

## Technologies Used

- Python (requests, hashlib, time)
- Node.js (Express)
- Git & GitHub

---

## How It Works (Approach)

1. Generate 500 serial numbers (SN-000 to SN-499)
2. Divide them into batches of 10
3. For each request:
   - Generate current timestamp
   - Create MD5 signature using:
     URL + Token + Timestamp
   - Attach headers
4. Send request to server
5. Wait 1 second before next request
6. Retry if request fails
7. Collect and store all results

This ensures maximum throughput while respecting API rules.

---

## Setup and Installation

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm

---

### Step 1: Start Mock Server

Open terminal and run:

```bash
cd mock-api
npm install
npm start
````

You should see:

```
⚡ EnergyGrid Mock API running on port 3000
```

---

### Step 2: Run Client

Open a new terminal and run:

```bash
cd energygrid-client
pip install requests
python main.py
```

The client will start sending batched requests.

---

## Output

After completion, all device data is stored in:

```
energygrid-client/output.json
```

This file contains the aggregated results for all 500 devices.

---

## Error Handling

* Handles HTTP 429 (Too Many Requests)
* Handles authentication errors
* Retries failed requests
* Prevents exceeding rate limits

---

## Learning Outcomes

Through this project, I learned:

* Implementing rate-limited API clients
* Secure request signing
* Batch processing
* Error handling and retries
* Client-server architecture
* Professional project structuring

---

## Author

**Kriti Rastogi**

````