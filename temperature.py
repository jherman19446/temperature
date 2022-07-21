degrees = input("What is the temperature indicated by F or C ").upper()


def CtoF(temperature):
    temperature = int(temperature)
    fahrenheit = (temperature * 1.8) + 32
    kelvinF = (fahrenheit - 32) * (5/9) + 273.15
    print("Your temperature in Fahrenheit is " + str(fahrenheit) + " and your temperature in Kelvin is " + str(kelvinF))

def FtoC(temperature):
    temperature = int(temperature)
    celsius = (temperature - 32) * .5556
    kelvinC = (celsius + 273.15)
    print("Your temperature in Celsius is " + str(celsius) + " and your temperature in Kelvin is " + str(kelvinC))

if degrees[:-1].isnumeric() == True:
    if degrees[-1] == "C":
        temperature = degrees.replace("C","")
        CtoF(temperature)
    
    
    elif degrees[-1] == "F":
        temperature = degrees.replace("F","")
        FtoC(temperature)
    

else:
    print("Please check your input and try again")





