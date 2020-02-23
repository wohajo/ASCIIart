from PIL import Image

def loadImage(imagePath, selection):

    pixels = []

    for i in range(height):
        templist = []
        for j in range(width):
            templist.append(image.getpixel((i, j)))
        pixels.append(templist)

    if (selection == 3):
        return luminosityCalculation(pixels, height, width)
    elif (selection == 2):
        return lightnessCalculation(pixels, height, width)
    elif (selection == 1):
        return averageCalculation(pixels, height, width)

def printPixels(pixels, height, width):
    for i in range(height):
        print()
        for j in range(width):
            pixel = pixels[j][i]
            if pixel >= 170:
                print(chr(254) * 2, end="")
            elif pixel >= 85 and pixel < 170: 
                print("::", end="")
            elif pixel < 85:
                print("..", end="")

def lightnessCalculation(pixels, height, width):
    
    for i in range(height):
        for j in range(width):
            r, g, b = pixels[i][j]
            pixels[i][j] = (r + g + b) // 3

    return pixels

def averageCalculation(pixels, height, width):
    
    for i in range(height):
        for j in range(width):
            r, g, b = pixels[i][j]
            pixels[i][j] = (max(r, g, b) + min(r, g, b)) // 2

    return pixels

def luminosityCalculation(pixels, height, width):
    
    for i in range(height):
        for j in range(width):
            r, g, b = pixels[i][j]
            pixels[i][j] = int(0.21 * r + 0.72 * g + 0.07 * b)

    return pixels

if __name__ == "__main__":
    
    # getting file
    print ("Welcome to ASCII art converter")
    print ("Provide a filename: ")
    filename = input()

    image = Image.open(filename)
    height, width = image.size
    print("Image loaded! Size: ", height, "x", width)
    #TODO secure input for jpgs only
    #TODO chcecking if file is in folder?

    # selecting mode
    print ("Select one of the modes: ")
    print ("1: Average")
    print ("2: Lightness")
    print ("3: Luminosity")
    selection = int(input("Select mode: "))

    while (selection > 3 or selection < 1):
        selection = int(input("Select mode (1 - 3): "))
        #TODO secure input from other chars

    pixels = loadImage(filename, selection)
    printPixels(pixels, height, width)

    print("\n\n")

    #robi cos w jednej linijce i iteruje po wszystkim
    # i = [1, 2, 3]
    # j = [zmienna**2 for zmienna in i]