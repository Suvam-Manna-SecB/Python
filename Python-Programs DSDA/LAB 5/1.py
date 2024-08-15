'''
1.The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
I. Sort the list and find the min and max age
II. Add the min age and the max age again to the list
III. Find the median age (one middle item or two middle items divided by two)
IV. Find the average age (sum of all items divided by their number )
V. Find the range of the ages (max minus min)
VI. Compare the value of (min - average) and (max - average), use _abs()_ method
'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print(f"Sorted ages: {ages}")
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")

ages.append(min_age)
ages.append(max_age)
print(f"Updated ages: {ages}")

n = len(ages)
if n % 2 == 1:
    median_age = ages[n // 2]
else:
    median_age = (ages[n // 2 - 1] + ages[n // 2]) / 2
print(f"Median age: {median_age}")

average_age = sum(ages) / len(ages)
print(f"Average age: {average_age}")

age_range = max_age - min_age
print(f"Range of ages: {age_range}")

min_minus_avg = abs(min_age - average_age)
max_minus_avg = abs(max_age - average_age)
print(f"Absolute value of (min - average): {min_minus_avg}")
print(f"Absolute value of (max - average): {max_minus_avg}")
