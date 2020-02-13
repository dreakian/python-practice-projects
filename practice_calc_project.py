def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def mod(x, y):
    return x % y

calc = True
while calc:


    print("""\nMathematical calculations:

    1. Add        2. Subtract
    3. Multiply   4. Divide
    5. Mod""")

    user_mathematical_calculation = int(input("\nChoose what mathematical calculation you would like to run: "))

    if user_mathematical_calculation == 1:
        print("\nYou've chosen the addition function!")

    elif user_mathematical_calculation == 2:
        print("\nYou've chosen the subtraction function!")

    elif user_mathematical_calculation == 3:
        print("\nYou've chosen the multiplication function!")

    elif user_mathematical_calculation == 4:
        print("\nYou've chosen the division function!")

    elif user_mathematical_calculation == 5:
        print("\nYou've chosen the modulo function!")

    num_one = float(input("\nEnter your first number: "))
    num_two = float(input("\nEnter your second number: "))

    if user_mathematical_calculation == 1:
        print("/nYou've chosen the addition function!")
        add(num_one, num_two)
        print(str(num_one) + " + " + str(num_two) + " = " + str(add(num_one, num_two)))
        print("==============================================================================================")

    elif user_mathematical_calculation == 2:
        print("/nYou've chosen the subtraction function!")
        subtract(num_one, num_two)
        print(str(num_one) + " - " + str(num_two) + " = " + str(subtract(num_one, num_two)))
        print("==============================================================================================")

    elif user_mathematical_calculation == 3:
        print("/nYou've chosen the multiplication function!")
        multiply(num_one, num_two)
        print(str(num_one) + " * " + str(num_two) + " = " + str(multiply(num_one, num_two)))
        print("==============================================================================================")

    elif user_mathematical_calculation == 4:
        print("/nYou've chosen the division function!")
        divide(num_one, num_two)
        print(str(num_one) + " / " + str(num_two) + " = " + str(divide(num_one, num_two)))
        print("==============================================================================================")

    elif user_mathematical_calculation == 5:
        print("/nYou've chosen the module function!")
        mod(num_one, num_two)
        print(str(num_one) + " % " + str(num_two) + " = " + str(mod(num_one, num_two)))
        print("==============================================================================================")

    else:
        print("\nYou have entered an incorrect entry. Please try again.")
        print("==============================================================================================")
        input(str("\nChoose what mathematical calculation you would like to run: "))






