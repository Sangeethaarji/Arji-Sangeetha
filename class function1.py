class f15:
    def light(self,low voltage):
        print("light is switching")
    def fan(self,speed):
        print("fan is on")
        self.s=speed
    def cpu(self):
        print("powering on the system")
        print(self.s)
geetha=f15()
geetha.light()
geetha.fan(4)
geetha.cpu()
