status = True

while status:
    num =int(input("enter the num = "))
    if num>50:
        print("num is above.....50")
    else:
        print("num is below...50")
    choice =input("do you to continue ..to = y / n")
    if choice == 'y':
        status = True
    else:
        status = False