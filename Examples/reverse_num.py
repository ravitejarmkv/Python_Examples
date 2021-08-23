"""
Write a program to reverse a number ?
"""


def reverse_number(number):
    result = str(number)[::-1]
    print(f"Original number: {number}")
    print(f"Reverse number: {result}")


num1 = 123456
num2 = 654321
reverse_number(num1)
reverse_number(num2)
