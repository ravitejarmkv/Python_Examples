"""
Write a program to check whether a number is Armstrong?
"""
num = 153
order = len(str(num))
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
# Print the output
if num == sum:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
