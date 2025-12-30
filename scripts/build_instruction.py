import os
import random
import json

INPUT_FILE = r"C:\Users\Rosh\Documents\GitHub\Ilocano-Generator\data\continuation.jsonl"
OUTPUT_FILE = r"C:\Users\Rosh\Documents\GitHub\Ilocano-Generator\data\instruction.jsonl"

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

INSTRUCTION_TEMPLATES = [
    "Ipadagos ti teksto a mangrugi iti daytoy a linia.",
    "Kumpletuen ti sumaruno a teksto.",
    "Ipadagos ti sursurat a Ilocano.",
    "Ipadagos ti pakasaritaan a mangrugi iti daytoy.",
    "Ipadagos ti naisurat a teksto."
]
MAX_SAMPLES = 150_000
count = 0

with open(INPUT_FILE, 'r', encoding="utf-8") as fin, \
    open(OUTPUT_FILE, 'w', encoding="utf-8") as fout:

    for line in fin:
        if count >= MAX_SAMPLES:
            break

        record = json.loads(line)
        instruction = random.choice(INSTRUCTION_TEMPLATES)

        data = {
            "instruction": instruction,
            "input": record["prompt"],
            "output": record["continuation"],
            "domain": record["domain"]
        }

        fout.write(json.dumps(data, ensure_ascii=False) + "\n")
        count += 1

print(f"instruction.jsonl is created with {count} samples")