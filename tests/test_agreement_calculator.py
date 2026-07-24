from src.agreement_calculator import cohens_kappa

## Test a known result
def test_cohens_kappa_known_value():
    a = ["positive", "negative", "positive", "neutral"]
    b = ["positive", "negative", "negative", "neutral"]
    result = cohens_kappa(a,b)
    assert round(result,4) == 0.6364

## Edge case of perfect agreement
def test_cohens_kappa_perfect_agreement():
    a = ["positive", "negative", "positive", "neutral"]
    b = ["positive", "negative", "positive", "neutral"]
    result = cohens_kappa(a,b)
    assert result == 1.0
