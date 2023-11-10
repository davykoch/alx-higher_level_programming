#!/usr/bin/python3
def weight_average(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return 0

    # Initialize variables to store the total score and total weight
    total_score = 0
    total_weight = 0

    # Iterate over each tuple in the list
    for score, weight in my_list:
        # Calculate the weighted sum of scores
        total_score += score * weight
        # Accumulate the total weight
        total_weight += weight

    # Check if the total weight is zero to avoid division by zero
    if total_weight == 0:
        return 0

    # Calculate the weighted average
    return total_score / total_weight
