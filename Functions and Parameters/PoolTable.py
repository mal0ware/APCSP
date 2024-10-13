POOL_BALL_RADIUS = 40
FONT_TYPE = "30pt Arial"

def draw_pool_ball(color,number,x,y):#draws ball using color,number,and position
    ball = Circle(POOL_BALL_RADIUS)
    ball.set_color(color)
    ball.set_position(x,y)
    txt = Text(number) #the number of the pool ball
    txt.set_color(Color.white)
    txt.set_font("30pt Arial")
    txt.set_position(x-(POOL_BALL_RADIUS/2), y-(POOL_BALL_RADIUS/2))

draw_pool_ball(Color.orange, 5, 100, 100)
draw_pool_ball(Color.red, 3, 150, 350)
draw_pool_ball(Color.blue, 2, 250, 140)
draw_pool_ball(Color.green, 6, 50, 200)