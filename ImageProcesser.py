from cgitb import grey
from math import ceil, floor
import imageio.v3 as imageio
import numpy as np

# read an image
image = imageio.imread('images/cat.jpg')
  
# print shape of the image
print(image.shape)

print(image[2][4][2])

def RgbToGray(rgb):

    r = rgb[0]
    g = rgb[1]
    b = rgb[2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray

greyRamp = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "
def GetCharacterFromGreyscale(gs):
    return greyRamp[ceil((len(greyRamp) - 1) * gs / 255)]

def GenerateAscii(img, chunkWidth, chunkHeight):

    totalLoops = img.shape[0] * img.shape[1]
    currentLoop = 0
    progress = 0

    # newImage = np.zeros((floor(img.shape[0] / chunkHeight), floor(img.shape[1] / chunkWidth), 3), dtype="uint8")
    asciiText = ""

    for newY in range(0, (floor(img.shape[0] / chunkHeight))):
        for newX in range(0, floor(img.shape[1] / chunkWidth)):

            imageX = newX * chunkWidth
            imageY = newY * chunkHeight

            pixels = []

            # print("imageY + chunkHeight: ", imageY + chunkHeight, ", img.height: ", img.shape[0], ", min: ", min((imageY + chunkHeight), img.shape[0]))

            for y in range(imageY, min((imageY + chunkHeight), img.shape[0])):
                for x in range(imageX, min((imageX + chunkWidth), img.shape[1])):
                    pixels.append(RgbToGray(img[y][x]))
                    currentLoop += 1

            if (progress != round((currentLoop / totalLoops) * 100)):
                progress = round((currentLoop / totalLoops) * 100)
                print("Progress: ", progress, "%")

            average = 0
            for i in range(len(pixels)):
                average += pixels[i]

            if (len(pixels) > 0):
                average = average / len(pixels)
            else:
                average = 0

            char  = GetCharacterFromGreyscale(average)
            asciiText += char

            # newImage[newY][newX][0] = average
            # newImage[newY][newX][1] = average
            # newImage[newY][newX][2] = average

        asciiText += "\n"    

    return asciiText


newImage = GenerateAscii(image, 4, 8)

print("\n", newImage)

file = open("output.asciiArt", "w")

file.write(newImage)

print("output written to output.asciiArt")
