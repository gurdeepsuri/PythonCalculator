def calculate():
    print("Welcome to our Calculater Program \n")
    print("Please Select on of the Arithmetic Operation -\n"
          "1. Add \n"
          "2. Subtract \n"
          "3. Multiply \n"
          "4. divide \n")

    while True:
        try:
            operation = int(input("Select any one operation from above (1,2,3,4):"))
            if operation not in (1, 2, 3, 4):
                print("Invalid Input. \n "
                      "Please Select on of the operation values (1,2,3,4)")
            else:
                break
        except ValueError:
            print("Please Enter a Valid Number")

    while True:
        try:
            number_1 = float(input("Please enter a number: "))
            number_2 = float(input("Please enter another number: "))
            if operation == 1:
                print(number_1, " + ", number_2, " = ", number_1 + number_2)
            elif operation == 2:
                print(number_1, " - ", number_2, " = ", number_1 - number_2)
            elif operation == 3:
                print(number_1, " * ", number_2, " = ", number_1 * number_2)
            elif operation == 4:
                try:
                    print(number_1, " \ ", number_2, " = ", number_1 / number_2)
                except ZeroDivisionError:
                    print("Number Cannot be Divizible by 0")
            break
        except ValueError:
            print("Please Enter a Valid Number")
    again()


def again():
    calc_again = input("If you want to calculate again select Y else to exit select N: ")

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print("Thank you for using our calculater")
    else:
        again()


calculate()
