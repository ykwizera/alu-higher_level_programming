#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    sum_r = 0
    var = 0
    for symbol in reversed(roman_string):
        value = roman_symbols.get(symbol)
        if value is None:
            return 0
        if value < var:
            sum_r -= value
        else:
            sum_r += value
        var = value
    return sum_r
