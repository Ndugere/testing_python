def the_longest_sequece_of_1_and_os(nums: list) -> int:
    
    if not nums:
        return 0
    
    if len(nums)<2:
        return 1
    longest = 1
    left = 0
    for right in range(1, len(nums)):
        if nums[right - 1] != nums[right]:
            longest = max(right - left +1, longest)
        else:
            left = right
    return longest
        
