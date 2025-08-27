def more_efficient_look_up(s):
    num_to_index = {}
    longest = 0
    left = 0

    for right, this_char in enumerate(s):
        if this_char in num_to_index and num_to_index[this_char] >= left:
            left = num_to_index[this_char] + 1
        num_to_index[this_char] = right
    
        longest = max(longest, right - left + 1)

    return longest
