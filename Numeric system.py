while True:
    dec = int(input("Enter a decimal value:"))

    print(bin(dec), "in binary")
    print(oct(dec), "in octal")
    print(hex(dec), "in hexadecimal")
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
