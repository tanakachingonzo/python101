# creating list of winning lottery codes
import random

winners = []
for i in range(4):
    winners.append(random.randint(0, 9))
print(winners)

# code to create user guesses
myTickets = []
for i in range(4):
    ticket = input("Enter ticket number:")
    myTickets.append(int(ticket))
print("Your ticket:", myTickets)

# testing user guesses against winning range
numCorrect = 0
for i in range(4):
    if myTickets[i] in winners:
        numCorrect = numCorrect + 1
if numCorrect < 4:
    print("Your tickets lost")
    print("Your ticket:", myTickets)
else:
    print("You win")
