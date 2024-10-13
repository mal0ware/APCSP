#5.9.3 Draw Something by Marius Castillo
#my program draws a target board and the user must guess where the bullseye is
#the program will visually show where the shot landed
#it will also give advice on how to adjust your aim

centerx = get_width()/2
centery = get_height()/2

#prints target board
box = Rectangle(get_width(), get_height())
box.set_position(0,0)
box.set_color(Color.purple)
add(box)
#uses canvas size to draw circle
if get_width() > get_height():
    z = get_height()/2
else:
    z = get_width()/2
area = Circle(z)
area.set_position(centerx, centery)
area.set_color(Color.orange)
add(area)
area2 = Circle(z/2)
area2.set_position(centerx, centery)
area2.set_color(Color.purple)
add(area2)
area3 = Circle(z/4)
area3.set_position(centerx, centery)
area3.set_color(Color.orange)
add(area3)

def target(x,y): #shows hit location
    vert = Line(x,0,x,get_height())
    vert.set_color(Color.black)
    add(vert)
    hori = Line(0,y,get_width(),y)
    hori.set_color(Color.black)
    add(hori)
    bullseye = Circle(4)
    bullseye.set_color(Color.red)
    bullseye.set_position(x,y)
    add(bullseye)

def checkx(x): #checks if x is correct
        if x > centerx:
            print("A little more to the left")
        elif x < centerx:
            print("A little more to the right")
        else:
            print("You are fine horizontally.")

def checky(y): #checks if y is correct
        if y > centery:
            print("a little higher.")
        elif y < centery:
            print("a little lower.")
        else:
            print("keep that height.")

#user input
x = 0
y = 0
try:
    x = int(input("X: "))
    y = int(input("Y: "))
    target(x, y)
    print("Nice shot...")
    if x != centerx or y != centery:#if not center
        print("You missed.")
        checkx(x)#advice on horizontal aim
        checky(y)#advice on vertical aim
    else:
        print("You hit the bullseye!")
except ValueError:
     print("Uh oh! Please enter valid values")