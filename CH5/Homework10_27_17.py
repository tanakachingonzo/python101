# 1) (2pts) Give a program segment that prompts for two english words, and determines if
# all the letters of first word are within the second. For example, if my words are 'car' and 'race',
# your program prints "True", because all lettters from the first word are found in the second word;
# for the words 'bear' and 'abrupt', your program prints "False", because "e" from the first word is not
# found in the second word;

# word1=input("Enter word")
# word2=input("Enter word 2")
#
# for i in word1:
#     if not (i in word2):
#         print(False)
#     else:
#         print(True)

# 2) (2pts) Write a Python function named count_vowels(my_string), which receives a string and prints out
# a dictionary having the counts of all vowels. For example, a function call such as count_vowels("I like pie")
# will generate the following print out: {'i': 3, 'e':2'}.

# def count_vowels(myWord):
#     temp={}
#     vowelCount={}
#     alf="aeiou"
#     for i in alf:
#         temp[i]=0
#         for x in myWord:
#             if(i==x):
#                 temp[i]=temp[i]+1
#     for i in temp:
#         if (temp.get(i)!=0):
#             vowelCount[i]=temp.get(i)
#     print(vowelCount)
#
# myStr=input("Enter a word:  ")
# count_vowels(myStr)


# 3) (2pts) Write a function named moderate_days(my_dict) which receives a dictionary of seven temperatures each
# corresponding to a day of the week, and returns a list of the days in which the temperatures where between 70 and
# 79 degrees. For example, for a function call moderate_days({'M':56, 'T':75, 'W':89, 'Th':72, 'F':100, 'S':23, 'Su':77),
# your function returns the list ['T', 'Th', 'Su']

# days={'Monday':80, 'Tuesday':76, 'Wednesday':74, 'Thursday':88, 'Friday':86, 'Saturday':84, 'Sunday':79}
# print ("cold weather is: ")
# def moderate_days(my_temp_dict):
#     mDays=[]
#     for i in my_temp_dictt:
#         if (my_temp_dict.get(i)>70 and my_temp_dict.get(i)<=79):
#             mDays.append(i)
#     print(mDays)
#
# moderate_days(days)

# 4) (4pts) Reverse Phone Spelling Program
# Create a function name reverse_phone() that allows the user to enter a spelled phone number for the last four digits
# and returns the phone number that produces that spelling. For example, if I enter '410-555-book', the function will
# return '410-555-2665".
# Hint 1: the number 2 corresponds to "abc"; 3 corresponds to "def"; ....; 7 corresponds to 'pqrs'; ...; 9 corresponds
# to "wxyz". Hint 2: you may use dictionaries to hold the key:values from above.

#
# inttoLetter={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
# def reverse_phone():
#     digits=""
#     nums=[]
#     phone= str(input("Enter a phone number:"))
#     digits=phone[-1:]
#     for i in digits:
#         for x in inttoLetter:
#             if (i in inttoLetter.get(x)):
#                 nums.append(x)
#     digits="".join(map(str, nums))
#
#     print(phone[:-1], digits)
#
# reverse_phone()