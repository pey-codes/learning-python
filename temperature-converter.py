Temperature = float(input("Enter temperature: "))
Scale = input("Choose a scale: ")

if Scale == "F": 
    Celsius = (Temperature - 32) * 5 / 9
    print("Celsius =" , Celsius)

elif Scale == "K":
    Celsius = (Temperature - 273.15)
    print("Celsius =" , Celsius)
else:
    Celsius = Temperature
    print("Celsius =" , Celsius)