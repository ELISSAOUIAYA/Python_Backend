class Personne:
    def __init__(self, nom, age):
        self._nom = nom
        self._age = age

    def se_presenter(self):
        return f"Je suis {self._nom}, {self._age}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valeur):
        if not isinstance(valeur, int):
            raise TypeError("Entrez une val INT")
        if valeur < 0:
            raise ValueError("La val ne peut pas etre moins que 0")
        if valeur > 140:
            raise ValueError("L Age ici est irrealiste")
        self._age = valeur

personne1 = Personne("aya", 21)
personne2 = Personne("Ahmed", 23)
personne3 = Personne("Med", 35)

print(personne1.age)
personne1.age = 23
print(personne1.age)