in_File=open(r'ch5rainfall.txt', 'r')
out_File = open(r'resukts.txt', 'w')


for line in in_File:
    list21 = line.split(" ")
    # print( list21 )
    out_File.write(list21[0]+" " + "has this much rain:"+ list21[1] + "\n")
out_File.write("City with max rain:" + "+maxRainCity+" + "\n")



in_File.close()
out_File.close()