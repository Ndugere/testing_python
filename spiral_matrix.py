def spiral_matrix(arr: list) -> list:
    res = []

    while arr:
        # top
        res.extend(arr.pop(0))

        # right column
        if arr and arr[0]:
            for row in arr:
                res.append(row.pop())
        
        # bottom most row
        if arr:
            res.extend(arr.pop()[::-1])

        # left column
        if arr and arr[0]:
            for row in reversed(arr):
                res.append(row.pop(0))
    
    return res