# Write a program to compute cosine of x. The user should supply x and a
# positive integer n. we compute the cosine of x using the series and the
# computation should use all terms in the series up through the term involving
# xn, cos x = -1 - x^2/2! + x^4/4! - x^6/6! ....

import math
def cal(x, n):
    ans = 0
    for i in range(1, n+1):
        if i%2 != 0:
            ans = ans - math.pow(x, i*2 - 2) / math.factorial(i * 2 - 2)
        else:
            ans = ans + math.pow(x, i*2-2) / math.factorial(i*2-2)
    return ans

x = float(input('Enter value of x: '))
n = int(input('Enter value of n: '))
print('cos {} = {}'.format(x, cal(x, n)))
