"""
Write a program to Reverse a string
"""
text = 'Reverse a string'
print("Original string: {}".format(text))
print("Method 1")
print(text[::-1])

print("Method 2")

n = len(text)-1
s = []
for i in text:
    s.append(text[n])
    n = n - 1
print("".join(s))

print("Method 3")
def reverse_str(text):
    str_ing = ''
    for i in text:
        str_ing = i + str_ing
    return str_ing


print(reverse_str(text))
