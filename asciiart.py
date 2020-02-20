from PIL import Image


if __name__ == "__main__":
    
    print ("welcome to ASCII art converter")

    image1 = Image.open("emotikonsmile.jpg")
    height, width = image1.size
    print("image size: ", height, "x", width)

    pixels = []

    for i in range(height):
        templist = []
        for j in range(width):
            templist.append(image1.getpixel((i, j)))
        pixels.append(templist)

    for i in range(height):
        for j in range(width):
            r, g, b = pixels[i][j]
            pixels[i][j] = (r + g + b) // 3 # dzielenie calkowite

    for i in range(height):
        print()
        for j in range(width):
            print("." if pixels[j][i] > 127 else ":", end="")

    # Average: average the R, G and B values - (R + G + B) / 3
    # Lightness: average the maximum and minimum values out of R, G and B - max(R, G, B) + min(R, G, B) / 2
    # Luminosity: take a weighted average of the R, G and B values to account for human perception - 0.21 R + 0.72 G + 0.07 B

    #robi cos w jednej linijce i iteruje po wszystkim
    # i = [1, 2, 3]
    # j = [zmienna**2 for zmienna in i]