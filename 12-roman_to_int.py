def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    prev = 0
    total = 0

    for each_char in reversed(roman_string):
        value = roman_values.get(each_char, 0)
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
        
    return total
