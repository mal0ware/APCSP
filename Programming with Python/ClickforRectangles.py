RECT_HEIGHT = 50
RECT_WIDTH = 30

COLORS = (Color.red, Color.black, Color.purple, Color.green, Color.orange)

def make_rect(x,y):
    rect = Rectangle(RECT_WIDTH, RECT_HEIGHT)
    rect.set_color(random.choice(COLORS))
    rect.set_position(x - RECT_WIDTH/2, y - RECT_HEIGHT/2)
    add(rect)
    
add_mouse_click_handler(make_rect)