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
    ASCIICHARS = " ^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

    for i in range(width):
        print()
        for j in range(height):
            pixel = pixels[j][i]
            print(ASCIICHARS[int(pixel//(255/65))], end="")
            print(ASCIICHARS[int(pixel//(255/65))], end="")

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
    
    print ("Welcome to ASCII art converter")
    print ("Provide a .jpg file")

    # getting file
    while True:
        try:
            print ("Provide a filename: ")
            filename = input()
            
            while not filename.endswith(".jpg"):
                print("Provide a .jpg file!")
                filename = input()
            
            image = Image.open(filename)
            height, width = image.size

        except:
            print("File not found! \n")

        else:
            print("Image loaded! Size: ", height, "x", width)
            try:
                print("Provide a new height to resize image or current height (", height, "): ")
                newHeight = int(input())

            except ValueError:
                print("That's not a number!")
            
            else:
                height = int(newHeight)
                width = int(height / image.height * image.width)
                print("new width: ", width)
                image.resize((height, width))
                image.save("resized.jpg")
                break

    # selecting mode
    print ("Select one of the modes: ")
    print ("1: Average")
    print ("2: Lightness")
    print ("3: Luminosity")

    print(height, width)

    while True:
        try:
            selection = int(input("Select mode: "))
            while (selection > 3 or selection < 1):
                selection = int(input("Select mode (1 - 3): "))
        except ValueError:
            print ("That's not a number!")
        else:
            print ("selected mode: ", selection)
            break

    # printing image
    pixels = loadImage("resized.jpg", selection)
    printPixels(pixels, height, width)

    print("\n\n")
