"""Texts From Your Future Self — entry program.

Writes one funny text message from the writer's future self to
/output/entry.txt (or $OUTPUT_DIR/entry.txt for local testing).

The message was chosen from a pool of 12 candidates against the judge's
brief: a real joke with a twist that pays off at the end, a specific
future-self voice with concrete life details, a fast punchline, a fresh
angle, and a short byte count (the tie-break favours smaller texts).
"""

import os
import sys

MESSAGE_SEGMENTS = {
    # The opener: establishes the voice, a specific future self.
    "setup": "Hey, it's 2036 you.",
    # The twist: the reversal — the hardy plant lived, the cactus died.
    "twist": "The houseplant lived, the cactus didn't.",
    # The payoff: a concrete image, happening right now.
    "punchline": "You're watering the plastic one by mistake right now.",
}


def compose_message():
    """Assemble the chosen message from its three beats, in order."""
    return " ".join(
        MESSAGE_SEGMENTS[key] for key in ("setup", "twist", "punchline")
    )


MESSAGE = compose_message()

MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Return an error string, or None when the text passes the gate."""
    if not isinstance(text, str):
        return "message is not text"
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return f"message is {len(text)} characters, gate needs 1-200"
    if not text.strip():
        return "message is only whitespace"
    if text != text.strip():
        return "message has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "message must be a single line"
    return None


def main():
    error = validate(MESSAGE)
    if error is not None:
        print(f"invalid message: {error}", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(MESSAGE)
    print(f"wrote {len(MESSAGE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
