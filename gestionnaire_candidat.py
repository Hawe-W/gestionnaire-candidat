import random
import math

#===============
#FONCTIONS
#===============

def est_admis(moyenne):
    return moyenne >= 10

def resultat(moyenne):
    if est_admis(moyenne):
        return "Admis"
    else:
        return "Refusé"
    
def calcul_moyenne(note1, note2):
    return (note1 + note2) / 2

#===============
#VARIABLE
#===============

candidats = []

nombre = int(input("Combien de candidats voulez-vous enregistrer ?"))

#===============
#SAISIE DES CANDIDATS
#===============

for i in range(nombre):

    print()
    print("Candidat", i + 1)

    nom = input("Nom : ")
    age = int(input("Age : "))

    note1 = float(input("Note 1 : "))
    note2 = float(input("Note 2 : "))

    moyenne = calcul_moyenne(note1, note2)

    candidat = {
        "nom": nom,
        "age": age,
        "note1": note1,
        "note2": note2,
        "moyenne": moyenne
    }

    candidats.append(candidat)

#===============
#AFFICHAGE COMPLET
#===============

print()
print("------- TOUS LES CANDIDATS -------")

for candidat in candidats:

    decision = resultat(candidat["moyenne"])

    print(
        candidat["nom"],
        "- moyenne :",
        candidat["moyenne"],
        "-",
        decision
    )

#===============
#STATISTIQUE
#===============

total = 0

for candidat in candidats:
    total = total + candidat["moyenne"]

moyenne_generale = total / len(candidats)

print()
print("Moyenne générale :", round(moyenne_generale, 2))

#===============
#EXEMPLE MODULE MATH
#===============

racine = math.sqrt(moyenne_generale)

print("Racine carrée de la moyenne :", round(racine, 2))

#===============
#EXEMPLE MODULE RANDOM
#===============

gagnant = random.choice(candidats)

print()
print("Tirage au sort :")
print("Le gagnant est", gagnant["nom"])

#===============
#SAUVEGARDE FICHIER
#===============

fichier = open("candidats.txt", "a")

for candidat in candidats:

    decision = resultat(candidat["moyenne"])

    fichier.write(
        f"{candidat['nom']} | "
        f"{candidat['age']} | "
        f"Moyenne : {candidat['moyenne']} | "
        f"{decision}\n"
    )

fichier.close()

print()
print("Résultats enregistrés dans candidats.txt")