def int_to_roman(num):
    if not isinstance(num, int) or num < 1 or num > 3999:
        return ""
    
    value_map = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    
    result = []
    
    for value, roman in value_map:
        while num >= value:
            result.append(roman)
            num -= value
    
    return "".join(result)
