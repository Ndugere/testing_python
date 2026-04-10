def number_nums(nums: list) -> tuple:
    x, y, h, w = None, None, 0, 0
    for i, row in enumerate(nums):
        if 0 in row:
            if y is None:  
                y = i
            zero_indices = [j for j, val in enumerate(row) if val == 0]
            left, right = min(zero_indices), max(zero_indices)
            if x is None:
                x = left
            w = max(w, right - x + 1)
            h += 1
    return (x, y), h, w
