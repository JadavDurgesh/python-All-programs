l1 = []

f = open("example2.txt","a")

for i in range(1,3):
    name = input("enter the name :")
    l1.append(name)

f.write("\n"+str(l1))
f.close()