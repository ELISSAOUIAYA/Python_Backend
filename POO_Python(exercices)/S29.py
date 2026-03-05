class Etudiant:
    def __init__(self):
        self.__cin = "LK228811"
        self._cne = "P12475962"

    def afficher_prive(self):
        return self.__cin

aya = Etudiant()
print(aya.afficher_prive())
print(aya._cne)