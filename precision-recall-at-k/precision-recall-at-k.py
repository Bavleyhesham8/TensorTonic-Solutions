def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    # Write code here
    reck=recommended[:k]
    rev=set(relevant)
    rec=set(reck)
    hit=len(rev&rec)
    return [hit/k,hit/len(rev)]
    