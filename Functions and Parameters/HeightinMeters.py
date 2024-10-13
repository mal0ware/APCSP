INCHES_TO_CM = 2.54
CM_TO_METERS = 0.01
FEET_TO_INCHES = 12

#asks for input
heightft = int(input("How tall are you in feet, not including inches? "))
heightin = int(input("How many inches more? "))

def convert_height_to_meters(heightft, heightin):
    #all conversions
    inches = heightft * 12 + heightin
    centimeters = inches * 2.54
    meters = centimeters * 0.01
    #print thingy out
    print (str(heightft) + " feet , " + str(heightin) + " inches =" + str(meters) + " meters")
#call function
convert_height_to_meters(heightft, heightin)
convert_height_to_meters(heightft, heightin)