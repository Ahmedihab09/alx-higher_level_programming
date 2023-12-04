#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    # Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
    return [num % 2 == 0 for num in my_list]
