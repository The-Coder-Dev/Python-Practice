# Temperature Convertor in Python

unit = input("Is temperature in Celsius or Fahrenheit (C/F): ");
temp = float(input("Enter the temperature: "))

if unit == "C": 
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"Temperature in Fahrenheit: {temp}°F")

elif unit == "F": 
    temp = round((temp - 32) * 5/9 , 1)
    print(f"Temperature in Calsius: {temp}°C")

else:
    print(f"{unit} was not valid...")