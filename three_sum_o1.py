def three_sum(nums: list, target: int) -> list:
    if len(nums) < 3:
        return []

    nums.sort()
    if nums[0] > target:
        return []

    res = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j, k = i + 1, len(nums) - 1

        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total == target:
                res.append([nums[i], nums[j], nums[k]])

                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1

                k -= 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1

            elif total > target:
                k -= 1
            else:
                j += 1

    return res