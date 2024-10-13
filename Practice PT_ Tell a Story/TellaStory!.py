def background1(): # Returns the variable for the background for scenes 1 and 2 - Matthew Izaguirre
    background = Image("https://images.pexels.com/photos/208698/pexels-photo-208698.jpeg?cs=srgb&dl=pexels-pixabay-208698.jpg&fm=jpg")
    background.set_size(1000,500)
    background.set_position(-500,0)
    return background

def background2():# Returns the variable for the background for scenes 3 and 4 - Matthew 
    background2 = Image("https://cdn-ffcgi.nitrocdn.com/ZhDYBbXPoHrCHvLPGOdQmXKAjZXwoPng/assets/static/optimized/rev-6496b27/wp-content/uploads/2020/01/night-city-photography-2.jpg")
    background2.set_size(700,500)
    background2.set_position(0,0)
    return background2
    
def text1(): # Returns the variable for the first line of text on scene 1 - Matthew
    openingLine = Text("On a bright sunny day,")
    openingLine.set_color(Color.white)
    openingLine.set_font("20pt Times New Roman")
    openingLine.set_position(get_width()/5-10,30)
    return openingLine

def text2(): # Returns second line (Scene 1) - Matthew
    line2 = Text("Keith and his dog Jamal")
    line2.set_color(Color.white)
    line2.set_font("20 pt Times New Roman")
    line2.set_position(get_width()/5-10,60)
    return line2
    
def exclamation(): # Returns a emotion effect (Scene 2) - Matthew
    exclam = Text("!!!")
    exclam.set_color(Color.white)
    exclam.set_font("20 pt Arial")
    exclam.set_position(320,250)
    return exclam
    
def text3(): # Retruns third line (Scene 1) - Matthew
    line3 = Text("are on their daily walk...")
    line3.set_color(Color.white)
    line3.set_font("20pt Times New Roman")
    line3.set_position(get_width()/5-10,90)
    return line3 
    
def text4(): # Returns line for scene 2 - Matthew 
    line4 = Text("...when suddenly!!!")
    line4.set_color(Color.white)
    line4.set_font("20pt Times New Roman")
    line4.set_position(get_width()/5-10,30)
    return line4
    
def text5(): # Returns line for scene 3 - Matthew
    line5 = Text("5 hours later...")
    line5.set_color(Color.white)
    line5.set_font("20pt Times New Roman")
    line5.set_position(3*get_width()/5,450)
    return line5
    
def dialogue(): # Returns dialogue for scene 4 - Matthew
    dialogue = Text("Found you!!!")
    dialogue.set_color(Color.white)
    dialogue.set_font("20pt Times New Roman")
    dialogue.set_position(260,250)
    return dialogue

#Marius
def head(): # Returns the head - Marius
    head = Circle(40)
    head.set_color(Color.black)
    head.set_position(340,300)
    return head

def body(): # returns the body - Marius 
    body = Rectangle(30,100)
    body.set_color(Color.black)
    body.set_position(325,300)
    return body

def limbs(x1,y1,x2,y2): # returns either an arm or leg and sets the parameters for the postion - Marius
    limbs= Line(x1,y1,x2,y2)
    limbs.set_color(Color.black)
    return limbs
    
def eye(): # returns the eye - Marius
    eye = Circle(12)
    eye.set_color(Color.white)
    eye.set_position(320,290)
    return eye

def legL(): # returns the left leg - Marius 
    legL = Rectangle(20,70)
    legL.set_color(Color.black)
    legL.set_position(xposs)
    return legL
    
def legR():# returns the right leg - Marius
    legR = Rectangle(20,70)
    legR.set_color(Color.black)
    legR.set_position()
    return legR

def dog(x,y): #adds the dog - Louis
    dog = Image("https://png.pngtree.com/png-vector/20220611/ourmid/pngtree-portrait-of-standing-in-profile-akita-inu-dog-png-image_4826237.png")
    #dog.set_position(90, 350)
    dog.set_position(x,y)
    dog.set_size(150,100)
    return dog

def leash(x1, y1, x2, y2): #makes the leash a line - Louis
    line = Line(x1, y1, x2, y2)
    line.set_position(x1, y1)
    line.set_endpoint(x2, y2)
    line.set_color(Color.green)
    return line

    

#stick(ratio on screen, variation)
        
background = background1()
background2 = background2()
#Marius

dog1 = dog(90,350)
dog2 = dog(-50,350)
dog3 = dog(10,350)
leash = leash(130,370,250,400)

# Calls back the functions and sets it to a variable - Matthew 
openingLine = text1()
line2 = text2()
line3 = text3()
line4 = text4()
line5 = text5()
exclam = exclamation()
dialogue = dialogue()

# 
head = head()
body = body()
armL = limbs(250,400,350,330)
legL = limbs(300,450,325,400)
legR = limbs(355,400,380,450)
eye = eye()
armL2 = limbs(270,300,350,370)
armR2 = limbs(355,350,450,300)

def stick(): # draws the stickfigure - Marius
    add(head)
    add(body)
    add(legL)
    add(legR)
    add(eye)

""" 
 Draws the first scene on the canvas and outputs the first
 section of text for the story.
"""
def draw_scene1():
    print("This is scene 1")
    add(background)
    add(openingLine)
    add(line2)
    add(line3)
    stick() # - Calls a function within a function
    add(armL)
    add(dog1)
    add(leash)

""" 
 Draws the second scene on the canvas and outputs the second
 section of text for the story.
"""
def draw_scene2():
    print("This is scene 2")
    add(background)
    add(line4)
    add(head)
    stick()
    add(armL2)
    add(armR2)
    add(exclam)
    add(dog2)
""" 
 Draws the third scene on the canvas and outputs the second
 section of text for the story.
"""
def draw_scene3():
    print("This is scene 3")
    remove(background)
    add(background2)
    add(line5)
    add(dog3)
""" 
 Draws the fourth scene on the canvas and outputs the second
 section of text for the story.
"""
def draw_scene4():
    print("This is scene 4") 
    remove(line5)
    stick()
    add(armL2)
    add(armR2)
    add(dialogue)
    add(dog3)
    
#DO NOT TOUCH CODE BEYOND THIS POINT
scene_counter = 0
def draw_next_screen(x, y):
    global scene_counter
    scene_counter += 1

    if scene_counter == 1:
        draw_scene1()
    elif scene_counter == 2:
        draw_scene2()
    elif scene_counter == 3:
        draw_scene3()
    else:
        draw_scene4()

welcome = Text("Click to Begin!")
welcome.set_position(get_width() / 2 - welcome.get_width() / 2, get_height() / 2)
add(welcome)

add_mouse_click_handler(draw_next_screen)