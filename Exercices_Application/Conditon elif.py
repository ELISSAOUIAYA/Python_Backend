#  Évaluation de notes avec elif
note = int(input("Votre note : "))

if note >= 16:
    print("Très Bien !")
elif note >= 14:
    print("Bien")
elif note >= 12:
    print("Assez Bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")