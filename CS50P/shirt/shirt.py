from PIL import Image, ImageOps
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not (len(sys.argv[1]) >= 5 and (sys.argv[1].endswith(".jpg") or sys.argv[1].endswith(".jpeg") or sys.argv[1].endswith(".png"))):
        sys.exit("Invalid input")

    if not (len(sys.argv[2]) >= 5 and (sys.argv[2].endswith(".jpg") or sys.argv[2].endswith(".jpeg") or sys.argv[2].endswith(".png"))):
        sys.exit("Invalid output")

    if sys.argv[1][-4:] != sys.argv[2][-4:]:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open("shirt.png") as imgS:

            with Image.open(sys.argv[1]) as img1:
                resizedImg = ImageOps.fit(img1, (600, 600))
                resizedImg.save("newImg.jpg")
                resizedImg.paste(imgS, imgS)
                resizedImg.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


main()
