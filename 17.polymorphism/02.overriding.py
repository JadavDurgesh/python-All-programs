class A:
    def display(self):
        print("class A ")

class B(A):
    
    def display(self):
        A.display(self)
        print("class B")


obj = B()
obj.display()