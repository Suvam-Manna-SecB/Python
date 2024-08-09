# Compute the sum up to n terms in the series
# 1 - 1/2 + 1/3 - 1/4 + 1/5 - .... 1 / n where n is positive integer.

def cal(n):
    total = 0
    for i in range(1, n+1):
        if i%2 == 0:
            total = total - 1/i
        else:
            total = total + 1/i
    return total

n = int(input('Enter N: '))
print('Answer: ', cal(n))
