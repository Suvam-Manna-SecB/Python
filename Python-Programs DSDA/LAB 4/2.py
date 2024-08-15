# Write a program that accepts a comma separated sequence of words as input and prints the words
# in a comma-separated sequence after sorting them alphabetically.

s = input("Enter a comma separated sequence of words: ")
words = s.split(',')
words = [word.strip() for word in words]
words.sort()
s = ', '.join(words)
print(f"Sorted Words: {s}")
