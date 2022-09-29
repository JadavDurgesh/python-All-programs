year=int(input("enter a year = "))

if year%4==0 or year%400==0 and year%100!=0:
    print("Leap year.....")

else:
    print("Not a leap year.....")


