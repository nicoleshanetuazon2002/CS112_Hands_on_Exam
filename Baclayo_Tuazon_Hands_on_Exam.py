print("***************************************************\n   |          Number System Conversion          |\n***************************************************")
print("")
print("By: Baclayo, Myka Angelie G. | Tuazon, Nicole Shane P.")
print("")
num = eval(input("Enter a number: "))
print("")
print("*********************************************************************************")
print("[1] Decimal Number to Binary Number")
print("[2] Decimal Number to Octal Number")
print("[3] Decimal Number to Hexadecimal Number")
print("*********************************************************************************")
print("")
convert = eval(input("How do you want to convert " + str(num) + "? Enter from [1-3]: "))
print("")
print("*********************************************************************************")
#conversion
if convert == 1:
    res = format(num, "b")
    print("Decimal " + str(convert) + " converted to Binary Number is " + str(res))

elif convert == 2:
    res = format(num, "o")
    print("Decimal " + str(convert) + " converted to Octal Number is " + str(res))

elif convert == 3:
    res = format(num, "h")
    print("Decimal " + str(convert) + " converted to Hexadecimal Number is " + str(res))

else:
    print("Invalid option. Please try again")
print("*********************************************************************************")
