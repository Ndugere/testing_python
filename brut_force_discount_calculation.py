def brute_force_discounts_cal(nums: list) -> list:
    #Input: prices = [8, 4, 6, 2, 3]
    #Output: [4, 2, 4, 2, 3]
    i = 0
    res = []
    for i in range(len(nums) -1):
        found = False
        for j in range(i +1, len(nums)):
            if nums[j] < nums[i]:
                res.append(nums[i] - nums[j])
                found = True
                break
        if not found:
            res.append(nums[i])
    res.append(nums[-1])

    return res


