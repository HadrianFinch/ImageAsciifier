from cgitb import grey
from math import ceil, floor
from turtle import color
import imageio.v3 as imageio
import numpy as np
from progress.bar import PixelBar

# read an image
image = imageio.imread('images/python.jpg')
  
def RgbToGray(rgb):

    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

greyRamp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
def GetCharacterFromGreyscale(gs):
    return greyRamp[ceil((len(greyRamp) - 1) * gs / 255)]

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".format(r, g, b, text)

def GenerateAscii(img, chunkWidth, chunkHeight):

    totalLoops = img.shape[0] * img.shape[1]

    # newImage = np.zeros((floor(img.shape[0] / chunkHeight), floor(img.shape[1] / chunkWidth), 3), dtype="uint8")
    asciiText = ""
    escapedConsoleText = ""

    bar = PixelBar('Processing', max=totalLoops)
    
    for newY in range(0, (floor(img.shape[0] / chunkHeight))):
        for newX in range(0, floor(img.shape[1] / chunkWidth)):

            imageX = newX * chunkWidth
            imageY = newY * chunkHeight

            pixels = []
            pixelColors = []

            # print("imageY + chunkHeight: ", imageY + chunkHeight, ", img.height: ", img.shape[0], ", min: ", min((imageY + chunkHeight), img.shape[0]))

            for y in range(imageY, min((imageY + chunkHeight), img.shape[0])):
                for x in range(imageX, min((imageX + chunkWidth), img.shape[1])):

                    pixelColors.append(img[y][x])
                    pixels.append(RgbToGray(img[y][x]))
                    bar.next()

            colorAverage = [0, 0, 0]
            greyscaleAverage = 0
            for i in range(len(pixels)):
                greyscaleAverage += pixels[i]

                colorAverage[0] += pixelColors[i][0]
                colorAverage[1] += pixelColors[i][1]
                colorAverage[2] += pixelColors[i][2]

            if (len(pixels) > 0):
                greyscaleAverage = greyscaleAverage / len(pixels)

                colorAverage[0] = colorAverage[0] / len(pixelColors)
                colorAverage[1] = colorAverage[1] / len(pixelColors)
                colorAverage[2] = colorAverage[2] / len(pixelColors)                
            else:
                greyscaleAverage = 0
                colorAverage[0] = 0
                colorAverage[1] = 0
                colorAverage[2] = 0
            char  = GetCharacterFromGreyscale(greyscaleAverage)
            asciiText += char
            escapedConsoleText += colored(colorAverage[0], colorAverage[1], colorAverage[2], char)
            # if (colorAverage[0] != colorAverage[1]):
            #     print("Different!")

            # print("color average: ", colorAverage)
            # escapedConsoleText += colored(255, 233, 0, char)

            # newImage[newY][newX][0] = average
            # newImage[newY][newX][1] = average
            # newImage[newY][newX][2] = average

        asciiText += "\n"
        escapedConsoleText += "\n"

    return [asciiText, escapedConsoleText]


newImage = GenerateAscii(image, 4, 10)

print("\n", newImage[1])

file = open("output.asciiArt", "w")

print(colored(255, 0, 33, "foobar blat blah"))

file.write(newImage[0])

print("output written to output.asciiArt")
