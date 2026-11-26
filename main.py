"""The Meeting That Should Have Been One Line.

Decision record (weighed against the judge's criteria, most important first:
single line that replaces the meeting / kills it outright / relatable /
funny with a turn / stands alone):

Candidate A — "The update is: nothing has changed since the email, and the
email has not changed since the last meeting." CHOSEN. It IS the meeting's
own opening line, and it closes the loop: the email says nothing new, the
last meeting said nothing new, so this meeting has no reason to exist. The
"update" framing makes it the sentence that replaces the whole meeting
rather than a complaint about it, and the echo of "the email" twice gives
it the deadpan rhythm of a status report.

Candidate B — "This meeting exists because three people needed to hear the
same sentence at the same time, and none of them read the email." LOSES.
Relatable and it explains why the meeting was called, but it describes the
meeting instead of replacing it — after this line someone could still say
"right, so let me read the email out loud now", and the meeting survives.

Candidate C — "The decision was made in the hallway five minutes ago; this
meeting is just the paperwork." LOSES. A good sting and very relatable, but
"just the paperwork" is a shrug, not a kill: a meeting that is paperwork
still gets held. It also leans on a hallway decision, which is a specific
scene not every office shares, so it is less universal than A.

Candidate D — "If this meeting had an agenda, it would just say: please
confirm you received the email." LOSES. Funny and it kills the meeting's
purpose, but it is a joke ABOUT the meeting's agenda rather than the line
that replaces the meeting itself, and it needs the reader to picture an
agenda to land. A is the thing itself, not a comment on it.

Writing passes on the winner:
Pass 1 — first draft was "Nothing has changed since the email, and the
email has not changed since the last meeting." Adding "The update is:"
turned a bare observation into the meeting's own opening sentence, which is
what the brief asks for: the line that replaces the meeting, delivered as
if it were the meeting.
Pass 2 — tried ending "...since the last meeting about the email." and
dropped it: repeating "meeting" muddies the loop and the extra clause
slows the sentence. The clean ending "...since the last meeting." lands
harder because the loop snaps shut on the word the reader already expects.
"""

import os

MAX_CHARS = 200

LINE = ("The update is: nothing has changed since the email, and the email "
        "has not changed since the last meeting.")


def check_gate(line):
    """Mirror the sealed gate: 1-200 chars, not only whitespace, one line."""
    return 1 <= len(line) <= MAX_CHARS and line.strip() != "" and "\n" not in line


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    if not check_gate(LINE):
        raise SystemExit("line fails the 1-200 character gate")
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
