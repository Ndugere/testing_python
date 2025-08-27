def search_complement(arr, target):
    index_numb = {}

    for i, num in enumerate(arr):
        complement = target - num

        if complement in index_numb:
            return [index_numb[complement], i]
        
        index_numb[num] = i

    return -1
