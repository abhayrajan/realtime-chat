# Realtime Chat

A TCP-based multi-user chat server and client implementation, built as part of the [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-realtime-chat/) series.

## Overview

This project demonstrates building a realtime chat system from the ground up, starting with a simple echo server and evolving into a full multi-user chat application. The server uses modern Python asyncio for concurrent client handling, while the client uses threading for responsive user interaction.

## Features

- **Multi-user chat**: Multiple clients can connect and chat simultaneously
- **Real-time messaging**: Messages are broadcast to all connected users instantly
- **Username support**: Users can set custom usernames
- **Concurrent connections**: Server handles many clients efficiently using asyncio
- **Graceful shutdown**: Clean disconnection handling for both server and clients

## Usage

**Start the server:**
```bash
python server.py
```

**Connect clients (multiple terminals):**
```bash
python client.py
```

Each client will prompt for a username. Messages from any user appear on all other connected clients' screens.

## Architecture

- **Server**: Asyncio-based TCP server on port 7007
- **Client**: Threading-based command-line client
- **Protocol**: Simple UTF-8 text messaging over TCP
- **Concurrency**: Server uses coroutines, client uses threads for I/O

## Implementation Approach

This project was developed using **Claude Code** with systematic engineering practices:

- **Requirements-driven development**: Started with detailed requirements analysis
- **Incremental implementation**: Built in small, reviewable chunks (20-30 lines each)
- **Step-by-step progression**: Echo server → Network client → Username support → Multi-user chat
- **Code review focused**: Each chunk designed for easy developer review and approval
- **Systematic refactoring**: Converted from threading to asyncio through planned, small iterations

The implementation demonstrates how AI-assisted development can be effective when combined with proper guardrails, clear requirements, and systematic code review processes.

## Technical Requirements

- Python 3.7+ (asyncio support)
- No external dependencies (standard library only)

See [requirements.md](requirements.md) for detailed functional requirements, [implementation-log.md](implementation-log.md) for complete development history, and [CLAUDE.md](CLAUDE.md) for the development guardrails and constraints used with Claude Code.