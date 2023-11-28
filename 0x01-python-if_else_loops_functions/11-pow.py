#!/usr/bin/python3
def pow(a, b):
    # Base case: any number to the power of 0 is 1
    if b == 0:
        return 1

    # Initialize result to the base
    result = a

    # Multiply the result by base 'b' times
    for _ in range(1, abs(b)):
        result *= a

    # If the exponent is negative, take the reciprocal
    if b < 0:
        result = 1 / result

    return result
