class Mate_Rov:
    def __init__(self,name, hair_color,age,height,weight): # constructor function - called automatically when an object is created
        self.name = name
        self.hair_color = hair_color
        self.age = age
        self.height = height
        self.weight = weight
    def display(self):
        print("Name: ", self.name)
        print("Hair Color: ", self.hair_color)
        print("Age: ", self.age)
        print("Height: ", self.height)
        print("Weight: ", self.weight)
class navigator(Mate_Rov):
    def __init__(self, name, hair_color,age,height,weight,nav_type):
        super().__init__(name, hair_color,age,height,weight)
        self.nav_type = nav_type
    def display(self):
        super().display()
        print("Navigation Type: ", self.nav_type)
aditya = navigator("Aditya", "Black", 14, 5.6, 120, "Software")
aditya.display()
anoushka = navigator("Anoushka", "Black", 15, 5.4, 110, "Software")
anoushka.display()
hannah = navigator("Hannah", "Brown", 16, 5.4, 130, "Mechanical")
hannah.display()
evelyn = navigator("Evelyn", "Black", 15, 5.5, 125, "Electrical")
evelyn.display()
noah = navigator("Noah", "Brown", 14, 5.6, 120, "Mechanical")
noah.display()
brandon = navigator("Brandon", "Black", 15, 5.6, 120, "Software")
brandon.display()
Ken = navigator("Ken", "Black", 14, 5.6, 120, "Software")
Ken.display()
lucas = navigator("Lucas", "Black", 15, 5.6, 120, "Software")
lucas.display()
