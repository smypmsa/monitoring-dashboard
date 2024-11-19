import json
import asyncio
from datetime import datetime, timezone
import sys
import os

import websockets




hostname = os.getenv("HOSTNAME", "default-host")

with open("endpoints.json", "r") as f:
    endpoints = json.load(f)

async def fetch_block_delay(endpoint, websocket_url):
    async with websockets.connect(websocket_url) as websocket:
        await websocket.send(json.dumps({
            "id": 1,
            "jsonrpc": "2.0",
            "method": "eth_subscribe",
            "params": ["newHeads"]
        }))
        subscription_response = await websocket.recv()
        subscription_data = json.loads(subscription_response)
        if subscription_data.get("result") is None:
            sys.stderr.write(f"Failed to subscribe for endpoint: {endpoint}\n")
            return

        while True:
            response = await websocket.recv()
            response_data = json.loads(response)

            if "params" in response_data:
                block = response_data["params"]["result"]
                block_timestamp = int(block.get("timestamp", "0x0"), 16)
                block_time = datetime.fromtimestamp(block_timestamp, timezone.utc)
                current_time = datetime.now(timezone.utc)
                delay = (current_time - block_time).total_seconds()

                sys.stdout.write(f'block_delay_seconds{{endpoint="{endpoint}", host="{hostname}"}} {delay}\n')
                sys.stdout.flush()

async def main():
    tasks = [fetch_block_delay(endpoint, url) for endpoint, url in endpoints.items()]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())