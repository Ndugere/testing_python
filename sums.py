def combinations_that_sum_to_target(nums, target):
    results = []

    def backtrack(start, current_list, current_sum):
        if current_sum == target:
            results.append(list(current_list))
            return
        
        if current_sum > target:
            return

        for i in range(start, len(nums)):
            current_list.append(nums[i])
            backtrack(i + 1, current_list, current_sum + nums[i])
            current_list.pop()

    backtrack(0, [], 0)
    return results
