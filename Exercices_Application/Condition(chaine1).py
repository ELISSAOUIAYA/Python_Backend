# Validation d'un nom d'utilisateur 
nom_utilisateur = input("Nom : ")

if nom_utilisateur == "":
    print("Erreur : Le nom ne peut pas être vide !")
else:
    print(f"Bonjour {nom_utilisateur} !")

# Alternative plus pythonique 
if not nom_utilisateur:
    print("Nom requis !")