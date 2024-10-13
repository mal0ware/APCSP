# This program should draw a stop light

LIGHT_RADIUS = 25
STOPLIGHT_WIDTH = 100
STOPLIGHT_HEIGHT = 250
BUFFER = 75

rect = Rectangle(STOPLIGHT_WIDTH, STOPLIGHT_HEIGHT)
rect.set_position(get_width()/2-(STOPLIGHT_WIDTH/2), get_height()/2-(STOPLIGHT_HEIGHT/2))
rect.set_color(Color.gray)
add(rect)
# Implement a function that draws a single circle 
# with radius LIGHT_RADIUS.
# The circle should be in the center of the screen horizontally.
# Use the parameters for the y position and color
def draw_circle(y_pos, color):
    circ = Circle(LIGHT_RADIUS)
    circ.set_color(color)
    circ.set_position(get_width()/2, y_pos)
    add(circ)
draw_circle(get_height()/2, Color.yellow)
draw_circle(get_height()/2-BUFFER, Color.red)
draw_circle(get_height()/2+BUFFER, Color.green)