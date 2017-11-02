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

a= 3.97777
b=54

#print a in a 20-character space, right aligned, and with 22 decimals.
print("a is %20.2f and b is %d" %(a,b))

#print a ina  20-character space, left aligned, and with two decimals, in the same row print b.
print("a is %-20.2f and b is %d")

#print a in a 20-character space, right aligned with 2 decimals, and fill in with leading zeros.
print("%020.2f" %(a) )

