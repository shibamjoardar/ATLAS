# ATLAS

A local-first agentic AI assistant built in Python, running entirely on-device via [Ollama](https://ollama.com) + llama3.2 through the OpenAI-compatible SDK.

## Status
- Terminal chatbot with a tool-using agent loop
- Tools: calculator, `remember` / `recall` (persistent long-term memory)
- Conversation history persists across restarts

## Setup
```bash
ollama pull llama3.2
pip install -r requirements.txt
python main.py
```

## Roadmap
- More tools (file I/O, web fetch)
- Planning / multi-step task execution
- Computer control
- Voice interface
- Eventual robotics / IoT integration