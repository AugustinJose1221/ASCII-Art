import sys
inputImageFileName = "Image.jpg"
OutputTextFileName = "Output.txt"
from PIL import Image, ImageDraw, ImageFont
font = ImageFont.load_default() # load default bitmap monospaced font
(chrx, chry) = font.getsize(chr(32))
weights = []
for i in range(32, 127):
    chrImage = font.getmask(chr(i))
    ctr = 0
    for y in range(chry):
        for x in range(chrx):
            if chrImage.getpixel((x, y)) > 0:
                ctr += 1
    weights.append(float(ctr) / (chrx * chry))
image = Image.open(inputImageFileName)
(imgx, imgy) = image.size
imgx = int(imgx / chrx)
imgy = int(imgy / chry)
image = image.resize((imgx, imgy), Image.BICUBIC)
image = image.convert("L") # convert to grayscale
pixels = image.load()
output = open(OutputTextFileName, "w")
for y in range(imgy):
    for x in range(imgx):
        w = float(pixels[x, y]) / 255
        wf = -1.0; k = -1
        for i in range(len(weights)):
            if abs(weights[i] - w) <= abs(wf - w):
                wf = weights[i]; k = i
        output.write(chr(k + 32))
    output.write("\n")
output.close()
f = open('out.txt', 'r')
fcontents = f.read()
print(fcontents)
f.close()
