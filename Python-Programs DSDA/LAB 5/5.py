'''
From the above sets A and B
I. Join A and B
II. Find A intersection B
III. Is A subset of B
IV. Are A and B disjoint sets
V. Join A with B and B with A
VI. What is the symmetric difference between A and B
VII. Delete the sets completely
'''

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

join_A_B = A.union(B)
print(f"Join A and B: {join_A_B}")

intersection_A_B = A.intersection(B)
print(f"A intersection B: {intersection_A_B}")

is_subset = A.issubset(B)
print(f"Is A a subset of B: {is_subset}")

are_disjoint = A.isdisjoint(B)
print(f"Are A and B disjoint sets: {are_disjoint}")

join_A_B_alt = B.union(A)
print(f"Join B with A: {join_A_B_alt}")

symmetric_diff_A_B = A.symmetric_difference(B)
print(f"Symmetric difference between A and B: {symmetric_diff_A_B}")

del A
del B
