# Write a program which count and print the numbers of each character in a string input by console.

from collections import Counter
s = input("Enter a string: ")
characterCount = Counter(s)
for char, count in sorted(characterCount.items()):
    print(f"{char},{count}")
