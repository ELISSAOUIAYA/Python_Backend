class Caramel(DecorateurBoisson):
    def cout(self):
        return self._b.cout() + 0.8  

    def description(self):
        return self._b.description() + ", Caramel"

def ticket(obj):
    print(f"Commande : {obj.description()}")
    print(f"Prix : {obj.cout()}€")


