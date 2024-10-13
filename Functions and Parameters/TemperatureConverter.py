# converts C to F and returns a float.
def celsius(farenheit):
    celsius = (farenheit - 32)/1.8
    float(celsius)
    return celsius

#converts F to C and returns a float.
def farenheit(celsius):
    farenheit = (celsius * 1.8)+32
    float(farenheit)
    return farenheit
# Now change 0C to F:
print(farenheit(0))
# Change 100C to F:
print(farenheit(100))
# Change 40F to C:
print(celsius(40))
# Change 80F to C:
print(celsius(80))