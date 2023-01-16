print("                        jay bhavani ")
print("")
print("")

print("          Menu   ")
print("")
print("         1)vadapav    ",      30)
print("         2)bhel       ",      40)
print("         3)sendwich   ",      60)
print("         4)full megi  ",     100)
print("         5)pizza      ",     180)


n = True

while n:
    customer =input("enter the product ....vadapav,bhel,sendwich,full megi,pizza  = ")
    nag      =int(input("enter the qty = "))

    if customer == 'vadapav':
        print("vadapav", 30*nag)

    elif customer == 'bhel':
        print("bhel", 40*nag)

    elif customer == 'sendwich':
        print("sendwich", 60*nag)

    elif customer == 'full megi':
        print("full megi", 100*nag)

    elif customer == 'pizza':
        print("pizza", 180*nag)

    else:
        print("not valid products.....")

    choich = input("do you continue ....y/n..")

    if choich == 'y':
        n = True
    else:
        n = False

    customer.index(total)
    print(total)