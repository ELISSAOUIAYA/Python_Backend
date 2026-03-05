class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_presenter(self):
        return f"Je suis {self.nom}, {self.age}"

personne1 = Personne("aya", 21)

print(personne1.se_presenter())