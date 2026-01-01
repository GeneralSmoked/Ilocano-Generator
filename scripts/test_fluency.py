import torch
from transformers import GPT2LMHeadModel, AutoTokenizer

MODEL_DIR = "models/ilocano-gpt"
USE_GPU = torch.cuda.is_available()

PROMPTS = [
    "<bos> Annungen daguiti amaen",
    "<bos> Annong iti balasang",
    "<bos> Ti Dios tenglennat pigsa ti tao",
    "<bos> Surutem ti nalinteg a dalan",
    "<bos> Iti panagbiag ti tao"
]

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
print("Loading model...")
model = GPT2LMHeadModel.from_pretrained(MODEL_DIR)
model.eval()

if USE_GPU:
    model.to("cuda")
    print("Using GPU")
else:
    print("Using CPU")

def generate_text(prompt, max_new_tokens = 60, temperature = 0.9, top_k=50, top_p=0.95):
    inputs = tokenizer(prompt, return_tensors="pt")

    if USE_GPU:
        inputs = {k: v.to("cuda") for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=temperature,
            top_k=top_k,
            top_p=top_p,
            repetition_penalty=1.2,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

print("\n=== TEST A: FREE GENERATION(FLUENCY TEST) ===\n")

for i, prompt in enumerate(PROMPTS,1):
    print(f"---Sample {i}---")
    print("Prompt:", prompt)
    print("Output:")
    print(generate_text(prompt))
    print()