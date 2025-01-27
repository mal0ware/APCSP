# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/e07cd01271cac589cc9ef1bf012c6a0c"
IMAGE_WIDTH = 280
IMAGE_HEIGHT = 200
DARKENING_FACTOR = 50
MIN_PIXEL_VALUE = 0

image = Image(IMAGE_URL)
image.set_position(70, 70)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)

# This function should take a pixel and return a tuple
# with the new color
def darken_filter():
    for x in range(int(image.get_width()/2)):
        for y in range(int(image.get_height())):
            pixel = image.get_pixel(x,y)
            image.set_red(x,y, pixel[0] - DARKENING_FACTOR)
            image.set_green(x,y, pixel[1] - DARKENING_FACTOR)
            image.set_blue(x,y, pixel[2] - DARKENING_FACTOR)

# This function should loop through each pixel on the
# left hand side and call the darken filter to calculate 
# the new color then update the color.
def change_picture():
    darken_filter()
    add(image)
    pass            

# Give the image time to load
print("Making Darker....")
print("Might take a minute....")
timer.set_timeout(change_picture, 1000)