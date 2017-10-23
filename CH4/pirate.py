# w= 'hello madam'
# print(toPirate(w))
#
# toPirate=['hello','excuse','sir','boy','man','madam','officer''officer','the']
# English=['avast','arrr','matey']

pirate = {
'hello':'avast'
'sir':'matey'
'excuse':'arr'
'me':'me'}
phrase= "hello sir excuse"
split_phrase=phrase.split(" ")
print(split_phrase)

rez=""
for word in split_phrase:
    if word in pirate:
        rez= rez+ pirate[word]+ " "

print(rez)