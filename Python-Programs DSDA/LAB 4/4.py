# Write a program that accepts a sequence of whitespace separated words as input and prints the
# words after removing all duplicate words and sorting them alphanumerically.

s = input("Enter a sequence of whitespace separated words: ")
words = s.split()
unique = list(set(words))
unique.sort()
s = ' '.join(unique)
print(f"Output: {s}")
