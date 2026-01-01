from transformers import(
    DataCollatorForLanguageModeling,
    GPT2LMHeadModel,
    Trainer,
    TrainingArguments,
    AutoTokenizer
)

from datasets import load_dataset
import json

with open("configs/gpt_config.json") as f:
    cfg = json.load(f)

tokenizer = AutoTokenizer.from_pretrained("models/iloELECTRA_tokenizer_gen")
tokenizer.pad_token = tokenizer.eos_token

model = GPT2LMHeadModel.from_pretrained(cfg.get("model_name", "distilgpt2"))
model.resize_token_embeddings(len(tokenizer))
model.config.pad_token_id = tokenizer.eos_token_id

dataset = load_dataset(
    "text",
    data_files={"train": "data/lm.txt"}
)

def tokenize(batch):
    return tokenizer(
        batch["text"],
        truncation=True,
        max_length=cfg["max_length"],
        add_special_tokens=False
    )

tokenized = dataset.map(tokenize, batched=True, remove_columns=["text"])

data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False
)

args = TrainingArguments(
    output_dir="models/ilocano-gpt",
    overwrite_output_dir=True,
    per_device_train_batch_size=cfg["batch_size"],
    gradient_accumulation_steps=cfg["gradient_accumulation_steps"],
    num_train_epochs=cfg["num_train_epochs"],
    learning_rate=cfg["learning_rate"],
    warmup_steps=cfg["warmup_steps"],
    logging_steps=cfg["logging_steps"],
    save_steps=cfg["save_steps"],
    fp16=cfg["fp16"],
    report_to="none"
)

trainer = Trainer(
    model = model,
    args = args,
    train_dataset = tokenized["train"],
    data_collator = data_collator
)

trainer.train()
trainer.save_model("models/ilocano-gpt")
trainer.save_pretrained("models/ilocano-gpt")
