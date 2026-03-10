class Cafe(Boisson):
    def cout(self):
        return 2.0

    def description(self):
        return "Café simple"

class The(Boisson):
    def cout(self):
        return 1.5

    def description(self):
        return "Thé"

# Test (création d'une boisson simple)
b = Cafe()
print(b.description())
print(b.cout())