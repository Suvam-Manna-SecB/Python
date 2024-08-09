# Find GCD of two numbers.
def gcd(a, b):
    if b == 0:
        return a
    else:
        gcd(b, a%b)

a = int(input('Enter 1st Number: '))
b = int(input('Enter 2nd Number: '))
res = gcd(a, b)
print('GCD of {} and {} = {}'.format(a, b, res))
