# Copilot instructions for contributors

This repository is a tiny single-purpose Python project (BookBot) that reads a book text and computes simple statistics. The guidance below focuses on concrete, discoverable patterns so an AI coding agent can be productive immediately.

## Quick runtime (how to run)
- Run the program: `python3 main.py` from the repository root.
- The program reads `books/frankenstein.txt` using the relative path in `main.py`.

## Key files
- `main.py` — entrypoint. Imports `get_word_count` and `get_letter_count` from `stats.py`, reads the book file into memory and prints counts. Note: `main.py` calls `main()` at module level (so importing `main.py` executes the script).
- `stats.py` — contains the library functions used by `main.py` (`get_word_count`, `get_letter_count`). Currently `get_letter_count` is incomplete and contains a stray variable name; fix here when adding functionality.
- `books/` — contains plain-text data used by the script.

## Project patterns & constraints (important for automated edits)
- Small, single-file functions: keep `stats.py` functions pure and deterministic (accept text input and return counts) so they are easy to unit-test.
- Avoid importing `main.py` in other modules/tests because `main()` runs immediately on import. Import functions directly from `stats.py` instead.
- File I/O is done with simple open/read calls in `main.py` — preserve or explicitly improve encoding handling (`encoding='utf-8'`) and consider streaming if file sizes grow.

## Concrete examples (what to change / how to implement)
- `get_word_count(book_text)` currently uses `book_text.split()` and returns `len(words)` — this is the existing word-count approach (split on whitespace).
- `get_letter_count(book_text)` should return the number of alphabetic characters. Example implementation to follow the project's simple style:

```python
def get_letter_count(book_text):
    return sum(1 for ch in book_text if ch.isalpha())
```

Replace the placeholder/inappropriate variable currently in `stats.py` with the above or equivalent logic.

## Tests, CI, and developer workflow
- There are no tests or CI config in the repo. When adding tests, place them in a top-level `tests/` directory and prefer `pytest` with small unit tests that import `stats.get_*` functions directly.
- When modifying `main.py`, ensure you do not introduce side effects on import. If you add CLI parsing, protect top-level execution with `if __name__ == "__main__":`.

## PR checklist for agents
- Run the script locally: `python3 main.py` and verify output matches expectations.
- Add or update unit tests for any changed logic in `stats.py`.
- Keep changes minimal and focused to the failing feature; do not refactor unrelated files.

If anything above is unclear or you'd like the instructions to include additional examples (unit tests, more edge cases, or a small CI workflow), tell me which area to expand. 
