# Realtime Chat Challenge Requirements

Based on: https://codingchallenges.fyi/challenges/challenge-realtime-chat/

## Overview

Build your own realtime chat server and client that allows multiple users to communicate in real-time over a network connection.

## Technical Specifications

- **Protocol**: TCP/IP networking
- **Port**: Server must listen on port 7007
- **Language**: Python implementation
- **Architecture**: Separate server and client applications
- **Concurrency**: Support multiple simultaneous client connections

## Step-by-Step Implementation

### Step 1: Echo Server
Create a simple TCP server that echoes messages back to clients.

**Requirements:**
- Listen on port 7007
- Accept client connections
- Echo received messages back to the sender
- Handle connection and disconnection properly

**Testing:**
- Use telnet to connect: `telnet localhost 7007`
- Send messages and verify they are echoed back
- Test connection termination

**Acceptance Criteria:**
- Server starts and listens on port 7007
- Accepts incoming connections
- Echoes messages back to connected client
- Handles client disconnection gracefully

### Step 2: Network Client
Build a dedicated client application that connects to the chat server.

**Requirements:**
- Connect to server on localhost:7007
- Send user input to server
- Display server responses
- Handle "quit" and "exit" commands to disconnect cleanly
- Provide clear user interface for message input

**Testing:**
- Run client and connect to echo server from Step 1
- Send various messages and verify responses
- Test quit/exit functionality

**Acceptance Criteria:**
- Client successfully connects to server
- User can type messages and see server responses
- Clean disconnection with quit/exit commands
- Clear indication of connection status

### Step 3: Chat Client with Username
Enhance the client to support usernames and concurrent message handling.

**Requirements:**
- Prompt user for username on connection
- Prefix sent messages with username
- Handle simultaneous input and message reception
- Use `select()` or threading for concurrent I/O operations
- Display incoming messages while user is typing

**Testing:**
- Connect client to echo server
- Verify username is prefixed to messages
- Test concurrent input/output handling

**Acceptance Criteria:**
- User provides username when connecting
- Messages are prefixed with username
- User can receive messages while typing
- No blocking between input and message display

### Step 4: Multi-User Chat Server
Transform the echo server into a multi-user chat server with message broadcasting.

**Requirements:**
- Accept multiple concurrent client connections
- Use threading or asyncio for handling multiple clients
- Broadcast messages from one client to all other connected clients
- Do not echo messages back to the sender
- Maintain list of connected clients
- Handle client disconnections without affecting other users
- Implement basic chatroom functionality

**Testing:**
- Start server and connect multiple clients
- Send messages from different clients
- Verify messages are broadcast to all other clients
- Test client disconnection scenarios

**Acceptance Criteria:**
- Server handles multiple simultaneous connections
- Messages from one client appear on all other clients
- Sender does not receive their own message back
- Client disconnections don't crash server or affect other users
- All connected clients can participate in the chat

### Step 5: Enhanced Features (Optional)
Add advanced features to improve the chat experience.

**Possible Enhancements:**
- Join/leave notifications for users
- User list command
- Improved message formatting with timestamps
- Better error handling and connection recovery
- Private messaging capabilities
- Chat commands (e.g., /users, /help, /quit)
- IRC-style features

## Technical Requirements

### Server Requirements
- Must use TCP sockets (not WebSockets or HTTP)
- Listen on port 7007
- Handle multiple concurrent connections
- Broadcast messages to all connected clients
- Graceful handling of client connections and disconnections
- Use Python standard library (socket, threading/asyncio)

### Client Requirements
- Connect to server via TCP on port 7007
- Send user input to server
- Display received messages
- Handle username registration
- Support concurrent input/output operations
- Clean disconnection handling

### Network Protocol
- Simple text-based protocol
- Messages sent as plain text over TCP
- No complex message formatting required initially
- Handle message boundaries properly

## Success Criteria

The challenge is complete when:

1. **Step 1**: Echo server works with telnet client
2. **Step 2**: Custom client can connect and communicate with echo server
3. **Step 3**: Client supports usernames and concurrent I/O
4. **Step 4**: Multiple clients can chat together through the server
5. **Testing**: System works reliably with multiple concurrent users

## Testing Strategy

- Use telnet for initial server testing
- Test with multiple client instances
- Verify message broadcasting works correctly
- Test connection and disconnection scenarios
- Ensure server remains stable under various conditions

## Constraints

- Use Python standard library where possible
- Keep the implementation simple and focused
- Prioritize functionality over advanced features
- Ensure cross-platform compatibility
- No external databases required (in-memory storage is sufficient)