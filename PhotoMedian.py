import statistics
from PIL import Image

def median(mylist):
    sorts = sorted(mylist)
    length = len(sorts)
    if not length % 2:
        return (sorts[int(length / 2)] + sorts[int(length / 2) - 1]) / 2.0
    return sorts[length / 2]

#imgPath = os.path.abspath("Images/1.png")
imgPath = "Images/"

im = ()
for i in range (1,9):
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