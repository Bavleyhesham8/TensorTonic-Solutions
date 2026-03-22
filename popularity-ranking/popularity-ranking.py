def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    ans=[]
    for avg_rating,num_votes in items:
        ans.append((num_votes/(num_votes+min_votes))*avg_rating+(min_votes/(min_votes+num_votes))*global_mean)
    return ans
    # Write code here