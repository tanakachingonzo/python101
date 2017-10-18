#Tanaka Chingonzo

#EXERCISE 1
#Pg. 89: 3.1 - 3.7 (Note: make sure you write the Python code and the output it generates)

#3.1 Create a string variable that is initialized to your entire name--first, middle, and last.

# full_name="Tanaka Gregory Chingonzo"

# 3.2 Using the slice operator, print your first name.

# full_name="Tanaka Gregory Chingonzo"
# print(full_name[:6])
# Tanaka

# 3.3 Using the slice operator, print your last name.

# full_name="Tanaka Gregory Chingonzo"
# print(full_name[-9:])
# Chingonzo

# 3.4 Using the slice and concatenation operators, print your name in the
# form “Lastname, Firstname.”

# full_name="Tanaka Gregory Chingonzo"
# print(full_name[-9:] + ', ' + full_name[:6])
# Tanaka Chingonzo


# 3.5 Print the length of your first name.

# full_name="Tanaka Gregory Chingonzo"
# print(full_name[:6].__len__())
# 6

# 3.6 Assume you have two variables: s='s', and p='p'. Using concatenation
# and repetition, write an expression that produces the string
# mississippi.

# s="s"
# p="p"
#
# print('mi'+s*2+'i'+s*2+'i'+p*2+'i')

# 3.7 Modify the prefix example in Session 3.5 to print all prefixes of “Roy
# G Biv,” including the entire string.

# for ch in range(len('Roy G. Biv')+1):
#     print('Roy G. Biv'[:ch])
#
#     Roy
#     Roy
#     Roy    G
#     Roy    G.
#     Roy    G.
#     Roy    G.B
#     Roy    G.Bi
#     Roy    G.Biv


# EXERCISE 2
# Pg. 91: 3.8 - 3.11 (Note: make sure you write the Python code and the output it generates)

#3.8 Using the count method, find the number of occurrences of the character `s' in the string 'mississippi'.

# river= "mississippi"
# print(river.count("s"))
# 4

#3.9 Replace all occurrences of the substring 'iss' with 'ox'.

# river= "mississippi"
# newriver = river.replace("iss","ox")
# print(newriver)
# moxoxippi

#3.10 Find the index of the first occurrence of 'p' in 'mississippi'.

# river= "mississippi"
# print(river.index('p'))

#3.11 Make the word 'python' centered and all capital letters in a string of length 20.

# word = "python"
# print(word.upper().center(20))
#       PYTHON

#EXERCISE 3
# Pg. 93: 3.12 - 3.16
# Notes:
# Pb. 3.13 example: my_function('3') returns 3.
# Pb. 3.14 SHOULD read as "Write the letterToIndex function using ord". Example: letterToIndex('a') must return 0.
# Pb. 3.15 SHOULD read as "Write the indexToLetter function using chr". Example: indexToLetter(2) must return 'c'.

#3.12 What is the difference between ord('A') and ord('a')?

#ord('a') gives 97 whereas ord('A') gives 65

#3.13Write a function that takes a single character digit and returns its integer value.

def intval(i):
    i = int(i)
    return i

intval(10)

#3.14 Write the letterToIndex function using ord and chr.

# def letterToIndex(ch):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     ch = ord(ch)
#     num = chr(ch)

# return alphabet.find(num)

#3.15 Write the indexToLetter function using ord and chr
# def index2letter(index):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     letters = ''
#     num = 97
#     a = index + num
#     for x in alphabet:
#         letters = letters + "," + str(ord(x))
#     b = ''
#     if str(a) in letters:
#         b = chr(int(a))
#     return b

#3.16 Write a function that takes an exam score from 0­100 and returns the corresponding letter grade.
#  Use the same grading scale your professor does for this class.

# def grade():
#     mark = input("Enter your score: ")
#     score = int(mark)
#     if score >= 95:
#         lettergrade = "A"
#     elif score >= 94 or score >= 90:
#         lettergrade = "A-"
#     elif score >= 89 or score >= 88:
#         lettergrade = "B+"
#     elif score >= 87 or score >= 83:
#         lettergrade = "B"
#     elif score >= 82 or score >= 80:
#         lettergrade = "B-"
#     elif score >= 79 or score >= 78:
#         lettergrade = "C+"
#     elif score >= 77 or score >= 73:
#         lettergrade = "C"
#     elif score >= 72 or score >= 70:
#         lettergrade = "C-"
#     elif score >= 69 or score >= 68:
#         lettergrade = "D+"
#     elif score >= 67 or score >= 63:
#         lettergrade = "D"
#     elif score >= 62 or score >= 60:
#         lettergrade = "D-"
#     elif score <= 59:
#         lettergrade = "F"
#     return lettergrade