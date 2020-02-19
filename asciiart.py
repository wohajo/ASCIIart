from PIL import Image

def convertIntTuple(tup):
    str = ''.join(tup)
    return str

print ("welcome to ASCII art converter")

image1 = Image.open("parrot.jpg")
height, width = image1.size

pixels = []

for i in range(width):
    for j in range(height):
        pixels.append(image1[i, j] + (i, j))