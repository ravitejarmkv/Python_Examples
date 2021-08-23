"""
Write a program to determine the factors of a number
"""


def factors(n):
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res


n = 500
print(f"Factors of a {n} are:")
print(factors(n))
