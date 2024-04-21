def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation.")
print("1.fahrenheit to celsius")
print("2.celsius to fahrenheit")

while True:
    choice = input("Enter choice(1/2): ")
    if choice in ('1', '2'):

        if choice == '1':
            num1 = float(input("enter number (fahrenheit): "))
            multiply = (num1 - 32)*(5/9)
            print(multiply,("celsius"))

        elif choice == '2':
            num2 = float(input("enter number (celsius): "))
            divide = (num2 * (9/5))+32
            print(divide,("fahrenheit"))

        next_calculation = input("convert temperature again? (yes/no): ")
        if next_calculation == "no":
            uni = int(input(
                "1.area\n2.length\n3.Weight\n4.temperature\n5.volume\n6.speed\n7.numeric system\nChose witch category number do you want :  "))
            if uni == 1:
                import area
            elif uni == 2:
                import length
            elif uni == 3:
                import Weight
            elif uni == 4:
                import temperature
            elif uni == 5:
                import volume
            elif uni == 6:
                import speed
            elif uni == 7:
                import numeric_system

            else:
                print("Invalid error")

    else:
        print("Invalid Input")
