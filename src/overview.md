# Overview

**Tenx** is a sharp command-line tool for AI-assisted coding.


```bash
cargo install tenx
```


## Features

- AI-assisted code editing and generation.
- Session-based workflow for organized development.
- Preflight checks to ensure the project is consistent before prompting.
- Post-patch checks with automated model feedback and retry on failure.
- Undo, retry and re-edit steps in the session.
- Model agnostic - swap models on the fly, mid-conversation.
- Built-in support for models from OpenAI, Anthropic, DeepInfra, DeepSeek, xAI,
  Google and Groq, and local models through tools like Ollama.
- Built on **libtenx**, a Rust library for building AI-assisted coding tools.


## Ethos

- Built with an uncompromising focus on expert developers.
- Rigorous benchmarks to track the performance of our system prompt and
  interaction protocol against all current models.
- Stay flexible and refuse to commit deeply to any one model or API.
- Supports all practically useful models.

