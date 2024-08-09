# Declare a function named print_list. It takes a list as a parameter and
# it prints out each element of the list.

def print_list(l):
    for item in l:
        print(item)

l = []
n = int(input('Enter Number of Elements: '))
print('Enter Elements :-')
for i in range(0, n):
    l.append(int(input()))
print_list(l)
    
