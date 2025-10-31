def solution(nums):
    is_there = set(nums)

    for num in range(len(nums) +1):
        if num not in is_there:
            return num