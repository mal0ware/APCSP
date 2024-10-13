NUM_CIRCLES = 15

# This graphics program should draw a caterpillar. 
# A caterpillar is made up of NUM_CIRCLES circles.
# The circles should alternate red - green - red - green, etc
# Use a for loop to draw the worm, 
# centered vertically in the screen. 
# Also, be sure that the worm is still drawn across 
# the whole canvas, even if the value of NUM_CIRCLES is changed.

#diameter and radius
dia = get_width() / NUM_CIRCLES
rad = dia / 2

#position of initial circle
x = rad

for i in range (NUM_CIRCLES):
    circ = Circle(rad)
    if i % 2 == 0:
        circ.set_color(Color.red)
    else:
        circ.set_color(Color.green)
    circ.set_position(x , get_height() / 2)
    x = x + dia
    add(circ)