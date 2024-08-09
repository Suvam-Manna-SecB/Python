# Write a program to generate the Fibonacci series upto n.

n = int(input('Enter n: '))
a = 0
b = 1
while n>0:
    print(a)
    c = a + b
    a = b
    b = c
    n = n - 1
