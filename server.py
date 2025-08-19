#!/usr/bin/env python3
"""
Realtime Chat Server - Step 1: Echo Server
Basic TCP server that listens on port 7007
"""

import socket
import threading

def handle_client(client_socket, client_address):
    """Handle messages from a single client in separate thread"""
    print(f"Connection established with {client_address}")
    
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"Client {client_address} disconnected")
                break
            print(f"Received from {client_address}: {message.strip()}")
            client_socket.send(message.encode('utf-8'))
    except ConnectionResetError:
        print(f"Client {client_address} connection reset")
    finally:
        client_socket.close()

def main():
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow socket reuse to avoid "Address already in use" errors
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind to localhost on port 7007
    host = 'localhost'
    port = 7007
    server_socket.bind((host, port))
    
    # Start listening for connections (allow multiple)
    server_socket.listen(1)
    print(f"Multi-user server listening on {host}:{port}")
    print("Waiting for client connections...")
    
    try:
        while True:
            # Accept client connections in loop
            client_socket, client_address = server_socket.accept()
            
            # Create thread for each client
            client_thread = threading.Thread(
                target=handle_client, 
                args=(client_socket, client_address)
            )
            # client_thread.daemon = True
            client_thread.start()
            
    except KeyboardInterrupt:
        print("\nShutting down server...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()