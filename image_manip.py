from PIL import Image

filename = "./image/image1.jpg"

with Image.open(filename) as img:
    img.load()
    #img.show()
    size = img.size
    print(f"size = {size}")
    format = img.format
    print(f"format = {format}")
    mode = img.mode
    print(f"mode = {mode}")
    # img.crop = (x,y, w+x, h+y)
    # x,y can be the coordinates to start and w+x or y+h
    # is a way to add the reduced size to the coordinates.
    # This way the image is cropped below the actual size.
    cropped_img = img.crop((0,0, 2500, 4000))
    #cropped_img.rotate(-25).show()

    #cropped_img.show()