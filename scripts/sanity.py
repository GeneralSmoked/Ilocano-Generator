from transformers import AutoTokenizer, GPT2LMHeadModel

tokenizer = AutoTokenizer.from_pretrained("models/iloELECTRA_tokenizer_gen")

tokenizer.pad_token = tokenizer.eos_token

model = GPT2LMHeadModel.from_pretrained("distilgpt2")
model.resize_token_embeddings(len(tokenizer))
model.config.pad_token_id = tokenizer.eos_token_id

inputs = tokenizer(
    "<bos> Annungen daguiti",
    return_tensors="pt",
    add_special_tokens=False
)

out = model.generate(
    inputs["input_ids"],
    attention_mask=inputs["attention_mask"],
    max_length=30
)

print(tokenizer.decode(out[0]))