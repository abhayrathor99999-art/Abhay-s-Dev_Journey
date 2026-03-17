# Day 6 — Error Handling, File I/O, JSON

## What I Learned
- try/except: catch errors instead of crashing
- with open(): always use this — auto closes file
- File modes: r=read, w=write(erases), a=append
- json.dump() → dict to file
- json.dumps() → dict to string
- json.load() → file to dict
- json.loads() → string to dict

## Patterns
- Safe file read: try → open → json.load → except FileNotFoundError
- Save pattern: open with "w" → json.dump → indent=4

## Mistakes I Made
- Used "w" mode instead of "a" — erased the file
- Wrote f.read(filename) — f.read() takes no argument
- Put result={} outside function — global state bug

## One Thing To Remember
- 's' in dumps/loads = string. No 's' = file.
- with open() closes automatically — always use it