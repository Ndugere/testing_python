def check_for_pattern(pattern, source):
    """
    – The pattern and substring are equal in length.
    – Where there is a 0 in the pattern, there is a vowel in the substring. 
    – Where there is a 1 in the pattern, there is a consonant in the substring. 
    """
    res = 0
    vowels = {"a", "e", "i", "o", "u", "y"}

    if len(pattern) > len(source):
        return res
    
    right = len(pattern)
    left = 0

    while right <= len(source):
        valid_substring = True
        substring = source[left:right]

        for i, each_char in enumerate(substring):
            if each_char in vowels and int(pattern[i]) == 1 \
            or each_char not in vowels and int(pattern[i]) == 0:
                valid_substring = False
                break
            else:
                continue
        
        if valid_substring:
            res += 1

        right += 1
        left += 1
    
    return res
    