import os

INPUT_DIR = r"C:\Users\Rosh\Documents\GitHub\Ilocano-Generator\corpus_work_cleaned"
OUTPUT_FILE = r"C:\Users\Rosh\Documents\GitHub\Ilocano-Generator\data\lm.text"

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

def word_count(line: str) -> int:
    return len(line.strip().split())

total = 0

with open(OUTPUT_FILE, "w", encoding="utf-8") as fout:
    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".txt"):
            continue

        with open(os.path.join(INPUT_DIR, filename), "r", encoding="utf-8") as fin:
            for line in fin:
                line  = line.strip()
                if word_count(line) >= 4:
                    fout.write(f"<bos> {line} <eos>\n")
                    total +=1

print(f"lm.txt is created with a total of {total} lines")

    