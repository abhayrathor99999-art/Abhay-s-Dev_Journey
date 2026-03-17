# Day 8 — Type Hints + mypy

## What I Learned
- Type hints: labels that show what goes in and out
- Variable hints: name: str, age: int, score: float
- Function hints: def fn(a: int, b: int) -> str:
- Returns nothing: -> None
- Returns list: -> list
- Optional: str | None (either str or None)
- mypy: checks types without running code

## Syntax
- def add(a: int, b: int) -> int:
- def greet(name: str) -> str:
- def save(data: list) -> None:
- def search(key: str) -> dict | None:

## Where I Will Use This
- FastAPI Month 6: required for endpoints
- TypeScript Month 8: same concept different language
- Every function from now: type hints always

## Commands
- pip install mypy
- mypy filename.py
- Success: no issues found = zero errors

## One Thing To Remember
- Type hints don't convert or force types
- They are labels — like a sign on a door
- -> shows what comes OUT of the function