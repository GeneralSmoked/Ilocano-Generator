import os
from transformers import AutoTokenizer

TOKENIZER_DIR = r"C:\Users\Rosh\Documents\GitHub\Ilocano-Generator\models\iloELECTRA_tokenizer"
OUTPUT_DIR = r"C:\Users\Rosh\Documents\GitHub\Ilocano-Generator\models\iloELECTRA_tokenizer_gen"

os.makedirs(OUTPUT_DIR, exist_ok=True)

tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_DIR)

print("Original vocab size:", len(tokenizer))

special_tokens = {
    "bos_token":"<bos>",
    "eos_token":"<eos>",
}

num_added = tokenizer.add_special_tokens(special_tokens)

print("Added Tokens: ", num_added)
print("New vocab size:", len(tokenizer))

tokenizer.save_pretrained(OUTPUT_DIR)

print("Extended tokenizer saved to", OUTPUT_DIR)