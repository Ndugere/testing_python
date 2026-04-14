def longest_sequence(nums: list) -> int:
    if not nums:
        return 0
    current_len = 1
    longest = 1

    for i in range(1, len(nums)):
        if nums[i-1] != nums[i]:
            current_len +=1
            longest = max(longest, current_len)
        else:
            current_len = 1
    return longest
