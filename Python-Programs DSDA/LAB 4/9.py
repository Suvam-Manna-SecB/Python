''' 
Write a program that accepts a string
I. reverses it.
II. checks whether it is a palindrome.
III. checks whether it ends with a specific substring.
IV. capitalize the first letter of each word in a string
V. check if a string is anagram of another string
VI. remove vowels from string
VII. find length of the longest word in a sentence
'''

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return s == s[::-1]

def ends_with(s, substring):
    return s.endswith(substring)

def capitalize_words(s):
    return s.title()

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

def longest_word_length(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return len(longest_word)

input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print(f"Reversed string: {reversed_string}")

palindrome_check = is_palindrome(input_string)
print(f"String is palindrome?: {palindrome_check}")

substring = input("Enter the substring to check if it is at the end of the string: ")
ends_check = ends_with(input_string, substring)
print(f"String ends with: '{substring}': {ends_check}")

capitalized_string = capitalize_words(input_string)
print(f"Capitalized Words String: {capitalized_string}")

anagram_string = input("Enter another string to check if it is an anagram of the first string: ")
anagram_check = are_anagrams(input_string, anagram_string)
print(f"String are anagrams: {anagram_check}")

no_vowels_string = remove_vowels(input_string)
print(f"String without vowels: {no_vowels_string}")

sentence = input("Enter a sentence to find the length of the longest word: ")
longest_length = longest_word_length(sentence)
print(f"Length of the longest word: {longest_length}")
