"""
Write a program to check whether a string is palindrome ?
"""


def reverse_str(text):
    str_ing = ''
    for i in text:
        str_ing = i + str_ing
    return str_ing

def is_palindrome(string):
    string = string.lower()
    if string == reverse_str(string):
        print(f"Given String({string}) is a palindrome")
    else:
        print(f"Given string({string}) is not a palindrome")
string1 = 'Pop'
string2 = 'Malayalam'
string3 = "Python"

is_palindrome(string1)
is_palindrome(string2)
is_palindrome(string3)

# Method 2
def palindrom(word):
    if word.lower() == word[::-1].lower():
        print(f"Given String({word}) is a palindrome")
    else:
        print(f"Given string({word}) is not a palindrome")
word1 = 'Pop'
word2 = 'Malayalam'
word3 = "Python"
palindrom(word1)
palindrom(word2)
palindrom(word3)
