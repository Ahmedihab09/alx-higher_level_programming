#!/usr/bin/python3

def fizzbuzz():
    for i in range(101):
        if i % 3 == 0:
            print("fuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        else:
            print(i)
