def square_matrix_map(matrix=[]):
    
    def multiply(n):
        return n * n

    def each_list(lst):
        return list(map(multiply, lst))
    
    return list(map(each_list, matrix))
