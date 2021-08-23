"""
Write a program to calculate the number of numerical digits in a string
"""


def digits_in_string(text):
    count = 0
    for i in text:
        if i.isdigit():
            count += 1
    print(count)


text = 'I have 2 apple, 4 oranges and 1 chocolate.'
digits_in_string(text)
