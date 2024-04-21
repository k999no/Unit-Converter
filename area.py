print("""
Covered units:
[ km^2 and m^2 and cm^2 and mm^2 ]
""")
while True:
    print("convert area")
    num = input("""if you want convert area
    enter the number you want to convert: """)
    unit1 = input("enter the unit you have: ")
    unit2 = input("enter the unit you want: ")
    if unit1 == "km^2" and unit2 == "m^2":
        conv = float(num) *(1000000)
        print(conv, "m^2")
    elif unit1 == "km^2" and unit2 == "cm^2":
        conv = float(num) *(10000000000)
        print(conv, "cm^2")
    elif unit1 == "km^2" and unit2 == "mm^2":
        conv = float(num) *(1000000000000)
        print(conv, "mm^2")
    elif unit1 == "m^2" and unit2 == "km^2":
        conv = float(num) /(1000000)
        print(conv, "km^2")
    elif unit1 == "m^2" and unit2 == "cm^2":
        conv = float(num) *(10000)
        print(conv, "cm^2")
    elif unit1 == "m^2" and unit2 == "mm^2":
        conv = float(num) *(1000000)
        print(conv, "mm^2")
    elif unit1 == "cm^2" and unit2 == "km^2":
        conv = float(num) /(10000000000)
        print(conv, "km^2")
    elif unit1 == "cm^2" and unit2 == "m^2":
        conv = float(num) /(10000)
        print(conv, "m^2")
    elif unit1 == "cm^2" and unit2 == "mm^2":
        conv = float(num) *(100)
        print(conv, "mm^2")
    elif unit1 == "mm^2" and unit2 == "km^2":
        conv = float(num) /(1000000000000)
        print(conv, "km^2")
    elif unit1 == "mm^2" and unit2 == "m^2":
        conv = float(num) /(1000000)
        print(conv, "m^2")
    elif unit1 == "mm^2" and unit2 == "cm^2":
        conv = float(num) /(100)
        print(conv, "cm^2")
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
