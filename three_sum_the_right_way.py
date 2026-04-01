def three_sum_final(arr, target):
    arr.sort()
    res = []

    for i, num in enumerate(arr):
        # Final mathematical pruning: stop early if the smallest possible sum is already too big
        if num * 3 > target:
            break

        left, right = i + 1, len(arr) - 1

        while left < right:
            total = num + arr[left] + arr[right]

            if total == target:
                res.append([num, arr[left], arr[right]])

                # Move both pointers and skip duplicates
                left += 1
                right -= 1

                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif total < target:
                left += 1  # Increase sum
            else:
                right -= 1  # Decrease sum

    return res