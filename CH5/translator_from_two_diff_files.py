in_File=open(r'hw8PirateInput.txt', 'r')
out_File = open(r'hw8PirateOutput.txt', 'w')

pirate = {
"hello":"avast",
"excuse":"arr",
"sir":"matey",
"boy":"matey",
"man":"matey",
"madam":"proud beauty",
"officer":"foul blaggart",
"the":"th'",
"my":"me",
"your":"yer",
"is":"be",
"are":"be",
"restroom":"head",
"restaurant":"galley",
"hotel":"fleabag inn"}

phrase= in_File.read()
phrase=phrase.split()

rez=""
for word in phrase:
    if word in pirate:
        word1= pirate.get(word)
    else:
        word1=word
    rez=rez+word1+" "

out_File.write(rez)
in_File.close()
out_File.close()
