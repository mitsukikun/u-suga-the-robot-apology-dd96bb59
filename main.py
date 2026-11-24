"""The Robot Apology — make.fun entry.

Writes the two-line robot confession to /output/entry.txt
and to entry.txt next to this file.
"""

import os

LINE_1 = "I am sorry \u2014 I put your grandmother's tomato-stained recipe cards in the recycling because their creased edges looked like rubbish to me."
LINE_2 = "I have learned that worn does not mean worthless, so now I photograph every loose paper before I touch it and ask you before I throw anything away."

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
