# name= "Diana"
# age=21.5
# noOfPets=4
# print("%s is %.2f years old and has %d pets." %(name, age, noOfPets))

#%s is for strings. %d is for integers

file_in= open(r"cities.txt", 'r')
file_out= open(r"output.txt", 'w')

for line in file_in:
    print(line)

for line in file_out:
    list33= line.split(" ")
    print(list33)

file_in.close()
file_out.close()

