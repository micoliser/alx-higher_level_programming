#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list) == 0:
        return None
    else:
        new_list = list(map(lambda x: replace if x == search else x, my_list))
        return new_list
