"""
Write a program to calculate the number of vowels and consonants in a string?
"""
words = "Python is an interpreted high-level general-purpose programming language. " \
       "Its design philosophy emphasizes code readability with its use of significant indentation. " \
       "Its language constructs as well as its object-oriented approach aim to help programmers write clear, " \
       "logical code for small and large-scale projects"
text = words.lower()
vowels = ['a', 'e', 'i', 'o', 'u']
v_count = 0
c_count = 0
for i in text:
    if i in vowels:
        v_count += 1
    else:
        c_count += 1
print("Number of vowels: {}\nNumber of consonants: {}".format(v_count, c_count))
print("Total number of words: {}".format(len(text)))