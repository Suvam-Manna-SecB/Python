# Declare a function named reverse_list. It takes an array as a parameter and
# it returns the reverse of the array (use loops).

def reverse_list(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])

arr = []
n = int(input('Enter The Number of Elements: '))
print('Enter Elements :-')
for i in range(0, n):
    arr.append(int(input()))
reverse_list(arr)
    
