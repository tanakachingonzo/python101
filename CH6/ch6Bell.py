from cImage import *

myWin = ImageWin("Img", 300, 300)
img = FileImage("mickey.gif")

width= img.getWidth()
height= img.getHeight()
print(width, height)

newColor= Pixel(0,0,205)

for row in range(height):
    for col in range(width):
        colorOfPixel= img.getPixel(row,col)
        if colorOfPixel[0]> 180 and colorOfPixel[1] > 100:
            img.setPixel(row,col,newColor)
        #print img.getPixel(r,c)[0]
#print "\n"

img.draw(myWin)

myWin.exitOnClick()