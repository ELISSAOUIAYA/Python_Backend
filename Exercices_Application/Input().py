# Demander l'âge et le convertir en deux étapes
age_str = input("Votre âge : ")
age = int(age_str) # Conversion indispensable

# Conversion en une seule ligne (plus rapide)
age = int(input("Votre âge : ")) 

# Maintenant on peut calculer
dans_10_ans = age + 10
print(f"Dans 10 ans: {dans_10_ans}") 


#  ERREUR FRÉQUENTE (oubli de la conversion)
# age = input("Votre âge : ") # "25"
# dans_10_ans = age + 10 
# Résultat : TypeError car on ne peut pas additionner du texte ("25") et un nombre (10)