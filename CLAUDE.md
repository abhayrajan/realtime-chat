# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a realtime chat application project based on a coding challenge to build both client and server components. The repository is currently in initial setup phase with only a basic README file present.

## Current State

- Repository contains README.md, requirements.md, and CLAUDE.md files
- Ready for implementation based on requirements.md specifications
- No source code or configuration files exist yet

## Expected Architecture

Given the project description, this will involve:

- A Python chat server using TCP sockets
- A Python chat client (command-line based)
- Real-time communication using TCP/IP networking
- Message persistence (in-memory storage)

## Development Commands

Since this is a Python-based implementation, standard commands will be:

- `python server.py` to start the chat server
- `python client.py` to start the chat client
- `python -m pytest` for running tests once implemented

## Development Guardrails & Constraints

### Code Quality Standards

- Write clean, readable code with meaningful variable and function names
- Keep functions small and focused on single responsibilities
- Add error handling for all network operations and user inputs
- Use consistent code formatting throughout the project

### Architecture Constraints

- Follow the milestone progression defined in requirements.md
- Implement server and client as separate, independent components
- Use TCP sockets for real-time communication (not WebSockets or HTTP)
- Keep dependencies minimal - prefer standard library solutions when possible
- Design for concurrent users from the start (no single-user limitations)

### Implementation Rules

- Always validate user input before processing
- Handle network disconnections gracefully without crashing
- Use in-memory storage only (no external databases)
- Implement proper cleanup when clients disconnect
- Follow the text-based message protocol defined in requirements.md
- Test with multiple concurrent connections before considering milestones complete

### Security Considerations

- Sanitize all user inputs to prevent injection attacks
- Limit message sizes to prevent memory exhaustion
- Implement basic rate limiting to prevent spam
- No sensitive data should be logged or exposed

### Development Process

- **CRITICAL**: Do not implement any code or create any files without explicit developer approval
- **SMALL ITERATIONS**: Implement only small, manageable chunks of code at a time for review
- Always present implementation plans and get confirmation before proceeding
- Break down each step into the smallest possible reviewable pieces
- Wait for developer approval after each small implementation before continuing
- If implementation seems too large, break it down further into smaller pieces
- Complete milestones in order as defined in requirements.md, but in small increments
- Test each small increment thoroughly before moving to the next piece
- Maintain backward compatibility when adding features
- Document any deviations from requirements.md with clear justification
- Update the implementation log after the developer reviews and approves the implementation

### Code Review Guidelines

- Implement maximum 20-30 lines of code at a time
- Focus on single functionality per implementation cycle
- Present clear explanation of what each code chunk does
- Allow developer to review and approve before adding more code
- If developer requests changes, implement them before proceeding
- Never implement multiple functions or large code blocks simultaneously

### Technology Preferences

- Use Python standard library: socket, threading, asyncio, select
- Prefer built-in modules over external dependencies
- Use TCP sockets (socket module) for network communication
- Use threading or asyncio for handling concurrent connections
- Ensure cross-platform compatibility (Windows, macOS, Linux)

## Notes for Implementation

- Refer to requirements.md for detailed functional and non-functional requirements
- Follow milestone progression for structured development approach
- Plan for both client and server components as mentioned in the project description
- Design for real-time bidirectional communication between multiple clients
- Consider message broadcasting, user management, and connection handling
