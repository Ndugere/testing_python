def multiply_list_map(my_list=[], number=0):
    def multiply(n):
        return n * number
    new_list = list(map(multiply, my_list))
    return new_list