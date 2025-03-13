# client.py
import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"  # Server URL
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello, Server!")
        print("Message sent to server")

        response = await websocket.recv()  # Wait for the response from the server
        print(f"Received from server: {response}")

if __name__ == "__main__":
    asyncio.run(hello())