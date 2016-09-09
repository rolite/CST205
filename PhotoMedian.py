'''
David Little
CSt 205 Proj 1

This code will take a set of .png pictures labeled 1.png to n.png from the Project1Images folder and performs a median function
to remove inconsiderate pedestrians and outputs to output.png

Not fast, doesn't check for errors or read in non .png files
but it works

github
https://github.com/rolite/CST205
'''

import os, os.path
import statistics
from PIL import Image

def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return (sorts[int(length / 2)] + sorts[int(length / 2) - 1]) / 2.0
    return sorts[length / 2]

#imgPath = os.path.abspath("Images/1.png")
imgPath = "Project1Images/"

im = ()
for i in range (1,len([name for name in os.listdir(imgPath)])):
    im = im + (Image.open(imgPath + str(i) + ".png").convert('RGB'),)

newImg = Image.new('RGB', im[0].size)

x,y = im[0].size

for i in range (0,x):
    for j in range (0,y):
        arR = ()
        arG = ()
        arB = ()
        for image in im:
            r, g, b = image.getpixel((i, j))
            arR = arR + (r,)
            arG = arG + (g,)
            arB = arB + (b,)
        newImg.putpixel((i,j), (int(median(arR)), int(median(arG)), int(median(arB))))

newImg.save("output.png")
