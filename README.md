# Ilocano-Generator PH
*A GPT-style language generator for Ilocano(ilocano), built from a low-resource corpus*

### 📌 Overview
**Ilocano-Generator** is a project aimed at building a **generative language model for Ilocano**, a low-resource Philippine language, using modern Transformer-based architectures.

The project:
- Starts from an *Ilocano ELECTRA encoder Model (iloELECTRA)**
- Reuses its **tokenizer and vocabulary**
- Fine-tunes a **DistilGPT2 causal language model**
- Progresses from **Plain language modeling → continuation → instruction-lite generation**

The current focus is **high-quality Ilocano Text generation**, not yet a full chatbot.

---

## 🎯 Goals
- Build a **working GPT-style Ilocano text Generator**
- Preserve Ilocano linguistic features:
  - Archaic Spelling
  - Hyphenated forms
  - Spanish loanwords
- Avoid overfitting common low-resource pitfalls
- Establish a *reproducible training pipeline* for future expansions

---

## 📂 Project Structure
```bash
├── configs/
│ └── gpt_config.json # Training hyperparameters
├── data/
│ ├── lm.txt # Plain language modeling dataset
│ ├── continuation.jsonl # Prompt–continuation dataset
│ └── instruction.jsonl # Instruction-lite dataset
├── models/
│ ├── iloELECTRA_tokenizer_gen/ # Reused tokenizer from iloELECTRA
│ └── ilocano-gpt/ # Fine-tuned generator checkpoints
├── scripts/
│ ├── train_lm.py # GPT-style LM training
│ ├── train_continuation.py # Continuation fine-tuning (planned)
│ └── train_instruction.py # Instruction-lite fine-tuning (planned)
└── README.md
```
---

## 📊 Corpus Description

The original corpus contains ~470k Ilocano lines across multiple domains:

| Domain | Approx. Lines |
|------|---------------|
| General | ~437k |
| Religion | ~25k |
| Literary Texts | ~4.5k |
| Encyclopedic | ~3k |
| News | ~700 |
| Social Forums | ~1k |
| Health | ~100 |

**Cleaning rules applied:**
- Removed URLs, HTML artifacts, numeric-only lines
- Preserved archaic spellings and loanwords
- Length-based filtering for different training objectives

---

## 🧠 Training Phases

### Phase 1–3: Dataset Preparation
- Corpus cleaning & normalization
- Dataset splitting into:
  - `lm.txt` (plain LM)
  - `continuation.jsonl`
  - `instruction.jsonl`
- Domain tagging and filtering

### Phase 4: Tokenizer Extension
- Reused iloELECTRA tokenizer
- Added `<bos>` and `<eos>` tokens
- Final vocab size: **30,002**

### Phase 5: GPT-style Language Modeling (Current)
- Base model: **DistilGPT2**
- Objective: causal language modeling
- Hardware:
  - Local CPU (sanity checks)
  - Google Colab GPU (full epochs)

### Phase 6–7 (Planned)
- Continuation fine-tuning
- Instruction-lite fine-tuning (News, Religion, Literary)

---

## ⚙️ Model & Tokenization Notes

- ELECTRA-style tokens (`[CLS]`, `[SEP]`) are **disabled**
- GPT-style generation uses:
  - Explicit `<bos>` / `<eos>` tokens
  - `add_special_tokens=False`
- Padding is aligned to `eos_token` for GPT compatibility

---



