def calcArea(base, height):
    return (base * height)/ 2

input("Lets Calculate the Area of Triangle")
input_base = int(input("Enter the Base:- "))
input_height = int(input("Enter the Height:- "))

print(f"The Area of Triangle is {calcArea(input_base, input_height)}")

