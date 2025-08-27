def longest_substring_without_reapeating_characters(s):
    longest_substring = 0
    num_to_index = {}
    left = 0

    for each_char in range(len(s)):
        if s[each_char] in num_to_index:
            num_to_index[s[each_char]] += 1
        else:
            num_to_index[s[each_char]] = 1
        
        while num_to_index[s[each_char]] > 1:
            num_to_index[s[left]] -= 1
            left += 1
        
        length_of_current_substring = each_char - left + 1
        longest_substring = max(longest_substring, length_of_current_substring)
    
    return longest_substring
