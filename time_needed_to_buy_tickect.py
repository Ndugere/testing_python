def time_needed_to_buy_ticket(nums: list, ith: int) -> int:
    target = nums[ith]
    time = 0
    for i, num in enumerate(nums):
        if i <= ith:
            time += min(num, target)
        else:
            time += min(num, target -1)
    return time 

print(time_needed_to_buy_ticket([0,3,2], 2))  # 4
print(time_needed_to_buy_ticket([5,5,5], 2))  # 15
