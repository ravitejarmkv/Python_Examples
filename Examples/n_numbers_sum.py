"""
Write a program to calculate sum of numbers from 1 to n
"""


def sum_of_numbers(n):
    num = 0
    for i in range(1, n + 1):
        num = num + i
    print(f'Using loops calculating sum of numbers from 1 to n is:{num}')


n = 100
sum_of_numbers(n)


# Recursive method

def num_sum(num):
    if num == 1:
        return 1
    else:
        return num + num_sum(num - 1)

res = num_sum(100)
print("Using recursive sum of numbers from 1 to n is:{}".format(res))
