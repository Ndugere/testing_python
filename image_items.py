def image_items(nums: list) -> str:
    first_row, last_row = None, None
    first_col, last_col = None, None
    
    for i, row in enumerate(nums):
        for j, col in enumerate(row):
            if col == 0:
                if first_row is None:
                    first_row = i
                if last_row is None or i > last_row:
                    last_row = i
                if first_col is None or j < first_col:
                    first_col = j
                if last_col is None or j > last_col:
                    last_col = j
    
    if first_row is None:  # no zeros found
        return "No image is found!"

    height = (last_row - first_row) + 1
    width = (last_col - first_col) + 1

    return f"row: {first_row + 1}, col: {first_col + 1}, width: {width}, height: {height}"
