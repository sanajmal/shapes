choice = ""
ch = ""
while True:
    print("---------SHAPE CALCULATIONS---------")
    print("------------------------------------")
    print("------------------------------------")
    print("CHOOSE YOUR OPTIONS")
    print("1.Perimeter")
    print("2.Area")
    print("3.Exit")
    choice = input("SELECT YOUR CHOICE")
    if choice == '1':
        print("YOU CHOOSE PERIMETER")
        while True:
            print("-------------------------")
            print(".....ENTER YOUR CHOICE....")
            print("1.CIRCLE")
            print("2.SQUARE")
            print("3.RECTANGLE")
            print("4.TRIANGLE")
            print("5.EXIT")
            print("--------------------------")
            # con = input("...DO YOU WANT TO CONTINUE....")
            # if con == "yes" or  con == "y" or con == "Y":

            ch = input("WHICH SHAPE DO YOU WANT")

            if ch == '1':
                print(" YOU CHOOSE CIRCLE")
                r = float(input("Input Radius : "))
                perimeter = round(2 * 3.14 * r, 2)
                print("Perimeter of Circle: ", perimeter)



            elif ch == '2':
                print("YOU CHOOSE SQUARE")
                s = int(input("Side : "))
                perimeter = 4 * s
                print("Perimeter of square : ", perimeter)

            elif ch == '3':
                print("YOU CHOOSE RECTANGLE")
                l = int(input("Length : "))
                w = int(input("Width : "))
                perimeter = 2 * (l + w)
                print("Perimeter of Rectangle : ", perimeter)

            elif ch == '4':
                print("YOU CHOOSE TRIANGLE")
                a = int(input("Side 1 : "))
                b = int(input("Side 2 : "))
                c = int(input("Side 3 : "))
                perimeter = a + b + c
                print("Perimeter of Triangle : ", perimeter)

            elif ch == '5':
                print("....YOU ARE EXITED.....")
                break

            c = input("DO YOU WANT TO CONTINUE..")
            if c == "yes" or c == "y" or c == "Y":
                continue

    elif choice == '2':
        print("you choose area")

        while True:
            print("-------------------------")
            print(".....ENTER YOUR CHOICE....")
            print("1.CIRCLE")
            print("2.SQUARE")
            print("3.RECTANGLE")
            print("4.TRIANGLE")
            print("5.EXIT")
            print("--------------------------")
            choice = input("WHICH SHAPE DO YOU WANT")

           # while True:
            if choice == '1':
                print(" YOU CHOOSE CIRCLE")
                r = int(input("Enter circle's radius length: "))
                pi = 3.14
                circle_area = pi * r * r
                print(f"The area of circle is {circle_area}.")
                print("--------------------------------------")
                    # input("DO YOU WANT TO CONTINUE")
                    # continue

            elif choice == '2':
                print("YOU CHOOSE SQUARE")
                s = int(input("Enter square's side length: "))
                square_area = s * s
                print(f"The area of square is {square_area}. ")
                print("--------------------------------------")

            elif choice == '3':
                print("YOU CHOOSE RECTANGLE")
                l = int(input("Enter rectangle's length: "))
                b = int(input("Enter rectangle's breadth: "))
                rectangle_area = l * b
                print(f"The area of rectangle is {rectangle_area}.")
                print("------------------------------------------")


            elif choice == '4':
                print("YOU CHOOSE TRIANGLE")
                h = int(input("Enter triangle's height: "))
                b = int(input("Enter triangle's breadth: "))
                triangle_area = 0.5 * b * h
                print(f"The area of triangle is {triangle_area}.")
                print("-----------------------------------------")

            elif choice == '5':
                print("....YOU ARE EXITED.....")
                break

            c = input("DO YOU WANT TO CONTINUE..")
            if c == "yes" or c == "y" or c == "Y":
                continue

    elif choice == '3':
        print("-----YOU ARE EXITED-----")
        print("------------------------")
        break