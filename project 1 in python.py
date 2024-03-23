class classroom:
    def __init__(self):
        self.cgst=0.18
        self.sgst=0.18
        self.insurance=100000
    def company(self):
        while True:
            print("select a car from ferrari mahindra voivo")
            self.n=input("select a car")
            if self.n=="Ferrari":
                print("welcome to Ferrari")
                self.model()
                break
            elif self.n=="volvo":
                print("welcome to voivo")
                self.model()
                break
            elif self.n=="mahindra":
                print("welcome to mahindra")
                self.model()
                break
            else:
                print("enter valid data")
    def model(self):
        if self.n=="Ferrari":
            while True:
                print("select a car from GTB ROMA")
                self.choice=input("your desired car")
                if self.choice=="GTB":
                    self.price(self.choice)
                    break
                elif self.choice=="ROMA":
                    self.price(self.choice)
                    break
                else:
                    print("enter available model")
        if self.n=="volvo":
            while True:
                print("select a car from xc90 s90")
                self.choice=input("your desired car")
                if self.choice=="xc90":
                    self.price(self.choice)
                    break
                elif self.choice=="s90": 
                    self.price(self.choice)
                    break
                else:
                    print("enter a valid model")


        if self.n=="mahindra":
            while True:
                print("select a car from SCORPIO THAR")
                self.choice=input("your desired car")
                if self.choice=="SCORPIO":
                    self.price(self.choice)
                    break
                elif self.choice=="THAR f ":
                    self.price(self.choice)
                    break
                else:
                    print("enter available model")
            
    def price(self,choice ):
        if choice=="GTB":
            self.price=24000000
        elif choice=="ROMA":
            self.price==2356780
        elif choice=="xc90":
            self.price=3575670
        elif choice=="s90":
            self.price=34234689
        elif coice=="SCORPIO":
            self.price=43567898
        elif choice=="THAR":
            self.price==123456789
        tot_p = self.price+(self.sgst)*self.price+(self.cgst)*self.price+self.insurance
        print(tot_p)
obj=classroom()
obj.company()
        
