# Print the pattern upto N lines:

n = int(input('Enter N: '))
for i in range(1,n-1):
    print(' ' * (n-i), end='')
    print('/' + ' ' * (2 * i - 2) + '\\')
print('/' + '_' * (2 * n - 2) + '\\')
