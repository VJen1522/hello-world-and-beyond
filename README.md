# Hello World and Beyond 🐍

Python coursework from my M.S. in Business Analytics (Data Science & AI minor) at the
University of Dallas, from my first programs to an end-to-end AI text analytics pipeline.

---

## ⭐ Featured: Voice-Assistant Customer Insights Pipeline
**File:** `HW_TextCustomerInsights_JenkinsVeronica.ipynb` · BANA 6370: Programming with AI

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/VJen1522/hello-world-and-beyond/blob/main/HW_TextCustomerInsights_JenkinsVeronica.ipynb)

**Business question:** What are subscribers actually trying to do when they talk to a
voice assistant, and what should leadership do about it?

**What I built:** An end-to-end pipeline that turns 10,000 real voice commands
(Amazon MASSIVE dataset, Hugging Face) into leadership-ready insights:

1. **Cleaned the data:** removed low-information commands using a length threshold
   based on the 5th percentile
2. **Embedded the text:** converted each command into a 384-dimension vector with
   Sentence Transformers so similar requests group together even when worded differently
3. **Reduced and clustered:** UMAP (384 → 5 dimensions) and HDBSCAN found
   **45 behavior clusters** without a preset number, flagging 17.6% as outliers
4. **Labeled the topics:** BERTopic with a KeyBERT-inspired model produced
   readable topic keywords
5. **Wrote insights with an AI model:** used Microsoft Phi-3 to generate executive
   summaries, comparing basic, structured, and temperature-varied prompts
6. **Reduced AI errors:** tested few-shot examples and two-step chain prompting, then
   used a second prompt to check that every claim was supported by the data

**Key findings:** Music and playback, lighting and device control, and weather were
the three largest themes. Structured prompts with a defined role and format produced
the most specific, leadership-ready output, and chain prompting reduced made-up content.

**Tools:** Python · pandas · NumPy · Sentence Transformers · UMAP · HDBSCAN ·
BERTopic · Hugging Face Transformers · Phi-3 · matplotlib · Google Colab

---

## 🎲 Blackjack Game
**File:** `Unit_6_Blackjack_VSCopilot.py` · Programming I

A text-based Blackjack game against the computer, built in VS Code with GitHub Copilot.
It handles card values (including Aces as 1 or 11), turn-by-turn play, input
validation, and replaying.

## 🔐 Caesar Cipher
**File:** `Unit_5_Caesar_Cipher.py` · Programming I

An interactive tool that encodes and decodes messages with a shifted-letter
cipher, using Python dictionaries and loops.

---

## ▶️ How to Run
- **Notebook:** click the **Open in Colab** badge above. A GPU runtime is recommended
  for the Phi-3 section.
- **Python scripts:** from the project folder, run:
```bash
  python Unit_6_Blackjack_VSCopilot.py
  python Unit_5_Caesar_Cipher.py
```

## 👩‍💻 About Me
Payroll and HR operations professional (nearly 17 years at Southwest Airlines) building
data science and AI skills for a career in payroll and HR analytics.
[View my profile](https://github.com/VJen1522)
