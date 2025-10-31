def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    
    new_matrix = []

    for row in matrix:
        new_row = [ x ** 2 for x in row ]

        new_matrix.append(new_row)
    
    return new_matrix
