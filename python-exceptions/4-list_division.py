#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length

    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and isinstance(my_list_2[i], (int, float)):
                if my_list_2[i] == 0:
                    result[i] = 0
                    print("division by 0")
                else:
                    result[i] = my_list_1[i] / my_list_2[i]
            else:
                result[i] = 0
                print("wrong type")
        except IndexError:
            print("out of range")
            break

    return result
