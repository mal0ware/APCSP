# Constants representing the radius of the top, middle,
# and bottom snowball.
BOTTOM_RADIUS = 100
MID_RADIUS = 60
TOP_RADIUS = 30
#some variable i made
bottom_dia = int(BOTTOM_RADIUS*2)
middle_dia = int(MID_RADIUS*2)
top_dia = int(TOP_RADIUS*2)

#bottom snowball
bottom = Circle(BOTTOM_RADIUS)
bottom.set_color(Color.gray)
bottom.set_position(get_width()/2, get_height()-BOTTOM_RADIUS
add(bottom)

#middle snowball
middle = Circle(MID_RADIUS)
middle.set_color(Color.gray)
middle.set_position(get_width()/2, get_height()-bottom_dia-MID_RADIUS)
add(middle)

#top snowball
top = Circle(TOP_RADIUS)
top.set_color(Color.gray)
top.set_position(get_width()/2, get_height()-bottom_dia-middle_dia-TOP_RADIUS)
add(top)