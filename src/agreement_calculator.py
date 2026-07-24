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

if __name__ == "__main__":
    a = ["positive", "negative", "positive", "neutral"]
    b = ["positive", "negative", "negative", "neutral"]
    print(cohens_kappa(a,b))