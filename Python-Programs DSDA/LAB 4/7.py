# Write a program which accepts a sequence of words separated by whitespace as input to print the
# words composed of digits only.

s = input("Enter a sequence of words: ")
words = s.split()
digitWords = [word for word in words if word.isdigit()]
print(digitWords)
