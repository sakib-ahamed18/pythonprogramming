#distance
print("press 1 for distance conversion")
print("press 2 for temperature conversion")
print("press 3 for quantity conversion")
choice = int(input("enter the choice"))
if choice == 1:
    print("press 1 to convert cm to m")
    print("press 2 to convert m to cm")
    choice2 = int(input("enter your choice"))
    if choice2 == 1:
        cm = int(input("enter centimeters"))
        meter = cm/100
        print(cm, "centimeters is equal to",meter, "meters")
    elif choice2 == 2:
        meter = int(input("enter meters"))
        cm = meter * 100
        print(meter, "meters is equal to",cm, "centimeters")
    else:
        print("invalid operator")
#temperature
elif choice == 2:
    print("press 1 to convert celsius to fahrenheit")
    print("press 2 to convert fahrenheit to celsius")
    choice3 = int(input("enter choice"))
    if choice3==1:
        celsius = int(input("enter celsius"))
        fahrenheit = (celsius * (9/5))+32
        print(celsius,"C is equql to",fahrenheit,"F")
    elif choice3==2:
        fahrenheit=int(input("enter fahrenheit"))
        celsius= (fahrenheit-32)*(5/9)
        print(fahrenheit,"F is equal to",celsius,"C")
    else:
        print("invalid operator")
#quantity
elif choice==3:
    print("press 1 to convert ml to l")
    print("press 2 to convert l to ml")
    choice4=int(input("enter choice"))
    if choice4==1:
        ml=int(input("enter ml"))
        l=ml/1000
        print(ml,"ml is equal to",l,"litres")
    elif choice4==2:
        l=int(input("enter litres"))
        ml=l*1000
        print(l,"litres is equal to",ml,"ml")
    else:
        print("invalid operator")
else:
    print("invalid operator")







