"""
Write a program to find Fibonacci sequence
"""


def fibonacci_seq(nterms):
    # Program to display the Fibonacci sequence up to n-th term
    
    # first two terms
    n1, n2 = 0, 1
    count = 0
    
    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1


nterms = int(input("How many terms? "))
fibonacci_seq(nterms)

# Using recursive function

# def recur_fib(n):
#     if n <= 1:
#         return n
#     else:
#         return recur_fib(n - 1) + recur_fib(n - 2)
#
#
# nterms = int(input("How many terms: "))
# if nterms <= 0:
#     print("Please enter a positive or non_zero integer")
# else:
#     print("Fibonacci sequence:")
#     for i in range(nterms):
#         print(recur_fib(i))
