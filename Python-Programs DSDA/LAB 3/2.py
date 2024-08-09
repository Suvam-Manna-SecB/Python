# Write a function called calculate_scope which return the slope of
# a linear equation.

import sys
def calculate_scope(x1, y1, x2, y2): 
    if(x2 - x1 != 0): 
      return (float)(y2-y1)/(x2-x1) 
    return sys.maxsize

x1 = int(input('Enter x1: '))
y1 = int(input('Enter y1: '))
x2 = int(input('Enter x2: '))
y2 = int(input('Enter y2: '))
print("Slope is: ", calculate_scope(x1, y1, x2, y2)) 
