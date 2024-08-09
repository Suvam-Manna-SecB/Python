# Convert Decimal to binary.
n = int(input('Enter Decimal Number: '))
l = []
while n > 0:
    rem = n%2
    l.append(rem)
    n = n // 2

l = l[::-1]
for i in l:
    print(i, end='')
