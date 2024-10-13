# Create a Blue rectangle on left
rect_1 = Rectangle(get_width()/3, get_height())
rect_1.set_color(Color.blue)
rect_1.set_position(0, 0)

# Create a Red rectangle on right
rect_2 = Rectangle(get_width()/3, get_height())
rect_2.set_color(Color.red)
rect_2.set_position(get_width()*2 /3, 0)

#add them both to canvas
add(rect_1)
add(rect_2)