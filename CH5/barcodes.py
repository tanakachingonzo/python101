in_File=open(r'hw8BarCodes.txt', 'r')
barcode= in_File.read()
barcode = barcode.split()
    
for i in barcode:
    i= [int(x) for x in i]
    odd = sum(i[0:-1:2])*3
    even= sum(i[1:-1:2])
    print("'Check sum digit:'", i[-1])
    print(10- ((even+odd)%10) == i[-1])