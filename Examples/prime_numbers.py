def numbers(lower, upper):
    lis = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                lis.append(num)
    
    return lis


class Prime_Numbers:
    pass


lower = 1
upper = 100

print(numbers(lower, upper))
