mot_de_passe_correct = "python123"

mot_de_passe = input("Veuillez saisir le mot de passe : ")

while mot_de_passe != mot_de_passe_correct:
    print("Mot de passe incorrect. Recommencez.")
    mot_de_passe = input("Veuillez saisir le mot de passe : ")

print("Accès autorisé. Mot de passe correct !")