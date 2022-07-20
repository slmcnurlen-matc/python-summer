#!/usr/bin/env python3
"""
Sam NcNurlen
This script uses a function to convert a temperature from Fahrenheit to Celsius.
"""

def convert_temp(degrees_fahrenheit):
    return int((degrees_fahrenheit - 32) * 5 / 9)

degrees_celsius = convert_temp(32)
print(degrees_celsius)