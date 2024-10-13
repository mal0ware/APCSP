import random

set_size(480, 400)

# This graphics program should draw a square. 
# The fill color should be randomly choosen from
# the COLORS list

SIDE_LENGTH = 100
COLORS = [Color.red, Color.orange, Color.yellow, Color.green, Color.blue, 
        Color.purple, Color.black, Color.gray]
        

square = Rectangle(SIDE_LENGTH, SIDE_LENGTH)
sqx = get_width()/2-(SIDE_LENGTH/2)
sqy = get_height()/2-(SIDE_LENGTH/2)
square.set_position(sqx,sqy)
square.set_color(random.choice(COLORS))
add(square)