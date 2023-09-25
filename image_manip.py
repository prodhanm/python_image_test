from PIL import Image, ImageFilter

filename = "./image/image1.jpg"
logo = "./image/logo.png"

with Image.open(filename) as img:
    img.load()
    #img.show()
    size = img.size
    print(f"size = {size}")
    format = img.format
    print(f"format = {format}")
    mode = img.mode
    print(f"mode = {mode}")
    print("Cropped image:")
    # img.crop = (x,y, w+x, h+y)
    # x,y can be the coordinates to start and w+x or y+h
    # is a way to add the reduced size to the coordinates.
    # This way the image is cropped below the actual size.
    cropped_img = img.crop((0,0, 2500, 4000))
    cropped_img.size
    crop_img_size = print(f"size = {cropped_img.size}")
    #the rotate() takes a geometrical angle as an argument,
    # and the value can be positive or negative, depending 
    # on the orientation of the image. 
    img_crop = cropped_img.rotate(-90, expand=True, center=(500,600))
    #The image has been cropped to center the image of the
    #child at the tuple: (500,600). 
    img_resize = img_crop.resize(
        (700,500)
        )
    img_resize.show()
    #When the image is resized after some aspects of image
    #maipulation, it is able to be resized to the size that
    #is desired, to still maintain the clarity of the image.
    '''
    '''
    #cropped_img.show()
''' 
    #cropped_img.effect_noise((500,500),128)
    image_2 = cropped_img.copy()
    #image_2.show()
    #image_2.paste(logo_img,(0,0,150,85),mask=logo_img)
    #image_2.save("mixed.png")
    #image_2.show("mixed.png")
    with Image.open(logo) as logo_img:
        logo_img.load()
        #logo.show()
        #image_2.paste(logo_img, (0,0,150,85), logo_img)
        #image_2.show()
        #logo_img = Image.open(logo)
        #logo_img.show()
        logo_img = logo_img.convert("L")
        threshold = 50
        logo_img = logo_img.point(lambda x:255 if x > threshold else 0)
        logo_img = logo_img.resize(
            logo_img.width//2, logo_img.height//2
        )
        logo_img = logo_img.filter(Image.BICUBIC)
        logo_img.show()

#img2 = Image.open(logo)
#print(img2.size)
'''


    