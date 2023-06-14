#!/usr/bin/python3

def search_replace(my_list, search, replace):
    replaced_list = []
    for num in my_list:
        if num == search:
            replaced_list.append(replace)
        else:
            replaced_list.append(num)
    return replaced_list
