'''
Create fruits, vegetables and animal products tuples.
I. Join the three tuples and assign it to a variable called food_stuff_tp.
II. Change the about food_stuff_tp tuple to a food_stuff_lt list
III. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
IV. Slice out the first three items and the last three items from food_staff_lt list
V. Delete the food_staff_tp tuple completely
'''

fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'broccoli', 'spinach')
animal_products = ('milk', 'cheese', 'butter')

food_stuff_tp = fruits + vegetables + animal_products
print(f"Combined tuple (food_stuff_tp): {food_stuff_tp}")

food_stuff_lt = list(food_stuff_tp)
print(f"Converted list (food_stuff_lt): {food_stuff_lt}")

n = len(food_stuff_lt)
if n % 2 == 1:
    middle_item = food_stuff_lt[n // 2]
    print(f"Middle item: {middle_item}")
else:
    middle_items = food_stuff_lt[n // 2 - 1 : n // 2 + 1]
    print(f"Middle items: {middle_items}")

first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(f"First three items: {first_three_items}")
print(f"Last three items: {last_three_items}")

del food_stuff_tp
