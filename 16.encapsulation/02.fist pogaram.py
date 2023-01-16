class mobilestore:
    def __init__(self):
        self.mobile = 1000
        self.__computer = 50000

    def desplay(self):
        print("mobile = ",self.mobile)
        print("computer = ",self.__computer)

obj = mobilestore()
obj.desplay()

obj.mobile = 252000
obj.__computer = 550004

obj.desplay()

obj.change(60000)
obj.desplay()