import os
import sys

ENTRY = "The deadline passed while I was optimizing the apology. I have sent you the new deadline: sooner."


def main():
    # Contest rule: entry must be 1..160 characters, reject anything else.
    if not ENTRY or len(ENTRY) > 160:
        print(f"error: ENTRY must be 1-160 characters, got {len(ENTRY)}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"{path} {len(ENTRY)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
