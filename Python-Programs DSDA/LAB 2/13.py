# Write a python program to print the first 6 terms of a geometrc sequence
# starting with 2 and having a common ratio of 3.
import math
a = 2
r = 3
for i in range(1, 7):
    print(a * math.pow(r, i-1))
    
