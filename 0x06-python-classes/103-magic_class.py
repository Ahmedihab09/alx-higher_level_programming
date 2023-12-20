#!/usr/bin/python3 

'''Magic Class'''


import math

class MagicClass:
    ''''Class MagicClass'''
    def __init__(self, radius=0):
        """Initialize MagicClass"""
        self.__radius = 0

        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        '''Calculate area of a circle'''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        '''Calculate circumfrence of a circle'''
        return 2 * math.pi * self.__radius

