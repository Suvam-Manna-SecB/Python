# Write a program that accepts sequence of lines as input and prints the lines after making all
# characters in the sentence capitalized.

lines = []
print("Enter a sequence of lines (press Enter on an empty line to finish):")
while True:
    line = input()
    if line == '':
        break
    lines.append(line)
    
for line in lines:
    print(line.upper())
