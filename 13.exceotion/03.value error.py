try:
    num1 = int(input("enter the num...."))
    num2 = int(input("enter the num ...."))

    print(num1)

except ValueError:
    print("enter the int number..")

except ZeroDivisionError:
    print("can not divide by zero")