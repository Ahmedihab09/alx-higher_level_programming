#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            value = my_list[i]
            if type(value) == int:
                print("{:d}".format(value), end=" ")
                count += 1
        print()
        return count
    except (IndexError, ValueError, TypeError) as e:
        if "list index out of range" in str(e):
            print("Error: {}".format(e))
            return count
        else:
            raise e
