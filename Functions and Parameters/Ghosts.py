#CodeHS Python 5.9.1 Ghosts by Marius Castillo
#Constants for body
HEAD_RADIUS = 35
BODY_WIDTH = HEAD_RADIUS * 2
BODY_HEIGHT = 60
NUM_FEET = 3
FOOT_RADIUS = (BODY_WIDTH) / (NUM_FEET * 2)
#Constants for eyes
PUPIL_RADIUS = 4
PUPIL_LEFT_OFFSET = 8
PUPIL_RIGHT_OFFSET = 20
EYE_RADIUS = 10
EYE_OFFSET = 14

center_x = get_width()/2
center_y = get_height()/2

def head(x, y, color):
    head = Circle(HEAD_RADIUS)
    head.set_color(color)
    head.set_position(x, y)
    add(head)

def body(x, y, color):
    body = Rectangle(BODY_WIDTH, BODY_HEIGHT)
    body.set_color(color)
    body.set_position(x - BODY_WIDTH/2,y)
    add(body)

#eyes are complicated bruh.
def eyes(x, y):
    #lefteye
    lefteye = Circle(EYE_RADIUS)
    lefteye.set_color(Color.white)
    lefteye.set_position(x-EYE_OFFSET, y)
    add(lefteye)
    #right eye
    righteye = Circle(EYE_RADIUS)
    righteye.set_color(Color.white)
    righteye.set_position(x+EYE_OFFSET, y)
    add(righteye)
    #left pupil
    leftpupil = Circle(PUPIL_RADIUS)
    leftpupil.set_color(Color.blue)
    leftpupil.set_position(x-PUPIL_LEFT_OFFSET,y)
    add(leftpupil)
    #right pupil
    rightpupil = Circle(PUPIL_RADIUS)
    rightpupil.set_color(Color.blue)
    rightpupil.set_position(x+PUPIL_RIGHT_OFFSET,y)
    add(rightpupil)

#feet are complicated.
def feet(x, y, color):
    distance = FOOT_RADIUS * 2
    for i in range(NUM_FEET):
        foot = Circle(FOOT_RADIUS)
        foot.set_color(color)
        foot_x = x - (BODY_WIDTH / 2) + FOOT_RADIUS+ i * distance
        foot_y = y + BODY_HEIGHT
        foot.set_position(foot_x, foot_y)
        add(foot)
     
#main function
def draw_ghost(x, y, color):
    head(x, y, color)
    body(x, y, color)
    eyes(x, y)
    feet(x, y, color)
    
center_x = get_width()/2
center_y = get_height()/2
draw_ghost(center_x, center_y, Color.red)
draw_ghost(100, 100, Color.green)
draw_ghost(370, 150, Color.black)
draw_ghost(40, 200, Color.orange)