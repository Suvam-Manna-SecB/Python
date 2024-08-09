# Write a program to generate prime number series upto n.

def isPrime(num):
    for i in range(2, num):
        if num%i==0:
            return False
    return True

n = int(input('Enter the value of n: '))
print('Prime Numbers:-')
for i in range(2, n+1):
    if isPrime(i):
        print(i)
