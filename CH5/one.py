in_File=open(r'ch5rainfall.txt', 'r')
out_File = open(r'resukts.txt', 'w')

x=[]
for line in in_File:
    list21 = line.split(" ")
    # print( list21 )
    out_File.write(list21[0]+" " + "has this much rain:"+ list21[1] + "\n")
    x.append(float(list21[1]))

maximumval =str(max(x))
minimumval =str(min(x))

out_File.write("City with max rain:" + maximumval + "\n")
out_File.write("City with min rain:" + minimumval + "\n")

in_File.close()
out_File.close()