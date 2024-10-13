# Constants for the image
IMAGE_URL = "https://codehs.com/uploads/c709d869e62686611c1ac849367b3245"
IMAGE_WIDTH = 420
IMAGE_HEIGHT = 300
IMAGE_LOAD_TIME = 1000

image = Image(IMAGE_URL)
image.set_size(IMAGE_WIDTH, IMAGE_HEIGHT)
add(image)

"""
 Filter that takes an image as a parameter
 and applies a filter, then returns the filtered image
"""
#changeable variable
enhancer = 30

#filter on the pixel level
def sillywilly(pixel):
    RGB = []
    for r in range(len(pixel)):
        if pixel[r] >= 128:
            color = min(pixel[r] + enhancer, 255)
        elif pixel[r] < 128:
            color = max(pixel[r] - enhancer, 0)   
        RGB.append(color)
    return RGB

def apply_filter(image):
    for x in range(image.get_width()):
        for y in range(image.get_height()):
            pixel = image.get_pixel(x,y)
            filtered = sillywilly(pixel)
            image.set_red(x, y, filtered[0])
            image.set_green(x, y, filtered[1])
            image.set_blue(x, y, filtered[2])
    return image

def change_image():
    global image
    image = apply_filter(image)
 
timer.set_timeout(change_image, IMAGE_LOAD_TIME)
print("give it a few seconds")