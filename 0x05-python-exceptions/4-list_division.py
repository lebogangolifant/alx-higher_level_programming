#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for idx in range(list_length):
        try:
            division_result = 0
            if idx < len(my_list_1) and idx < len(my_list_2):
                if type(my_list_1[idx]) in (int, float) and type(my_list_2[idx]) in (int, float):
                    if my_list_2[idx] != 0:
                        division_result = my_list_1[idx] / my_list_2[idx]
                    else:
                        print("division by 0")
                else:
                    print("wrong type")
            elif idx >= len(my_list_1) or idx >= len(my_list_2):
                print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            result.append(division_result)
    return result
