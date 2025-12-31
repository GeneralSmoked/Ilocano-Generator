import os
import json

INPUT_DIR = r"C:\Users\Rosh\Documents\GitHub\Ilocano-Generator\corpus_work_cleaned"
OUTPUT_FILE = r"C:\Users\Rosh\Documents\GitHub\Ilocano-Generator\data\continuation.jsonl"

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

def split_line(words):
    split_idx = max(3, int(len(words) *0.4))
    return " ".join(words[:split_idx]), " ".join(words[split_idx:])

total = 0

with open(OUTPUT_FILE, "w", encoding="utf-8") as fout:
    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".txt"):
            continue

        domain = filename.replace(".txt", "")

        with open(os.path.join(INPUT_DIR, filename), "r", encoding="utf-8") as fin:
            for line in fin:
                words = line.strip().split()

                if len(words) <= 6:
                    continue

                prompt, continuation = split_line(words)

                record = {
                    "domain": domain,
                    "prompt": f"<bos> {prompt}",
                    "continuation": f"{continuation} <eos>"
                }

                fout.write(json.dumps(record, ensure_ascii=False) + "\n")
                total += 1

print(f"continuation.jsonl is created with {total} samples")