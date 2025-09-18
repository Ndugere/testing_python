def array_maker(a):
    b = [0 for _ in range(len(a))]
    for i in range(len(a)):
        left = a[i - 1] if i > 0 else 0
        right = a[i + 1] if i < len(a) - 1 else 0
        b[i] = left + a[i] + right
    return b 
