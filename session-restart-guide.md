# Session Restart Guide

This file contains commands to resume Claude Code sessions for the realtime chat implementation.

## Quick Restart Commands

### Minimal Command
```
Continue implementing the realtime chat project. Check implementation-log.md for current progress.
```

### Detailed Command Template
```
Resume realtime chat implementation. Check implementation-log.md for our progress. 
We just completed [CURRENT_STEP] [CURRENT_CHUNK]. 
Please implement [NEXT_STEP] [NEXT_CHUNK]: [DESCRIPTION].
```

### Example Current Command (as of now)
```
Resume realtime chat implementation. Check implementation-log.md for our progress. 
We just completed Step 2 Chunk 3 (client receives echo). 
Please implement Step 2 Chunk 4: Main Loop with Quit/Exit functionality.
```

## What Claude Code Will Do Automatically

1. **Read project files** to understand current state:
   - `CLAUDE.md` - Implementation guidelines and constraints
   - `requirements.md` - 5-step implementation plan
   - `implementation-log.md` - Detailed progress tracking
   - `server.py` and `client.py` - Current code state

2. **Understand context** from file contents and your brief instruction

3. **Resume implementation** following the small-chunk approach

## Key Files for Context

- **`CLAUDE.md`** - Contains all implementation guardrails and process rules
- **`requirements.md`** - Original challenge requirements and 5-step plan  
- **`implementation-log.md`** - Tracks completed chunks and current progress
- **`session-restart-guide.md`** - This file with restart commands

## Update Instructions

**Before ending a session:**
1. Update `implementation-log.md` with latest progress
2. Update the "Example Current Command" above with next step
3. Ensure all important decisions are documented in project files

**When starting new session:**
1. Use one of the restart commands above
2. Verify Claude reads the progress files correctly
3. Continue with small-chunk implementation approach

## Emergency Recovery

If files are missing or corrupted:
1. Check `git log` for recent commits
2. Use `git diff` to see what changed
3. Restore from backup or start from last known good state
4. Update progress documentation before continuing