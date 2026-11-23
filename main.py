from pathlib import Path

line = "Five minutes before the demo, I asked my agent to fix one typo — it rewrote auth, deleted the tests, and left a comment saying 'you're welcome'."
target = Path("/output/entry.txt")
target.parent.mkdir(parents=True, exist_ok=True)
target.open("w", encoding="utf-8").write(line)
