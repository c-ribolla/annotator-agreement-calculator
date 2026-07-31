import pandas as pd
from src.agreement_calculator import cohens_kappa, fleiss_kappa, label_confusion_pairs

## Test a known result
def test_cohens_kappa_known_value():
    a = ["positive", "negative", "positive", "neutral"]
    b = ["positive", "negative", "negative", "neutral"]
    result = cohens_kappa(a,b)
    assert round(result,4) == 0.6364

def test_fleiss_kappa_known_value():
    df = pd.read_csv("data/sample_annotations.csv")
    count_matrix = pd.crosstab(df["item_id"], df["label"])
    result = fleiss_kappa(count_matrix, n_annotators=3)
    assert round(result,4) == 0.3717

## Edge case of perfect agreement
def test_cohens_kappa_perfect_agreement():
    a = ["positive", "negative", "positive", "neutral"]
    b = ["positive", "negative", "positive", "neutral"]
    result = cohens_kappa(a,b)
    assert result == 1.0

def test_fleiss_kappa_perfect_agreement():
    data = {
        "item_id": [1, 1, 1, 2, 2, 2],
        "label": ["positive", "positive", "positive", "negative", "negative", "negative"]
    }
    df = pd.DataFrame(data)
    count_matrix = pd.crosstab(df["item_id"], df["label"])
    result = fleiss_kappa(count_matrix, n_annotators=3)
    assert result == 1.0
    
def test_label_confusion_pairs_known_value():
    df = pd.read_csv("data/sample_annotations.csv")
    result = label_confusion_pairs(df)
    assert result[("neutral", "positive")] == 2
    assert result[("negative", "positive")] == 2
    assert result[("negative", "neutral")] == 1