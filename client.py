
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
    
    # Prompt user for username
    username = input("Enter your username: ")
    print(f"Welcome, {username}!")
    
    # Main chat loop
    try:
        while True:
            # Get user input
            user_input = input()
            
            # Check for quit/exit commands
            if user_input.lower() in ['quit', 'exit']:
                print("Disconnecting...")
                break
            
            # Send message to server with username prefix
            message = f"{username}: {user_input}\n"
            client_socket.send(message.encode('utf-8'))
            
            # Echo locally (client-side display)
            print(f"{username}: {user_input}")
            
            # Receive and display server response
            response = client_socket.recv(1024).decode('utf-8')
            if response:
                print(response.strip())
            else:
                print("Server disconnected")
                break
                
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Error: {e}")
    
    # Close connection
    client_socket.close()
    print("Disconnected from server")

if __name__ == "__main__":
    main()