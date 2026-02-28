try:
    nbr1 = float(input("Entrez le premier nombre : "))
    nbr2 = float(input("Entrez le second nombre : "))

    print("\n Choisissez une opération ")
    print("1 : Addition ")
    print("2 : Soustraction ")
    print("3 : Multiplication ")
    print("4 : Division ")
    
    choix = input("\nVotre choix (1/2/3/4) : ")

    if choix == "1":
        resultat = nbr1 + nbr2
        print(f"Résultat : {nbr1} + {nbr2} = {resultat}")
        
    elif choix == "2":
        resultat = nbr1 - nbr2
        print(f"Résultat : {nbr1} - {nbr2} = {resultat}")
        
    elif choix == "3":
        resultat = nbr1 * nbr2
        print(f"Résultat : {nbr1} * {nbr2} = {resultat}")
        
    elif choix == "4":
        if nbr2 == 0:
            print("Erreur!! La division par zéro est impossible.")
        else:
            resultat = nbr1 / nbr2
            print(f"Résultat : {nbr1} / {nbr2} = {resultat}")
            
    else:
        print("Erreur!! Choix d'opération invalide.")

except ValueError:
    print("Erreur!! Veuillez saisir des nombres valides.")