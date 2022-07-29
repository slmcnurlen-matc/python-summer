#!/usr/bin/env python3
"""
Sam McNurlen
This script imports a function from another file.
"""

import f2c

degrees_fahrenheit = input("Enter the temperature in Fahrenheit: ")
degrees_celsius = f2c.convert_temp(int(degrees_fahrenheit))
print(f"The temperature in Celsius is {degrees_celsius}")