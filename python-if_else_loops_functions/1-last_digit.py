#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
last_digit =int(number_str[-1])
number_i=int(number_str)
if number_i < 0 and last_digit != 0:
        print(f"Last digit of {number_str} is -{last_digit} and is less than 6 and not 0")
elif last_digit < 6 and last_digit != 0:
        print(f"Last digit of {number_str} is {last_digit} and is less than 6 and not 0")
elif last_digit > 5:
    print(f"Last digit of {number_str} is {last_digit} and is greater than 5")
else:
    print(f"Last digit of {number_str} is {last_digit} and is 0")
