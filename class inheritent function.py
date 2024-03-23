class placements():
    def info(self):
        print("1072")
class dept(placements):
    def display(self):
        print("all depts")
class pragati(dept,placements):
    def welcome(self):
        print("welcome",)
obj=pragati()
obj.welcome()
obj.display()
