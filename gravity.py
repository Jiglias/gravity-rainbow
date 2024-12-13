import numpy as np
from PIL import Image, ImageDraw
import math

G = 1
name = "saw"
img = Image.open(name+".png")

WIDTH, HEIGHT = img.size

img = img.convert("L")



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

def applyPreset(row, col, grav, intense):
    intensity = intense / 255

    startX = midX - col # coordinates of were we start on preset
    startY = midY - row
    for indexRow in range(HEIGHT):
        for indexCol in range(WIDTH):
            currX = startX + indexCol # where we currently are on preset
            currY = startY + indexRow

            # print([currY, currX, 0],[indexRow, indexCol, 0] )
            try:
                grav[indexRow, indexCol, 0] += preset[currY, currX, 0]*intensity
                grav[indexRow, indexCol, 1] += preset[currY, currX, 1]*intensity
            except:
                print(preset[currY, currX],grav[indexRow, indexCol] )
    return grav



def convertColour(grav):
    gravColour = np.zeros(shape=(HEIGHT,WIDTH,3),  dtype=np.uint8)
    for indexRow, row in enumerate(gravColour):

        for indexCol, col in enumerate(row):
            gravX= grav[indexRow, indexCol, 0]
            gravY= grav[indexRow, indexCol, 1]

            angle = (math.atan2(gravY,gravX)+math.pi) / (2*math.pi) * 255

            intensity = min(math.floor(math.sqrt(gravX**2 + gravY**2)/3),255)


            gravColour[indexRow, indexCol] = [angle, 180, intensity]
    return gravColour



midX = 3*WIDTH//2
midY = 3*HEIGHT//2
preset = calculateEffect(midY, midX, np.zeros((3*HEIGHT,3*WIDTH, 2)))

grav = np.zeros((HEIGHT,WIDTH, 2))

# img = Image.new("1", (HEIGHT, WIDTH))
# draw = ImageDraw.Draw(img)

# draw.circle((HEIGHT //2,WIDTH // 2), 16, fill ="white")



arr = np.asarray(img)



for indexRow, row in enumerate(arr):
    print(indexRow)
    for indexCol, col in enumerate(row):
        if col!=0:
            grav = applyPreset(indexCol, indexRow, grav, col)

img = convertColour(grav)
print(img)
img = Image.fromarray(img, "HSV")
img.show()
img = img.convert("RGB")
img.save(name+"-New.png")






