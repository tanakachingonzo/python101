# Tanaka Chingonzo
# CS100 Homework Due 10/20/17

# 4.1 Create a list with the following five items: 7, 9, 'a', 'cat', False. Assign this list to the variable myList.
myList = [7, 9, "a", "cat", False]

# 4.2 Write Python statements to do the following:

# (a)Append 3.14 and 7 to the list
myList.append(3.14)
myList.append(7)

# (b)Insert the value 'dog' at position 3
myList.insert(3, "dog")

# (c)Find the index of 'cat'.
myList.index("cat")

# (d)Count the number of 7's in the list.
myList.count(7)

# (e)Remove the first 7 from the list.
myList.remove(7)

# (f)Remove 'dog' from the list using pop and index.
myList.pop(myList.index("dog"))

# 4.3 Split the string "the quick brown fox" into a list of words.
'the quick brown fox'.split(' ')

# 4.4 Split the string "mississippi" into a list using the 'i' as the split point
"mississippi".split("i")


# 4.5 Write a function that takes a sentence as a parameter and returns the number of words in the sentence.
def wordCount(t):


    wordList = t.split()
returnlen(wordList)


# 4.6 Although Python provides us with many list methods, it is good practice
# and very instructive to think about how they are implemented.
# Implement a Python function that works like the following:

# (a) count
def myCount(alist, anitem):


    itemcount = 0
for item in alist:
    if item == anitem:
    itemcount = itemcount + 1
return itemcount


# (b) inList – return True if item is in list

def inList(alist, anitem):


    for item in alist:
    if item == anitem:
    return True
return False


# (c) reverse

def myReverse(alist):


    for i i n range(len(alist) −1):
    alist.insert(i, alist.pop())


# (d) find
def find(alist, anitem):


    found = False
loc = 0

while loc < len(alist) and not found:
    if alist[loc] == anitem:
    found = True
else:
loc = loc + 1
if found:
    return loc
else:
return −1


# (e) insert
def myInsert(alist, loc, anitem):


    alist.append(None)
for i in range(len(alist)−2, loc −1, −1):
    alist[i + 1] = alist[i]
alist[loc] = anitem
