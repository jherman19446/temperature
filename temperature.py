fahrenheit = input("What is the temperature in Fahrenheit? ")
celsius = int(fahrenheit) - 32 * .5556
kelvin = int(celsius) + 273.15
Cfloat = "{:.2f}".format(celsius)
Kfloat = "{:.2f}".format(kelvin)
print("The temperature in Celsius is " + Cfloat + " and the temperature in Kelvin is " + Kfloat)