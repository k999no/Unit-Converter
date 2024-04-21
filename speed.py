def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


print("Select operation.")
print("1.mph to kph")
print("2.kph to mph")

while True:
    choice = input("Enter choice(1/2): ")
    if choice in ('1', '2'):

        if choice == '1':
            num1 = float(input("enter number (mph): "))
            multiply = num1 * 1.609344
            print(multiply,("kph"))

        elif choice == '2':
            num2 = float(input("enter number (kph): "))
            divide = num2 / 1.609344
            print(divide,("mph"))

        next_calculation = input("convert speed again? (yes/no): ")
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
