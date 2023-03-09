import hmac
import json
import time
from hashlib import sha256

from fastapi import FastAPI, HTTPException, Request, status

app = FastAPI()

SECRET = "YOUR_WEBHOOK_SECRET"  # (1)!


@app.post("/webhook-endpoint")
async def webhook_endpoint(request: Request):
    timestamp = request.headers.get("X-Fief-Webhook-Timestamp")
    signature = request.headers.get("X-Fief-Webhook-Signature")
    payload = (await request.body()).decode("utf-8")  # (2)!

    # Check if timestamp and signature are there
    if timestamp is None or signature is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    # Check if timestamp is not older than 5 minutes
    if int(time.time()) - int(timestamp) > 5 * 60:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    # Compute signature
    message = f"{timestamp}.{payload}"
    hash = hmac.new(
        SECRET.encode("utf-8"),
        msg=message.encode("utf-8"),
        digestmod=sha256,
    )
    computed_signature = hash.hexdigest()

    # Check if the signatures match
    if not hmac.compare_digest(signature, computed_signature):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    # Good to go!
    data = json.loads(payload)
    print(data)
