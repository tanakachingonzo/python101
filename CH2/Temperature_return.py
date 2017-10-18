def Celsius(tempF):
    result = (tempF-32)*(5.0/9)
    # tempF= int(input( "Input temperature in Fahrenheit:" ))
    return result


x = Celsius(32)
print( "Orig temp. is :", x)
x = x+20
print( "Temp. 1 degree warmer is :", x+1)

