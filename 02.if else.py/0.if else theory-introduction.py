'''
control statments:

3 types of control statments:

1.conditional statments
2.looping statments
3.jumping statments

 1.conditional statments

 ==>if statments
 ==>if .. else statments
 ==>nested if statments
 ==>elif statments


==> if statments: if condition goes true it will execute the statments
==> if syntax:
 if condition:
    statments

==> if...else syntax
 if condition:
    statments
 else:
    statments   

==> if...elif...else syntax
   if condition:
    statments
    
   elif condition:
    statments

   elif condition:
    statments 

   else:
    statments  

'''

# e.g : 1

num=int(input("enter number:"))

if num>18:
    print("you are eligible for voting")

else:
    print("you are below 18")    