def subarray_sum_fixed(nums, k):
    subarray_sum = sum(nums[:k])
    largest_sum = subarray_sum

    for right in range(k, len(nums)):
        subarray_sum = subarray_sum + nums[right] - nums[right - k]
        largest_sum = max(subarray_sum, largest_sum)

    return largest_sum
