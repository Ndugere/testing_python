def three_sum(arr):
    res = []
    seen = set()
    for i in range(len(arr) - 2):
        if i >0 and arr[i] in seen:
            continue
        else:
            seen.add(arr[i])
        def first_value():
            two_other_values = two_sum(arr[i+1:], target = 0 - arr[i])
            if two_other_values:
                res.append([arr[i].extend(two_other_values)])

        def two_sum(arr, target):
            seen_here = set()
            for each_num in arr:
                the_other = target - each_num
                if the_other in seen_here:
                    return [the_other, each_num]
                seen_here.add(each_num)

    return res

