from dataclasses import dataclass

@dataclass
class Client:
    nom: str
    numero: int
    pts: int  


# Création d'un client
#c1 = Client("Aya", 101, 50)
#print(c1)   # Affiche: Client(nom='Aya', numero=101, pts=50)