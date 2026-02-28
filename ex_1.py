try:
    age = int(input("Saisissez votre âge : "))

    if age < 0:
        print("Erreur!! L'âge ne peut pas être négatif.")
    elif age <= 12:
        statut = "Enfant"
    elif age <= 17:
        statut = "Adolescent"
    elif age <= 64:
        statut = "Adulte"
    else:
        statut = "Senior"

    if age >= 0:
        print(f"Vous êtes dans la catégorie : {statut}.")

except ValueError:
    print("Erreur!! Entrez un nombre entier valide.")