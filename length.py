print("""
Covered units:
[ km and m and cm and mm ]
""")
while True:
    num = input("""if you want convert Length
    enter the value: """)
    unit1 = input("which unit do you want it converted from: ")
    unit2 = input("which unit do you want it converted to: ")
    if unit1 == "km" and unit2 == "m":
        conv = float(num) * 1000
        print(conv, "m")
    elif unit1 == "km" and unit2 == "cm":
        conv = float(num) * 100000
        print(conv, "cm")
    elif unit1 == "km" and unit2 == "mm":
        conv = float(num) * 1000000
        print(conv, "mm")
    elif unit1 == "m" and unit2 == "km":
        conv = float(num) * 0.001
        print(conv, "km")
    elif unit1 == "m" and unit2 == "cm":
        conv = float(num) * 100
        print(conv, "cm")
    elif unit1 == "m" and unit2 == "mm":
        conv = float(num) * 1000
        print(conv, "mm")
    elif unit1 == "cm" and unit2 == "m":
        conv = float(num) / 100
        print(conv, "m")
    elif unit1 == "cm" and unit2 == "km":
        conv = float(num) * 0.00001
        print(conv, "km")
    elif unit1 == "cm" and unit2 == "mm":
        conv = float(num) * 10
        print(conv, "mm")
    elif unit1 == "mm" and unit2 == "m":
        conv = float(num) * 0.001
        print(conv, "m")
    elif unit1 == "mm" and unit2 == "km":
        conv = float(num) / 1000000
        print(conv, "km")
    elif unit1 == "mm" and unit2 == "cm":
        conv = float(num) * 0.1
        print(conv, "cm")
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
