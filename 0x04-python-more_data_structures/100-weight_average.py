#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    divisor = 0
    dividend = 0

    for item in my_list:
        divisor += item[0] * item[1]
        dividend += item[1]

    return divisor / dividend
