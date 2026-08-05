# Annotator Agreement Calculator

A Python tool for calculating inter-annotator agreement in labeled datasets 
that was built to demonstrate the statistical methods used in real QA 
workflows to flag areas of confusion.

## What it does

- **Cohen's Kappa** — measures agreement between 2 annotators, corrected for chance
- **Fleiss' Kappa** — extends this to 3+ annotators using a count-matrix approach
- **Label confusion analysis** — identifies which label pairs are most often confused across a dataset

## Setup

```bash
git clone https://github.com/c-ribolla/annotator-agreement-calculator.git
cd annotator-agreement-calculator
python -m venv venv
venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt
```

## Usage

Run the main script (demonstrates all three functions against the sample dataset):
```bash
python src/agreement_calculator.py
```

Run the test suite:
```bash
pytest
```

## Results & Analysis

This project calculates inter-annotator agreement using both Cohen's Kappa and 
Fleiss' Kappa on the same 8-item dataset. The dataset is intentionally small 
to demonstrate the methodology rather than produce statistically significant 
findings. In a production setting, this analysis would need a substantially 
larger dataset before drawing any firm conclusions.

Cohen's Kappa (annotator_A vs. annotator_B only) came out to 0.4286, while 
Fleiss' Kappa across all three annotators was 0.3717. It makes sense this is 
lower since adding a third annotator introduces more opportunities for 
disagreement than comparing just one pair.

If we look at the three lowest-agreement items individually, "neutral" 
initially appears to be the most confused label. However, measuring 
disagreement across the entire dataset actually showed that neutral/positive 
and negative/positive each had two instances of disagreement, while 
negative/neutral had only one. This would suggest that the confusion isn't 
necessarily isolated to the "neutral" label. It could mean that the underlying 
text should be reviewed for the presence of sarcasm, ambiguity, or mixed 
sentiment.

## Background

I've seen this exact pattern before in production where borderline items 
like a "neutral" label end up being the swing vote between two annotators 
leaning positive or negative. The goal was to turn that hands-on experience 
into a working tool.

## Tech stack

Python, pandas, pytest
