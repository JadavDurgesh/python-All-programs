i = True

while i:
    age = int(input("enter the age = "))
    if age > 18:
        print("+18 is above....")
    else:
        print("-18 is below....")

    choice = input("do you continue to y/n = ")
    if choice == "y":
       i = True
    else:
       i = False
