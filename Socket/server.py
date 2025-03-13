# server.py
import asyncio
import websockets

async def echo(websocket):
    print(f"New connection: {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            await websocket.send(f"Echo: {message}")  # Echo the message back to the client
    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")

async def main():
    async with websockets.serve(echo, "localhost", 8765):
        print("Server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())