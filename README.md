# AmanKharwal Examples

Hands-on exercises for learning GenAI, LLMs, and AI Agents — built and run locally, not just read about.

## Setup

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Note:** `torch` is pinned to the CPU-only build (`2.5.1+cpu`). If `pip install -r requirements.txt` pulls a different torch variant on another machine, reinstall explicitly:
```powershell
pip uninstall torch -y
pip install torch==2.5.1 --index-url https://download.pytorch.org/whl/cpu
```

## Exercises

### Exercise 1 — Text Generation with a Pretrained Model
`E1_Generate_CreativeText.py`

Uses Hugging Face's `pipeline` abstraction to generate text from `distilgpt2` given a prompt. Explores decoding strategy tradeoffs:

- `do_sample`, `top_k`, `top_p`, `temperature` — control randomness in next-token selection
- `repetition_penalty`, `no_repeat_ngram_size` — mitigate repetition/degeneration common in small models

**Key finding:** repetition controls eliminate verbatim repeat loops but can push a weak model toward incoherent rambling instead — a real tradeoff, not a bug. Small pretrained models like `distilgpt2` have real capability limits that decoding tricks alone can't fully overcome.