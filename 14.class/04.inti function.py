class car :
    def __init__(self,color,brand,wheel,model):
        self.color = color
        self.brand = brand
        self.wheel = wheel
        self.model = model

    def display(self):
        
        print(self.color)
        print(self.brand)
        print(self.wheel)
        print(self.model)
    
t1 = car("white","TATA","4","NANO")
t1.display()

t2 = car("black","hundai",4,"santro")
t2.display()