"""
Write a program to check whether two strings are anagrams
"""


def check(n1, n2):
    if len(n1) == len(n2):
        if sorted(n1.lower()) == sorted(n2.lower()):
            print("The strings are anagrams.")
        else:
            print("The strings aren't anagrams.")
    else:
        print("The strings aren't anagrams.")


m1 = "state"
m2 = "slate"

n1 = "State"
n2 = "Taste"

check(m1, m2)
check(n1, n2)
