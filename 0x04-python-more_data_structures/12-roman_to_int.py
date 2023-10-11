#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    r = {"I": 1, "V": 5, "X": 10, "L": 50,
         "C": 100, "D": 500, "M": 1000}
    total = 0
    itr = 0
    flag = 0
    for i in range(len(roman_string)):
        itr = i + 1
        if flag == 1:
            flag = 0
            continue
        cur = roman_string[i]
        if itr < len(roman_string) and r.get(roman_string[itr]) > r.get(cur):
            nex = roman_string[itr]
            total += int(r.get(nex) - r.get(cur))
            flag = 1
        else:
            total += int(r.get(roman_string[i]))
    return int(total)
