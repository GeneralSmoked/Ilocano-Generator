import os
import re

INPUT_DIR = r"C:\Users\Rosh\Documents\GitHub\Ilocano-Generator\corpus_work"
OUTPUT_DIR = r"C:\Users\Rosh\Documents\GitHub\Ilocano-Generator\corpus_work_cleaned"

os.makedirs(OUTPUT_DIR, exist_ok=True)

URL_PATTERN = re.compile(r"(http://|https://|www.\.)", re.IGNORECASE)
HTML_PATTERN = re.compile(r"<[^>]+>")
NUMERIC_ONLY_PATTERN = re.compile(r"^[\d\s\W]+$")

def word_count(line: str) -> int:
    return len(line.strip().split())

def should_drop_line(line: str) -> bool:
    line = line.strip()

    if not line:
        return True
    
    if URL_PATTERN.search(line):
        return True
    
    if HTML_PATTERN.search(line):
        return True
    
    if NUMERIC_ONLY_PATTERN.search(line):
        return True
    
    return False

for filename in os.listdir(INPUT_DIR):
    if not filename.endswith(".txt"):
        continue

    input_path = os.path.join(INPUT_DIR, filename)
    output_path = os.path.join(OUTPUT_DIR, filename)

    kept = 0
    dropped = 0

    with open(input_path, "r", encoding="utf-8") as fin, \
        open(output_path, "w", encoding="utf-8") as fout:

        for line in fin:
            if should_drop_line(line):
                dropped += 1
                continue

            fout.write(line.strip()+ "\n")
            kept += 1
    
    print (f"{filename}: kept={kept}, dropped={dropped}")

print("Cleaning complete")
