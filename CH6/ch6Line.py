from cImage import *
import math

myWin = ImageWin("Class image", 300, 300)
img = EmptyImage(300,300)


blackPixel = Pixel(0,0,0)
redPixel = Pixel(255,0,0)

# diagonal pixels are colored black
for i in range(300):
    img.setPixel(i,i,blackPixel)
    img.setPixel(100,100,redPixel)

#square
for col in range(100, 201):
    img.setPixel(100,col, redPixel)
    img.setPixel(200,col, redPixel)
    for row in range(100, 200):
        img.setPixel(row,100,redPixel)
    


# displays the image
img.draw(myWin)

myWin.exitOnClick()
img.save("classImg.gif")

myWin.exitOnClick()
