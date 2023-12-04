#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # If idx is negative or out of range, nothing changes (returns the same list)
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Delete the element at the specified index in the original list
    del my_list[idx]
    return my_list
