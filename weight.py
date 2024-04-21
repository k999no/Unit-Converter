while True:
    print("""
    if you want convert weight: chose one of the unit:
    1.Kg to g, 2.kg to mg 
    3.g to kg, 4.g to mg 
    5.mg to g, 6.mg to kg 
    """)
    menu = int(input("enter the operation number from (1/2/3/4/5/6): "))
    if menu == 1:
        def multiply(n1):
            multiply = n1 * 1000
            return multiply;


        n1 = int(input("enter first number (kg): "))
        print("the convert number in grams equal: ", multiply(n1), ("g"))

    elif menu == 2:
        def multiply(n1):
            multiply = n1 * 1000000
            return multiply;


        n1 = int(input("enter first number (kg): "))
        print("the convert number in milligrams equal: ", multiply(n1), ("mg"))

    elif menu == 3:
        def multiply(n1):
            multiply = n1 * 0.001
            return multiply;


        n1 = int(input("enter first number (g): "))
        print("the convert number in kilograms equal: ", multiply(n1), ("kg"))

    elif menu == 4:
        def multiply(n1):
            multiply = n1 * 1000
            return multiply;


        n1 = int(input("enter first number (g): "))
        print("the convert number in milligrams equal: ", multiply(n1), ("mg"))

    elif menu == 5:
        def multiply(n1):
            multiply = n1 * 0.001
            return multiply;


        n1 = int(input("enter first number (mg): "))
        print("the convert number in grams equal: ", multiply(n1), ("g"))

    elif menu == 6:
        def multiply(n1):
            multiply = n1 * 0.000001
            return multiply;


        n1 = float(input("enter first number (mg): "))
        print("the convert number in kilograms equal: ", multiply(n1), ("kg"))
    next_calculation = input("convert Length again? (yes/no): ")
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
