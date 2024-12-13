import numpy as np
from PIL import Image, ImageDraw
import math

G = 1
HEIGHT = 128
WIDTH = 128

def forceGravity(M,m,r):
    global G
    return (G*M*m / (r**2))


def calculateEffect(startRow, startCol, grav):
    
    for indexRow, row in enumerate(grav):

        for indexCol, col in enumerate(row):

            distance = math.sqrt((startRow-indexRow)**2+(startCol-indexCol)**2)

            if distance != 0:
                force = forceGravity(100, 1, distance)

                angle = math.atan2(indexCol-startCol, startRow-indexRow)
                grav[indexRow, indexCol, 0] += force*math.cos(angle)
                grav[indexRow, indexCol, 1] += force*math.sin(angle)
    return grav

def convertColour(grav):
    gravColour = np.zeros(shape=(HEIGHT,WIDTH,3), dtype=np.uint8)
    for indexRow, row in enumerate(gravColour):

        for indexCol, col in enumerate(row):
            gravX= grav[indexRow, indexCol, 0]
            gravY= grav[indexRow, indexCol, 1]
            intensity = math.floor(math.sqrt(gravX**2 + gravY**2))
            gravColour[indexRow, indexCol] = [intensity, 0, 0]
    return gravColour



def createValues():
    preset = np.zeros(shape=(3*HEIGHT,3*WIDTH,3), dtype=np.uint8)



img = Image.new("1", (HEIGHT, WIDTH))
draw = ImageDraw.Draw(img)

draw.circle((HEIGHT /2,WIDTH / 2), 16, fill ="white")

arr = np.asarray(img)



for indexRow, row in enumerate(arr):
    print(indexRow)
    for indexCol, col in enumerate(row):
        if col:
            grav = calculateEffect(indexCol, indexRow)

img = convertColour(grav)
print(img)
img = Image.fromarray(img, "RGB")
img.show()






