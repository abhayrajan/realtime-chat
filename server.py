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
            
            # Echo message back to sender (will be changed to broadcast in Chunk E)
            writer.write(message.encode('utf-8'))
            await writer.drain()
            
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
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        server.close()
        await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(main())