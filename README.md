# Ilocano-Generator PH
*A GPT-style language generator for Ilocano(ilocano), built from a low-resource corpus*

### Overview
**Ilocano-Generator** is a project aimed at building a **generative language model for Ilocano**, a low-resource Philippine language, using modern Transformer-based architectures.

The project:
- Starts from an *Ilocano ELECTRA encoder Model (iloELECTRA)**
- Reuses its **tokenizer and vocabulary**
- Fine-tunes a **DistilGPT2 causal language model**
- Progresses from **Plain language modeling → continuation → instruction-lite generation**

The current focus is **high-quality Ilocano Text generation**, not yet a full chatbot.

## Goals
- Build a **working GPT-style Ilocano text Generator**
- Preserve Ilocano linguistic features:
  - Archaic Spelling
  - Hyphenated forms
  - Spanish loanwords
- Avoid overfitting common low-resource pitfalls
- Establish a *reproducible training pipeline* for future expansions



