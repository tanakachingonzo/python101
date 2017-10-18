import random 

def tossCoin():
    i= random.random()
    if i>= 0.50:
        coin="head"
    else:
        coin="tail"
    return coin
    
noOfTosses = 1000000
noOfHeads = 0
for i in range(noOfTosses):
    coin = tossCoin()
    if(coin == "head"):
        noOfHeads = noOfHeads +1
print( "No. of heads: ", noOfHeads )
print( "No. of tails: ", noOfTosses - noOfHeads )    
