import hashlib
import time

# Must match server.js
SECRET_TOKEN = "interview_token_123"


def get_timestamp():
    # Server expects milliseconds timestamp as string
    return str(int(time.time() * 1000))


def generate_signature(url, timestamp):
    """
    MD5( url + SECRET_TOKEN + timestamp )
    """

    raw = url + SECRET_TOKEN + timestamp

    md5_hash = hashlib.md5(raw.encode()).hexdigest()

    return md5_hash
