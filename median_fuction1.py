def median_function(nums1: list, nums2: list) -> float:
    merged_list = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            merged_list.append(nums1[i])
            i += 1
        else:
            merged_list.append(nums2[j])
            j += 1

    merged_list.extend(nums1[i:])
    merged_list.extend(nums2[j:])

    n = len(merged_list)
    mid = n // 2

    if n % 2 == 0:
        return (merged_list[mid - 1] + merged_list[mid]) / 2
    else:
        return merged_list[mid]