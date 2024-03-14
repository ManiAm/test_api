import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")
        await websocket.send(f"Server says: {message}")

# This server will listen for WebSocket connections on ws://localhost:8765
start_server = websockets.serve(echo, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

# Both the server and client examples use asyncio,
# a library to write concurrent code using the async/await syntax.
