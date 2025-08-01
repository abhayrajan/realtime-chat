#!/usr/bin/env python3
"""
Realtime Chat Server - Step 1: Echo Server
Basic TCP server that listens on port 7007
"""

import socket

def main():
    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Allow socket reuse to avoid "Address already in use" errors
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # Bind to localhost on port 7007
    host = 'localhost'
    port = 7007
    server_socket.bind((host, port))
    
    # Start listening for connections
    server_socket.listen(1)
    print(f"Echo server listening on {host}:{port}")
    print("Waiting for client connection...")
    
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    
    # TODO: Handle client messages (next chunk)
    
    # Close connections
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()