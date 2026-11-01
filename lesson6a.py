# Parent Class
class Person:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Person Information")

# child class
class Farmer(Person):
    def __init__(self, name, litres):
        super().__init__(name)
        self.litres = litres

    def display_info(self):
        print("Farmer Information")
        # return super().display_info()

farmer1 = Farmer("John", 50)
farmer1.display_info()

# Square = S * S
# Rec = L * W
# Cirlce = pie * r * r