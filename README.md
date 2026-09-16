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

What this code is actually solving (narrowly)

At its core, this script solves one specific, small problem: given a partial piece of text, generate a plausible continuation. That's it. Nothing more sophisticated is happening — no reasoning, no fact-checking, no understanding of what "AI Agnet" (typo and all) even means. It's pure statistical pattern continuation based on what distilgpt2 learned from its training data.

The two things you actually learned via this exercise, more precisely:

How to consume a pretrained language model for inference (not train one) — the "call pipeline(), get text back" pattern
How decoding strategy (the parameters) shapes output quality/behavior — independent of the model itself, these knobs control the tradeoff between coherence, repetition, and creativity
Where this connects to real daily/production use cases

This exact pattern — pretrained model + decoding parameters — is the backbone of a surprising amount of real, deployed software, even though the model here is toy-grade. A few concrete, current examples:

Autocomplete/autosuggest (email compose, code editors like GitHub Copilot, search-bar suggestions) — same next-token generation loop, just with a much bigger/better model and usually greedy or low-temperature decoding (since users want predictable, not creative, completions)
Chatbots/customer support assistants — same pipeline-style call pattern (prompt in, text out), just swapping distilgpt2 for something like GPT-4-class or Llama, and layering a system prompt + conversation history on top of the same core mechanism
Content drafting tools (marketing copy generators, "write me a product description" tools) — literally this same sampling logic; temperature/top_p tuning is exactly how these products let users choose "safe and consistent" vs "creative and varied" output
Summarization and paraphrasing tools — different task framing, same underlying generation mechanics
The honest caveat, since you value being pushed back on this rather than told everything's great

distilgpt2 itself has zero direct production relevance today — it's a 2019-era distilled GPT-2, objectively weak by any current standard (as your own repeated-output runs demonstrated). No one would ship this model in a real product now. Its value here is purely pedagogical: it's small enough to run instantly on your CPU, cheap enough to iterate on quickly, and — critically — it's weak enough that its failure modes (repetition, incoherence) are easy to observe and reason about, which is exactly what you did. A stronger model would have masked these dynamics behind better output, teaching you less about the mechanics.

A natural, honest next step, if you want to bridge from "toy demo" to "something closer to daily relevance": swap distilgpt2 for a genuinely current, small-but-capable open model (e.g., something in the Llama 3.2 1B/3B or Qwen2.5 class) and rerun the exact same script/parameters. That would let you compare, with real evidence, how much of what you observed was "small model weakness" versus "decoding parameter effects" — since a stronger model should be far more resistant to repetition even without no_repeat_ngram_size/repetition_penalty help.
