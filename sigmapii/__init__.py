"""Sigma-Pii - AI bug hunting tool.

Importing the package loads .env, so every entry point sees your OPENAI_API_KEY
without extra setup - `python -m sigmapii.run`, `python -m sigmapii.check`, or a bare
`from sigmapii import llm` in a REPL all pick it up the same way.
"""

from dotenv import load_dotenv

load_dotenv()
