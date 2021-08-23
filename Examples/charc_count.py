"""
Write a program to find the number of occurrences of a particular character in a string
"""


def character(char, text):
    res = 0
    for i in text:
        if char == i:
            res += 1
    print("The number of occurrences of a '{}' character in a given string: {}".format(char,res))


char = 'r'
text = 'the man with golden heart went to bank to get a loan on his heart but rejected, Why?'
character(char, text)
