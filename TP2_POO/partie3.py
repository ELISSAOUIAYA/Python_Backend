# Classe de base des ingrédients
class DecorateurBoisson(Boisson):
    def __init__(self, b):
        self._b = b  

# Ingrédient : Lait
class Lait(DecorateurBoisson):
    def cout(self):
        return self._b.cout() + 0.5

    def description(self):
        return self._b.description() + ", Lait"

# Ingrédient : Sucre
class Sucre(DecorateurBoisson):
    def cout(self):
        return self._b.cout() + 0.2

    def description(self):
        return self._b.description() + ", Sucre"


#boisson = Cafe()          # Un café simple
#boisson = Lait(boisson)        # On ajoute du lait
#boisson = Sucre(boisson)       # On ajoute du sucre

#print(boisson.description()) # Affiche: Café simple, Lait, Sucre
#print(boisson.cout())        # Affiche: 2.7 (2.0 + 0.5 + 0.2)