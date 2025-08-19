
#!/usr/bin/env python3
"""
Realtime Chat Client - Step 2: Network Client
Basic TCP client that connects to the chat server
"""

import socket
import threading

def receive_messages(client_socket):
    """Handle incoming messages from server in background thread"""
    while True:
        try:
            response = client_socket.recv(1024).decode('utf-8')
            if response:
                print(f"\r{response.strip()}\n> ", end="", flush=True)
            else:
                print("\rServer disconnected")
                break
        except:
            break

def main():
    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to server
    host = 'localhost'
    port = 7007
    
    print(f"Connecting to {host}:{port}...")
    client_socket.connect((host, port))
    print("Connected to server!")
    
    # Main chat loop with username prompt
    try:
        # Prompt user for username
        username = input("Enter your username: ")
        print(f"Welcome, {username}!")
        
        # Start background thread for receiving messages
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.daemon = True
        receive_thread.start()
        
        while True:
            # Get user input with prompt
            user_input = input("> ")
            
            # Check for quit/exit commands
            if user_input.lower() in ['quit', 'exit']:
                print("Disconnecting...")
                break
            
            # Send message to server with username prefix
            message = f"{username}: {user_input}\n"
            client_socket.send(message.encode('utf-8'))
                
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Error: {e}")
    
    # Close connection
    client_socket.close()
    print("Disconnected from server")

if __name__ == "__main__":
    main()