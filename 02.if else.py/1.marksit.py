guj=int(input("enter the gujarti  marks: "))
eng=int(input("enter the english  marks: "))
hin=int(input("enter the hindi    marks: "))
eco=int(input("enter the eco      marks: "))
bom=int(input("enter the bom      marks: "))
com=int(input("enter the com       marks: "))

total=guj+eng+hin+eco+bom+com
print("total = ",total)

percentage = total/6
print("percentage = ", percentage)

if percentage >= 85 and percentage <= 100:
    print("A grade")
elif percentage >= 65  and  percentage <= 85:
    print("B grade")
elif percentage >= 50 and percentage <= 65:
    print("C grade")
elif percentage >= 33 and percentage <= 50:
    print("D grade")
else:
    print("fail")
  











