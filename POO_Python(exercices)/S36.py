class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class Salarie(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)
        self.salaire = salaire

class Etudiant(Personne):
    def __init__(self, nom, age, cne):
        super().__init__(nom, age)
        self.cne = cne

class Doctorant(Salarie, Etudiant):
    def __init__(self, nom, age, salaire, cne, sujet_these):
        Salarie.__init__(self, nom, age, salaire)
        Etudiant.__init__(self, nom, age, cne)
        self.sujet_these = sujet_these

    def afficher_infos(self):
        print(f"Nom: {self.nom}, Age: {self.age}")
        print(f"Salaire: {self.salaire}, CNE: {self.cne}")
        print(f"Thèse: {self.sujet_these}")

doc = Doctorant("Aya", 23, 8000, "M123456", "Intelligence Artificielle")
doc.afficher_infos()