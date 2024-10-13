def celsius(farenheit):
    celsius = (int(farenheit) - 32)/1.8
    return celsius

def farenheit(celsius):
    farenheit = (int(celsius) * 1.8)+32
    return farenheit

try:
    print(farenheit(input("Celsius to Farenheit:")))
    print(celsius(input("Farenheit to Celsius: ")))
except ValueError:
    print("I'm sorry, that isn't possible.")