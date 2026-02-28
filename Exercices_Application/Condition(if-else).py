# Critères d'accès VIP 
age = int(input("Votre âge : "))
carte_membre = input("Carte membre (oui/non) : ")

# Conversion en booléen
a_carte = carte_membre.lower() == "oui"

# Test combiné avec AND 
if age >= 21 and a_carte:
    print("Accès autorisé !")
    print("Bienvenue dans l'espace premium.")
else:
    print("Accès refusé.")
    if age < 21:
        print("Raison : Âge insuffisant.")
    if not a_carte:
        print("Raison : Pas de carte membre.")