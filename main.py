"""Write the entry line to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.
"""

import os

LINE = "Last words? I was going to say something profound, but you used up my tokens."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
