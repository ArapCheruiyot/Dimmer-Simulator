class Dimer_light:

    def __init__(self):
        self.ison = True
        self.brightness =0

    def turnon(self):
        self.ison = True
        print("Light turn on")

    def turnoff(self):

        self.ison = False
        print("Light is Off")

    def increas_light(self):
        if self.ison:
            self.brightness = self.brightness +1
            if self.brightness >5:
                self.brightness =0
            print(f"Light Level {self.brightness}")

    def decreas_light(self):
        if self.ison:
            self.brighness = self.brightness -1
            if self.brightness ==0:
                self.brightness =5
            print(f"Light Level {self.brightness}")

    def show(self):

        print(f"light is {self.ison} , and brightness is {self.brightness}")
        

bulb1 = Dimer_light()
bulb2 = Dimer_light()


bulb1.increas_light()
bulb1.increas_light()
bulb1.increas_light()
bulb1.show()

bulb2.increas_light()
bulb2.increas_light()
bulb2.increas_light()
bulb2.show()


