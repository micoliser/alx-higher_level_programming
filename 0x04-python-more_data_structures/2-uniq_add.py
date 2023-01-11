#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        uniq_list = list(set(my_list))
        result = 0
        for num in uniq_list:
            result += num

        return result
