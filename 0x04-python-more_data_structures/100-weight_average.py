#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    result_2, result_1 = 0, 0
    mul = 1
    for i in range(len(my_list)):
        mul = my_list[i][0] * my_list[i][1]
        result_1 += mul
        result_2 += my_list[i][1]
    return result_1 / result_2
