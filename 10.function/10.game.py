import random

computer = random.randint(1,100)



status = True

while status:
        
        user = int(input("enter the num..."))
        if user >  computer:
            print("hint guess lower num ...")
        elif user < computer:
            print("hint guess upper num....;")
        else:
            print("you got it")
        
            status = False