#1) (3pts) Write a Python program that prints the frequencies of words in the text file hw8Text.txt. 
#Your output should be similar to the one shown below (same alignments and table-like format). 
#Submit your (1) program and (2) a snapshot (picture of at least first 7 words in your table) of your results.

in_File=open(r'hw8Text.txt', 'r')
word= "it"
freq= in_File.count(word)
print(freq)



