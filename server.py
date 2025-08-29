#!/usr/bin/env python3
"""
Realtime Chat Server - Step 1: Echo Server
Basic TCP server that listens on port 7007
"""

import socket
import asyncio

# Global list to track connected clients
connected_clients = []

async def remove_client(writer, client_address):
    """Safely remove a client from the connected clients list"""
    if writer in connected_clients:
        connected_clients.remove(writer)
        print(f"Removed client {client_address} from connected list")
    
    try:
        writer.close()
        await writer.wait_closed()
    except Exception:
        pass  # Connection may already be closed

async def broadcast_message(message, sender_writer):
    """Broadcast message to all connected clients except sender"""
    if not connected_clients:
        return
    
    # Send to all clients except the sender
    broadcast_tasks = []
    for client_writer in connected_clients.copy():  # Copy to avoid modification during iteration
        if client_writer != sender_writer:
            broadcast_tasks.append(send_to_client(client_writer, message))
    
    # Send to all clients concurrently
    if broadcast_tasks:
        await asyncio.gather(*broadcast_tasks, return_exceptions=True)

async def send_to_client(writer, message):
    """Send message to a specific client with error handling"""
    try:
        writer.write(message.encode('utf-8'))
        await writer.drain()
    except Exception:
        # Client disconnected, remove from list
        if writer in connected_clients:
            connected_clients.remove(writer)
            print(f"Removed disconnected client during broadcast")

async def handle_client(reader, writer, client_address):
    """Handle messages from a single client with asyncio streams"""
    try:
        while True:
            data = await reader.read(1024)
            if not data:
                print(f"Client {client_address} disconnected")
                break
            
            message = data.decode('utf-8')
            print(f"Received from {client_address}: {message.strip()}")
            
            # Broadcast message to all other clients (no echo to sender)
            await broadcast_message(message, writer)
            
    except asyncio.CancelledError:
        print(f"Client {client_address} task cancelled")
    except Exception as e:
        print(f"Client {client_address} error: {e}")
    finally:
        # Remove client using helper function
        await remove_client(writer, client_address)

async def handle_client_connection(reader, writer):
    """Handle new client connection with asyncio streams"""
    client_address = writer.get_extra_info('peername')
    print(f"Connection established with {client_address}")
    
    # Add client to connected clients list
    connected_clients.append(writer)
    
    # TODO: Will be implemented in Chunk C
    await handle_client(reader, writer, client_address)

async def main():
    host = 'localhost'
    port = 7007
    
    # Create asyncio server
    server = await asyncio.start_server(
        handle_client_connection, host, port
    )
    
    print(f"Multi-user server listening on {host}:{port}")
    print("Waiting for client connections...")
    
    try:
        await server.serve_forever()
    finally:
        print("\nShutting down server...")
        # Close all client connections
        if connected_clients:
            print(f"Closing {len(connected_clients)} client connections...")
            for client_writer in connected_clients.copy():
                await remove_client(client_writer, "server shutdown")
        server.close()
        await server.wait_closed()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server shutdown complete.")