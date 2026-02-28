contacts = ["Sanae", "Aya", "Sara"]

continuer = True

while continuer:
    print("\n MENU GESTION DE CONTACTS")
    print(" Ajouter un contact")
    print(" Afficher tous les contacts")
    print(" Quitter le programme")
    
    choix = input("\n Choisissez une option (1-3) : ")

    if choix == "1":
        new_name = input("Entrez le nom du nouveau contact : ")
        contacts.append(new_name)
        print(f" {new_name} a été ajouté avec succès.")

    elif choix == "2":
        print("\nListe de vos contacts :")
        if not contacts:
            print("Le carnet d'adresses est vide.")
        else:
            for index, contact in enumerate(contacts, start=1):
                print(f"{index}. {contact}")

    elif choix == "3":
        print("Fermeture du programme.")
        continuer = False 

    else:
        print("Option invalide, veuillez recommencer.")