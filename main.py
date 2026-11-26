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

Revision pass (pipeline review, output byte-identical):
Candidate E — "Status: unchanged." LOSES. Two words, kills the meeting,
but it is a label, not a sentence anyone would say out loud as the meeting
itself, and it loses the email loop that makes A recognisable to anyone
who has ever received the same status email twice.
Candidate F — "We are meeting to confirm that the email you already read
is the email we already sent." LOSES, close. It names the absurdity
directly, but it explains the joke instead of being the update; A wins
because its deadpan "The update is:" framing performs the meeting rather
than commenting on it, and its loop (email -> last meeting -> this one)
implies an infinite regress F states only once.
Candidate G — "Nothing to report, again." LOSES. Tight and relatable, but
"again" does all the work and the line could fit any recurring chore, not
specifically a meeting that an email already replaced.
Decision after revision: keep A exactly as written. The only code change
in this pass is structural: a dedicated gate-guard helper (guard_line)
that rejects empty, oversized, or multi-line candidates before the
existing gate check runs, so a future edit to LINE fails loudly at the
guard instead of silently writing a bad entry file. The shipped line,
its wording, and the bytes written to entry.txt are unchanged.
"""

import os

MAX_CHARS = 200

LINE = ("The update is: nothing has changed since the email, and the email "
        "has not changed since the last meeting.")


def guard_line(line):
    """Gate-guard: reject empty, oversized, or multi-line candidates early.

    Runs before check_gate so a bad future edit to LINE fails with a
    specific reason instead of a generic gate failure at write time.
    """
    if not isinstance(line, str) or line.strip() == "":
        raise SystemExit("guard: line is empty or not text")
    if len(line) > MAX_CHARS:
        raise SystemExit("guard: line exceeds the 200 character gate")
    if "\n" in line or "\r" in line:
        raise SystemExit("guard: line must be a single line")
    return line


def check_gate(line):
    """Mirror the sealed gate: 1-200 chars, not only whitespace, one line."""
    return 1 <= len(line) <= MAX_CHARS and line.strip() != "" and "\n" not in line


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    guard_line(LINE)
    if not check_gate(LINE):
        raise SystemExit("line fails the 1-200 character gate")
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
