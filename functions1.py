class shopping:
    def dresstype(self,type):
        self.s=type
    def d_price(self,price):
        self.h=price
    def d_size(self,size):
        self.g=size
    def display(self):
        print(self.s,self.h,self.g,)
geetha=shopping()
geetha.dresstype("jeans")
geetha.d_price(20)
geetha.d_size("L")
geetha.display()
