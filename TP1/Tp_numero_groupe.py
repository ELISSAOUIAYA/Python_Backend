Donnees = [
    ("Sara", "Math", 12, "G1"), ("Sara", "Info", 14, "G1"), ("Ahmed", "Math", 9, "G2"),
    ("Adam", "Chimie", 18, "G1"), ("Sara", "Math", 11, "G1"), ("Bouchra", "Info", "abc", "G2"), 
    ("", "Math", 10, "G1"), ("Yassine", "Info", 22, "G2"), ("Ahmed", "Info", 13, "G2"),
    ("Adam", "Math", None, "G1"), ("Sara", "Chimie", 16, "G1"), ("Adam", "Info", 7, "G1"),
    ("Ahmed", "Math", 9, "G2"), ("Hana", "Physique", 15, "G3"), ("Hana", "Math", 8, "G3")
]

# Partie 1 : Validation des données

def valider(enregistrement):
    nom, matiere, note, groupe = enregistrement
    if not nom or str(nom).strip() == "":
         return False, "Nom vide"

    if not matiere or str(matiere).strip() == "":
         return False, "Matière vide"

    if not groupe or str(groupe).strip() == "":
         return False, "Groupe vide"

    try:
        val_note = float(note)
        if not (0 <= val_note <= 20):
            return False, f"Note hors intervalle [0,20] : {val_note}"
    except (ValueError, TypeError):
        return False, f"Note non numérique : {note}"
    return True, ""

valides = []
erreurs = []
doublons_exact = set() # Pour détecter les doublons exacts
vus = set()            # Pour suivre les enregistrements déjà vus afin de détecter les doublons exacts

for ligne in Donnees:
    if ligne in vus:
        doublons_exact.add(ligne)
        continue 
    vus.add(ligne)                       # On valide la ligne seulement si ce n'est pas un doublon exact
    Valide, raison = valider(ligne)      
    if Valide:
        valides.append((ligne[0], ligne[1], float(ligne[2]), ligne[3])) # On convertit la note en float pour les calculs futurs
    else:
        erreurs.append({"ligne": ligne, "raison": raison})              #On ajoute la ligne à la liste des erreurs avec la raison de l'échec de validation

# Partie 2 : Structuration des données

Tmatieres = {enreg[1] for enreg in valides}  
notes_etudiant = {} 
etudiants_groupe = {}

for nom, matiere, note, groupe in valides:                    # Structure Etudiant -> Matière -> [Notes]    
    if nom not in notes_etudiant:
        notes_etudiant[nom] = {}
    if matiere not in notes_etudiant[nom]:                  
        notes_etudiant[nom][matiere] = []
    notes_etudiant[nom][matiere].append(note)
    
    if groupe not in etudiants_groupe:                         # Structure Groupe -> {Etudiants}                     
        etudiants_groupe[groupe] = set()
    etudiants_groupe[groupe].add(nom)

# Partie 3 : Calcul des moyennes

def somme(liste_notes):
    if not liste_notes: return 0
    return liste_notes[0] + somme(liste_notes[1:])

def calculer_moyenne(liste_notes):
    if not liste_notes: return 0
    return somme(liste_notes) / len(liste_notes)              

resultats_etudiants = {}                                   # Structure Etudiant -> {"moyenne_generale": x, "details": {Matière: moyenne}}
for nom, matieres in notes_etudiant.items():                              
    moyennes_mtr = {m: calculer_moyenne(n) for m, n in matieres.items()}  
    Notes = [n for l in matieres.values() for n in l]
    resultats_etudiants[nom] = {
        "moyenne_generale": round(calculer_moyenne(Notes), 2),
        "details": moyennes_mtr
    }

# Partie 4 : Détection d'anomalies

SEUIL_GRP_FAIBLE = 10.0
alertes = {"doublons": [], "incomplets": [], "grps_faibles": [], "ecarts": []}

for nom, mtr_etud in notes_etudiant.items():
    for m, n in mtr_etud.items():                                       #Doublons exacts
        if len(n) > 1: alertes["doublons"].append(f"{nom} ({m})")


    #  Vérifier que l'étudiant a des notes pour toutes les matières présentes dans les données
    if set(mtr_etud.keys()) != Tmatieres:
        alertes["incomplets"].append(nom)
        
    # Vérifier les écarts de notes pour chaque étudiant
    toutes_n = [n for l in mtr_etud.values() for n in l]
    if max(toutes_n) - min(toutes_n) > 10:
        alertes["ecarts"].append(nom)

# Calculer la moyenne de chaque groupe et détecter les groupes faibles

for grp, etuds in etudiants_groupe.items():
    notes_grp = [n for e in etuds for m in notes_etudiant[e].values() for n in m]
    if calculer_moyenne(notes_grp) < SEUIL_GRP_FAIBLE:
        alertes["grps_faibles"].append(grp)

# Affichage des résultats

print(f"Lignes valides : {len(valides)} | Erreurs détectées : {len(erreurs)}")
print(f"Moyennes : {resultats_etudiants}")
print(f"Alertes : {alertes}")