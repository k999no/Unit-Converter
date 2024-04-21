print("""
Covered units:
[ km^3 and m^3 and cm^3 and mm^3 ]
""")
while True:
    print("convert volume")
    num = input("""if you want convert volume
    enter the value: """)
    unit1 = input("enter the unit you have: ")
    unit2 = input("enter the unit you want: ")
    if unit1 == "km^3" and unit2 == "m^3":
        conv = int(num) *(1000*1000*1000)
        print(conv, "m^3")
    elif unit1 == "km^3" and unit2 == "cm^3":
        conv = int(num) *(1000*1000*1000*1000*1000)
        print(conv, "cm^3")
    elif unit1 == "km^3" and unit2 == "mm^3":
        conv = int(num) *(1000*1000*1000*1000*1000*1000)
        print(conv, "mm^3")
    elif unit1 == "m^3" and unit2 == "km^3":
        conv = int(num) /(1000*1000*1000)
        print(conv, "km^3")
    elif unit1 == "m^3" and unit2 == "cm^3":
        conv = int(num) *(100*100*100)
        print(conv, "cm^3")
    elif unit1 == "m^3" and unit2 == "mm^3":
        conv = int(num) *(100*100*100*10*10*10)
        print(conv, "mm^3")
    elif unit1 == "cm^3" and unit2 == "km^3":
        conv = int(num) /(1000*1000*1000*1000*1000)
        print(conv, "km^3")
    elif unit1 == "cm^3" and unit2 == "m^3":
        conv = int(num) /(100*100*100)
        print(conv, "m^3")
    elif unit1 == "cm^3" and unit2 == "mm^3":
        conv = int(num) *(10*10*10)
        print(conv, "mm^3")
    elif unit1 == "mm^3" and unit2 == "km^3":
        conv = int(num) /(1000*1000*1000*1000*1000*1000)
        print(conv, "km^3")
    elif unit1 == "mm^3" and unit2 == "m^3":
        conv = int(num) /(100*100*100*10*10*10)
        print(conv, "m^3")
    elif unit1 == "mm^3" and unit2 == "cm^3":
        conv = int(num) /(10*10*10)
        print(conv, "cm^3")
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
