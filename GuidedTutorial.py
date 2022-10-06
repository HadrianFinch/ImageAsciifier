# Here are all the imports that you need, uncomment as needed

# from cgitb import grey
# from math import ceil, floor
# from turtle import color
# import imageio.v3 as imageio
# import numpy as np
# from progress.bar import PixelBar

# read an image from a file to a varible called "image" using the imageio library

# Function to convert from rgb to greyscale
# correct ratio code is gray = (0.2989 * r + 0.5870 * g + 0.1140 * b)

# Function to convert from greyscale value to a character
# use ceil() and this grey ramp

# PICK A GREY RAMP TO UNCOMMENT!
# greyRamp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
# greyRamp = "▮▼●cɵ*v<>^`\"'~."

# main function
# parameters: 
#   img          -  the loaded pixels of the image
#   chunkWidth   -  the width of the console character
#   chunkHeight  -  the height of the console character

def GenerateAscii(img, chunkWidth, chunkHeight):

    # calculate the number of loops based off the width and height of the image
    # use img.shape to get size

    asciiText = "" # define the text for the output

    # OPTIONAL: make a progress bar to show the progress of the calculations
    # bar = PixelBar('Processing', max=totalLoops) 
    
    # Use a double for loop to index into the 2d array of pixels
    # use the range() fuction to control the loop

    # first varible is newY
    # second varible is newX

    # how far do we need to index?

    # for :
        # for :

            # calculate the source image position by multiplying by width and height of chunk
            # save to varables imageX and imageY

            # create an array for the pixel data to be stored

            # use another double for loop to get the pixels in the chunk from the source img

            # for y in range(imageY, min((imageY + chunkHeight), img.shape[0])):
            #     for x in range(imageX, min((imageX + chunkWidth), img.shape[1])):

                    # Use RgbToGrey() to get the greyscale value
                    # then save it to a new item in the pixels array

                    # OPTIONAL
                    # advance the progress bar with "bar.next()"

            # make a new varible to store the average of all the pixels 
            greyscaleAverage = 0

            # go through all the pixels and ad their values together
            for i in range(len(pixels)):
                # use the += operator to add to an existing varible

            # safety check to make sure to not devide by 0
            if (len(pixels) > 0):
                # complete the averaging by deviding by the number of pixels

            else:
                greyscaleAverage = 0

            

            char  = GetCharacterFromGreyscale(greyscaleAverage)
            asciiText += char

        # add a new line to the string

    return asciiText

# run the function with (image, 4, 10)
# print the output

# OPTIONAL: put the output into a file
# file = open("output.asciiArt", "w")
# file.write(newImage[0])

print("Generated!")
