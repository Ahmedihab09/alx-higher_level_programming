#!/usr/bin/python3
def pow(a, b):
    res = 1
    for i in range(b+1):
        res *= a
    return res
