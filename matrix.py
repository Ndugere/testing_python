def solution(matrix):
    nums = []

    while matrix:
        nums += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                nums.append(row.pop())

        if matrix:
            nums += matrix.pop()[::-1]
        
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                nums.append(row.pop(0))
        
    return nums
        


