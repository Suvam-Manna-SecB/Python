# Print the seres upto N terms: 1,2,6,24,120,720
n = int(input('Enter Number of Terms: '))
val = 1
for i in range(1, n+1):
    val = val * i
    if i == n:
        print(val)
    else:
        print(val,end=', ')
