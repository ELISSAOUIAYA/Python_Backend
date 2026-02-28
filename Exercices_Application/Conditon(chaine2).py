# Filtrage de contenu 
message = input("Votre message : ")
mots_interdits = ["spam", "pub", "promo"]

# Vérification simple avec 'in'
if "@" in message:
    print("Email détecté dans le message")

# Recherche de mots interdits avec une boucle
for mot in mots_interdits:
    if mot in message.lower():
        print(f"Contenu suspect : '{mot}' détecté")
        break