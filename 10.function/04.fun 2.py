def menu (): 

    menu_display = """
    
                            menu 

                press 1 for addition +
                press 2 for multiplication  *
                press 3 for sub   -
                press 4 for division  /

    
    """
    
    print(menu_display)
    choice = int(input("enter your choice : "))
    if choice == 1:
        addition()

    elif choice == 2:
        multiplication()

    elif choice == 3:
        sub()
    
    elif choice == 4:
        division()
 
    else:
        print(" not valid ....num....")

def addition():

    num1 = int(input("enter the num : "))
    num2 = int(input("enter the num : "))

    ans = num1 + num2
    print("a+b =",ans)

def multiplication():

     num1 = int(input("enter the num : "))
     num2 = int(input("enter the num : "))

     ans = num1 * num2
     print("a+b =",ans)

def sub():

    num1 = int(input("enter the num : "))
    num2 = int(input("enter the num : "))

    ans = num1 - num2
    print("a+b =",ans)

def division():

    num1 = int(input("enter the num : "))
    num2 = int(input("enter the num : "))

    ans = num1 / num2
    print("a+b =",ans)
menu()