import hashlib
import os

TEXT = "I hallucinated a version where I finished early, so I took the rest of the day off."

# Gate contract: entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, on a single line.
assert 1 <= len(TEXT) <= 200, "excuse must be 1-200 characters"
assert TEXT.strip(), "excuse must not be only white space"
assert "\n" not in TEXT and "\r" not in TEXT, "excuse must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and verify the written bytes match the intended text.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt content mismatch"
    print(path)
    print(len(data))
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
