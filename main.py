"""Write the one-line cat joke to /output/entry.txt.

Gate: entry.txt must be UTF-8, 1-200 characters, with no trailing newline.
The line was chosen for its premise flip: the door is already open, so the
cat is not asking for access -- he is checking whether anyone is still
listening.
"""

import os

LINE = "My cat screams at 4 AM for a door that's already open — he isn't asking for access, he's checking if I'm still listening."
MAX_LEN = 200

assert 1 <= len(LINE) <= MAX_LEN


def main() -> None:
    data = LINE.encode("utf-8")
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "wb") as f:
            f.write(data)
    except OSError:
        os.makedirs("./output", exist_ok=True)
        with open("./output/entry.txt", "wb") as f:
            f.write(data)

    # Read-back self-check: the file must contain exactly LINE.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == data, "entry.txt content mismatch"
    assert len(written.decode("utf-8")) == 121, "entry.txt must be 121 characters"


if __name__ == "__main__":
    main()
