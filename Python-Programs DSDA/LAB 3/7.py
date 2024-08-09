# Write a program to compute sin x for given x. The user should supply x and
# a positive integer n. We compute the sine of x using the series and the
# computation should use all terms in the series up through the term involving x
# sin x = x - x^3/3! + x^5/5! - x^7/7! + x^9/9! .....
import math
def cal(x, n):
    ans = 0
    for i in range(1, n+1):
        if i%2 == 0:
            ans = ans - math.pow(x, i*2 - 1) / math.factorial(i * 2 - 1)
        else:
            ans = ans + math.pow(x, i*2-1) / math.factorial(i*2-1)
    return ans

x = float(input('Enter value of x: '))
n = int(input('Enter value of n: '))
print('sin {} = {}'.format(x, cal(x, n)))
              

