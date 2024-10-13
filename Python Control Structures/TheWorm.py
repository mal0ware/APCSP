NUM_CIRCLES = 15

# This graphics program should draw a worm. 
# A worm is made up of NUM_CIRCLES circles. 
# Use a for loop to draw the worm, 
# centered vertically in the screen. 
# Also, be sure that the worm is still drawn across 
# the whole canvas, even if the value of NUM_CIRCLES is changed.

dia = get_width() / NUM_CIRCLES
rad = dia / 2
#initial
x = rad

for i in range (NUM_CIRCLES):
    circ = Circle(rad)
    circ.set_color(Color.black)
    circ.set_position(x , get_height() / 2)
    #this sets the X position of the next circle
    x = x + dia
    #makes the circle
    add(circ)