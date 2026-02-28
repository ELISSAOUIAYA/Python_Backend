# Variables de base
nom = "Laptop"
prix = 2
qte = 10

total = prix * qte

# Approche fragile (CONCATÉNATION)
print(
    "Le produit " + nom + 
    " coûte " + str(prix) + 
    " MAD et vous en voulez " + str(qte) + 
    ". Total: " + str(total) + 
    " MAD."
) 

# Approche moderne et lisible (F-STRINGS - RECOMMANDÉ)
print(f"Le produit {nom} coûte {prix} MAD et vous en voulez {qte}. Total: {total} MAD. ") 