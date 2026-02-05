# Pseudo‑AGI Orchestrator (Concept)

This project explores how to build a **"pseudo‑AGI"** system: an agent that *feels* general-purpose and intelligent by coordinating tools, memory, and planning – without claiming to be true AGI.

## High-Level Idea

Instead of one giant model that can do everything, the orchestrator:

1. **Understands the request** using an LLM
2. **Plans a sequence of steps** ("research", "call tools", "summarize")
3. **Calls tools** to actually do work
4. **Writes important facts to memory** so it can recall them later
5. **Returns a final answer or action plan**

Over time this makes the system feel like a single, general agent that can:

- Research topics by combining search + summarization
- Read and modify code in connected repositories
- Keep track of multi-step projects across sessions
- Adapt its behavior to each user based on past interactions

## Components (Planned)

- **Agent core** – the main loop that:
  - Receives user messages
  - Calls the LLM with a system prompt
  - Interprets tool-call requests from the LLM
  - Writes/reads from memory
- **Tool layer** – Python functions wrapped as tools, e.g.:
  - Web search / web fetch
  - GitHub inspection (list repos, files, issues)
  - Local file search / code analysis
  - Simple shell commands in a sandbox
- **Memory layer** – a small database or vector store to store:
  - User preferences
  - Ongoing project notes
  - Summaries of past conversations
- **Planner / router** – prompt-driven logic that asks the LLM to:
  - Break a task into steps
  - Decide which tools to use in which order

## Example Use-Cases

- "Read this GitHub repo and summarize the architecture for me."
- "Set up a small research report about X, including 5 references."
- "Remember my preferences for future conversations (tone, language, topics)."

## Status

Right now this repository documents the **design and intent** for a pseudo‑AGI system. The next steps will be:

1. Implement a minimal agent loop in Python (FastAPI backend)
2. Add 2–3 concrete tools (web fetch, local file search)
3. Add a very simple memory layer (SQLite or JSON+embeddings)
4. Expose a `/chat` HTTP endpoint that runs the orchestrator for a single user

This is meant as a starting point for experimenting with agent architectures, not as a claim of "real AGI".
