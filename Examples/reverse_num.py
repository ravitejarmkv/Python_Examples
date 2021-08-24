"""
Write a program to reverse a number ?
"""


def reverse_number(number):
    result = str(number)[::-1]
    result = int(result)
    print(f"Original number: {number}")
    print(f"Reverse number: {result}")


num1 = 123456
num2 = 654321
reverse_number(num1)
reverse_number(num2)

# Method 2

rev = 0
while num1 > 0:
    last_digit = num1 % 10
    rev = rev * 10 + last_digit
    num1 = num1 // 10
print(rev)
