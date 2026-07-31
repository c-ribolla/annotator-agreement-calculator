import pandas as pd
from collections import Counter
from itertools import combinations

def cohens_kappa(annotator_a_labels: list, annotator_b_labels: list) -> float:
    """
    Compute Cohen's Kappa between two annotators. 
    Both lists must be the same length and in the same order.
    """
    ## Compute Agreements
    unique_labels = set(annotator_a_labels + annotator_b_labels)
    observed_agreement = sum(a == b for a, b in zip(annotator_a_labels, annotator_b_labels)) / len(annotator_a_labels)
    expected_agreement = 0
    for label in unique_labels:
     a_proportion = annotator_a_labels.count(label) / len(annotator_a_labels)
     b_proportion = annotator_b_labels.count(label) / len(annotator_b_labels)
     expected_agreement += a_proportion * b_proportion

    ## Calculate Cohen's Kappa
    kappa = (observed_agreement - expected_agreement) / (1 - expected_agreement)
    return kappa
    
    
def fleiss_kappa(count_matrix, n_annotators:int) -> float:
    """
    Compute Fleiss' Kappa from a count matrix.
    count_matrix: DataFrame, items as rows, labels as columns, 
    values = number of annotators who chose that label for that item.
    n_annotators: number of annotators per item (must be constant across items).
    """
    N = len(count_matrix)
    
    #Compute Agreements
    p_i_per_item = (count_matrix.pow(2).sum(axis=1) - n_annotators) / (n_annotators * (n_annotators - 1))
    p_bar = p_i_per_item.mean()
    
    p_j = count_matrix.sum(axis=0) / (N * n_annotators)
    p_e_bar = sum(p_j**2)
    
    #Compute Fleiss' Kappa
    kappa = (p_bar - p_e_bar) / (1 - p_e_bar)
    return kappa

def label_confusion_pairs(df, item_col="item_id", label_col="label"):
    """
    Count how often each pair of labels appears in disagreement together.
    df: long-format DataFrame with one row per item-annotator pair.
    Returns a Counter mapping (label1, label2) -> count of items where both appeared.
    """
    labels_per_item = df.groupby(item_col)[label_col].apply(set)
    disagreement_pairs = []
    for label_set in labels_per_item:
        if len(label_set) > 1:
            for pair in combinations(sorted(label_set), 2):
                disagreement_pairs.append(pair)     
    return Counter(disagreement_pairs)

if __name__ == "__main__":
    df = pd.read_csv("data/sample_annotations.csv")
    
    pivoted = df.pivot(index="item_id", columns="annotator", values="label")
    print(cohens_kappa(pivoted["annotator_A"].tolist(), pivoted["annotator_B"].tolist()))
    
    count_matrix = pd.crosstab(df["item_id"], df["label"])
    print(fleiss_kappa(count_matrix, n_annotators=3))
    
    pair_counts = label_confusion_pairs(df)
    print(pair_counts)