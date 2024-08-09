# Write a python script that displays the following table.
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for j in range(1, 6):
    print(str(j) + ' ' + str(1) + ' ' + str(j) + ' ' + str(j**2) + ' ' + str(j**3))
        
