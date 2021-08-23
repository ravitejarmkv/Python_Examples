"""
Write a program to determine the largest and the smallest element of an array which is not sorted
"""

array = [55, 4, 9, 2, 5, 8, 9, 7, 19, 23]
small = array[0]
large = array[1]
for i in array:
    if i < small:
        small = i
    elif i > large:
        large = i
print(small)
print(large)

# method 2
print(min(array))
print(max(array))