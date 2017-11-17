from cImage import *

def sepiaPixel(oldPixel):
    newRed= int((oldPixel.getRed() * 0.393) + (oldPixel.getGreen() * 0.769) + (oldPixel.getBlue() * 0.189))
    newGreen= int((oldPixel.getRed() * 0.349) + (oldPixel.getGreen() * 0.686) + (oldPixel.getBlue() * 0.168))
    newBlue= int((oldPixel.getRed() * 0.272)+ (oldPixel.getGreen() * 0.534) + (oldPixel.getBlue() * 0.131))

if  newRed < 0:
    newRed = 0
if newRed > 255:
    newRed = 255

if newGreen < 0:
    newGreen=0
if newGreen > 255:
    newGreen=255

if newBlue < 0:
    newBlue = 0
if newBlue > 255:
    newBlue = 255
        

# created by S. Visa
# if the pixel received is yellow, it returns a blue pixel,
# otherwise it returns the old pixel
def changeYellowToBlue(oldPixel):
    if oldPixel.getRed() > 180 and oldPixel.getGreen() > 180 and \
    oldPixel.getBlue() < 130:
        newPixel = Pixel(0,0,255) 
    else:
        newPixel = oldPixel
    return newPixel

# takes a pixel and returns its reverse 
def negativePixel(oldPixel):
    newred = 255 - oldPixel.getRed()
    newgreen = 255 - oldPixel.getGreen()
    newblue = 255 - oldPixel.getBlue()
    newPixel = Pixel(newred, newgreen, newblue)
    return newPixel

# takes a pixel and returns its gray-scale correspondent 
# def grayPixel(oldpixel):
    # students can complete this


# takes a pixel and returns its sepia-tone correspondent
# def sepiaPixel(oldpixel):
    # students can complete this


# takes an image and a pixel mapping function
# and returns a new image with the pixels changed by the mapping function 
def pixelMapper(oldimage,rgbFunction):
    width = oldimage.getWidth()          
    height = oldimage.getHeight()
    newim = EmptyImage(width,height)     

    for row in range(height):
        for col in range(width):
            originalPixel = oldimage.getPixel(col,row)
            newPixel = rgbFunction(originalPixel)          
            newim.setPixel(col,row,newPixel)
    return newim

# takes an image, displays it, creates a new image by changing pixels of the 
# old image, and displays the new image next to the old image   
def generalTransform(imageFile):
    myimagewindow = ImageWin("Image Processing",600,200)
    oldimage = FileImage(imageFile)
    oldimage.draw(myimagewindow)
    
    newimage = pixelMapper(oldimage,changeYellowToBlue)       
    newimage.setPosition(oldimage.getWidth()+1,0)
    newimage.draw(myimagewindow)
    myimagewindow.exitOnClick()


def main():
    generalTransform("mickey.gif")
    
main()