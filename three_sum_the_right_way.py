def three_sum(arr, target):
    res = []
    arr.sort()

    for i, num in enumerate(arr):
        # Skip duplicate starting numbers
        if i > 0 and num == arr[i - 1]:
            continue
        
        # Early termination: smallest possible sum exceeds target
        if num * 3 > target:
            break

        left = i + 1
        right = len(arr) - 1

        while left < right:
            total = num + arr[left] + arr[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                res.append([num, arr[left], arr[right]])
                left += 1
                right -= 1

                # Skip duplicates
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

    return res
