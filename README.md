# ollama-sink

A tiny repo with practical Ollama examples: basic streaming, separating thinking vs answer tokens, timing latency, naive tool-trigger detection, and structured output with Pydantic / JSON schema. The repo currently contains Python examples plus a couple of raw `curl` request/response samples. :contentReference[oaicite:0]{index=0}

## What’s in here

- `streaming101.py` — stream a response while separating `thinking` and `content`, and accumulate both for use in a follow-up turn. :contentReference[oaicite:1]{index=1}
- `streaming_next.py` — minimal streaming example that prints tokens as they arrive. :contentReference[oaicite:2]{index=2}
- `streaming_with_latency.py` — measure time to first token and total generation time. :contentReference[oaicite:3]{index=3}
- `streaming_with_tooling.py` — simple streaming loop with naive buffer inspection to detect when a tool should be called. :contentReference[oaicite:4]{index=4}
- `ollama_structure_format.py` — structured output using `Pydantic` models and `format=...model_json_schema()`. :contentReference[oaicite:5]{index=5}
- `curl_request_format.txt` — raw `curl` request showing a JSON-schema-style structured output request. :contentReference[oaicite:6]{index=6}
- `curl_reply_answer.txt` — sample raw response from the previous request. :contentReference[oaicite:7]{index=7}
- `mise.toml` — minimal tool setup for Python. :contentReference[oaicite:8]{index=8}

## Requirements

- [Ollama](https://ollama.com/) running locally
- Python 3
- The `ollama` Python package
- `pydantic`

This repo’s examples point at a locally running Ollama server on `http://localhost:11434` and use models such as `deepseek-r1:1.5b`. :contentReference[oaicite:9]{index=9}

## Setup

Install dependencies:

```bash
pip install ollama pydantic
