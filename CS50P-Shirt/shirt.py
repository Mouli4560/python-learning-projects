from PIL import Image, ImageOps
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command line arguments")

elif len(sys.argv) == 3:
    first = sys.argv[1].lower()
    second = sys.argv[2].lower()
    jpg = first.endswith(".jpg") and second.endswith(".jpg")
    png = first.endswith(".png") and second.endswith(".png")
    jpeg = first.endswith(".jpeg") and second.endswith(".jpeg")
    jpg_diff = first.endswith(".jpg") and not second.endswith(".jpg")
    png_diff = first.endswith(".png") and not second.endswith(".png")
    jpeg_diff = first.endswith(".jpeg") and not second.endswith(".jpeg")

    if not (jpg or png or jpeg):
        sys.exit("Invalid input")
    elif jpg_diff or png_diff or jpeg_diff:
        sys.exit("Input and output have different extensions")
    else:
        with Image.open(sys.argv[1]) as img:
            img = ImageOps.fit(img, [600, 600])
            with Image.open("shirt.png") as shirt:
                img.paste(shirt, mask = shirt)
                img.save(second)
