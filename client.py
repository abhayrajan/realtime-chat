
#!/usr/bin/env python3
"""
Realtime Chat Client - Step 2: Network Client
Basic TCP client that connects to the chat server
"""

import socket

def main():
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to server
    host = 'localhost'
    port = 7007
    
    print(f"Connecting to {host}:{port}...")
    client_socket.connect((host, port))
    print("Connected to server!")
    
    # Get user input and send message
    user_input = input("Enter a message: ")
    
    # Send message to server
    message = user_input + '\n'  # Add newline for proper formatting
    client_socket.send(message.encode('utf-8'))
    print(f"Sent: {user_input}")
    
    # Receive and display server response
    response = client_socket.recv(1024).decode('utf-8')
    if response:
        print(f"Server echoed: {response.strip()}")
    else:
        print("Server disconnected")
    
    # Close connection
    client_socket.close()
    print("Disconnected from server")

if __name__ == "__main__":
    main()