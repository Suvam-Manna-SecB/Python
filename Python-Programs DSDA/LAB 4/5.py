# Write a program that accepts a sentence and calculate the number of letters and digits.

s = input("Enter a sentence: ")
letterCount = 0
digitCount = 0

for char in s:
    if char.isalpha():
        letterCount += 1
    elif char.isdigit():
        digitCount += 1

print(f"LETTERS {letterCount}")
print(f"DIGITS {digitCount}")
