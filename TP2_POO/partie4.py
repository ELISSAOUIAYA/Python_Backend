class Combo(Boisson):
    def __init__(self, b1, b2):
        self.b1 = b1
        self.b2 = b2

    def cout(self):
        return self.b1.cout() + self.b2.cout()

    def description(self):
        return self.b1.description() + " + " + self.b2.description()

#on ajoute la méthode __add__ à la classe Boisson pour pouvoir faire des combinaisons 

#m1 = Cafe()
#m2 = Sucre(The())

#menu = m1 + m2 

#print(menu.description()) # Café simple + Thé, Sucre
#print(menu.cout())        # 3.7 (2.0 + 1.5 + 0.2)