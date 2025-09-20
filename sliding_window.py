def longest_substring_without_repeating_characters(s):
    longest, left, right = 0, 0, 0
    seen_so_far = {}

    while right < len(s):
        if s[right] in seen_so_far:
            seen_so_far[s[right]] += 1  
        else:
            seen_so_far[s[right]] = 1
        
        while seen_so_far[s[right]] > 1:
            seen_so_far[s[left]] -= 1
            left += 1 

        longest = max(longest, right + 1 - left)

        right += 1

    return longest



