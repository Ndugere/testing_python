def merge_sort(lst):
    """
    Recursively sorts a list in ascending order using the merge sort algorithm.

    Steps:
    1. If the list has 0 or 1 elements, it's already sorted.
    2. Split the list into two halves.
    3. Recursively sort each half.
    4. Merge the two sorted halves into a single sorted list.
    """
    if len(lst) <= 1:
        return lst

    left, right = split_list(lst)
    left = merge_sort(left)
    right = merge_sort(right)

    return sorted_list(left, right)

def split_list(lst):
    """
    Splits a list into two halves.

    Parameters:
    - lst: The list to split.

    Returns:
    - A tuple containing the left and right halves.
    """
    mid = len(lst) // 2
    return lst[:mid], lst[mid:]

def sorted_list(left, right):
    """
    Merges two sorted lists into one sorted list.

    Parameters:
    - left: First sorted list.
    - right: Second sorted list.

    Returns:
    - A new list containing all elements from left and right, sorted.
    """
    result = []
    i, j = 0, 0

    # Compare elements from both lists and append the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from both lists
    result.extend(left[i:])
    result.extend(right[j:])

    return result
