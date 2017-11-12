#1) (3pts) Write a Python program that prints the frequencies of words in the text file hw8Text.txt. 
#Your output should be similar to the one shown below (same alignments and table-like format). 
#Submit your (1) program and (2) a snapshot (picture of at least first 7 words in your table) of your results.




def wordFreqency():
	
    infile= open(r'hw8Text.txt', 'r')
    aline= infile.read()

    splitwords = aline.split(" ")
    wordlist = {}
	
    for i in splitwords:
        if i in wordlist:
            wordlist[i]= wordlist[i]+1
        else: wordlist[i]= 1
        
    title="Word"
    freq= "Frequency"
    print("%-20s  %+20s" %(title, freq))
    for x in wordlist:
        space = ("_"*40)
        print("%-20s %+20s \n%s"%(x, wordlist[x], space))	
	
wordFreqency()
