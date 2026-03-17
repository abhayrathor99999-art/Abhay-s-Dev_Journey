# Day 7 — Virtual Environments, os, datetime

## What I Learned
- venv: isolated Python per project — no conflicts
- os.getcwd(): where am I right now
- os.makedirs(): create folder safely
- os.path.join(): build paths for any OS
- os.path.exists(): check if file/folder exists
- datetime.now(): current date and time
- strftime(): format date as string

## Commands
- python -m venv venv
- venv\Scripts\activate
- pip install package
- pip freeze > requirements.txt
- deactivate

## Patterns
- strftime("%d-%m-%Y") → 18-03-2026
- os.path.join("folder","file.txt") → correct path

## Mistakes I Made
- passwords.json saved in wrong folder
  because path was relative not absolute

## One Thing To Remember
- Every project gets its own venv. Always.
- Never push venv/ to GitHub — push requirements.txt