import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello Server!")
        response = await websocket.recv()
        print(f"Received from server: {response}")

asyncio.get_event_loop().run_until_complete(hello())
