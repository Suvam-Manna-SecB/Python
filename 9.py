# Write a program to check whether number is:
# (a) Perfect Number.
# (b) Armstrong Number.

num = int(input('Enter Number: '))
copy = num
sum = 0
cubeSum = 0
for i in range(1, num):
    if num%i==0:
        sum = sum + i

while num>0:
    rem = num%10
    cubeSum = cubeSum + rem**3
    num = num/10

num = copy

if num==sum:
    print('Perfect Number')
else:
    print('Not a Perfect Number')

if num==cubeSum:
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
