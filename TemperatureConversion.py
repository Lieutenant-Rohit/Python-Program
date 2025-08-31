def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32

print("Welcome To Temperature Conversion")
print("1 ---> Fahrenheit to Celsius")
print("2 ---> Celsius to Fahrenheit")
choice = input("ENTER YOUR CHOICE:- ")
if choice == "1":
    temp = float(input("Enter the Temperature in Fahrenheit:- "))
    print(f"The Temperature in Celsius is {fahrenheit_to_celsius(temp):.2f} degree celsius")

elif choice == "2":
    temp = float(input("Enter the Temperature in Celsius:- "))

    print(f"The Temperature in Fahrenheit is {celsius_to_fahrenheit(temp):.2f} degree fahrenheit")
else:
    print("Invalid Choice")
