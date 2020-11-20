import os
import json


#recupere le chemin vers ce courant scripts
dossier_courant = os.path.dirname(__file__)
chemin_liste = os.path.join(dossier_courant, "liste.json")


#recuperer chemin vers la liste des courses
if os.path.exists(chemin_liste):
    with open(chemin_liste, "r") as f:
        f.seek(0)
        liste_de_courses = json.load(f)
else:
    liste_de_courses = []

affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
"""

option = "0"

while option != "5":
    option = input(affichage)
    #ajouter des element dans la liste
    if option == "1":
        item_a_ajouter = input("Entrez le nom de l'élément à ajouter: ")
        liste_de_courses.append(item_a_ajouter)

    #Retirer un element de liste des courses
    elif option == "2":
        item_a_retirer = input("Entrez le nom de l'élément à enlever: ")
        if item_a_retirer in liste_de_courses:
            liste_de_courses.remove(item_a_retirer)
    #Affichage de la liste
    elif option == "3":
        if liste_de_courses:
            print("\n".join(liste_de_courses))
        else:
            print("La liste ne contient aucun élément.")
    #vider la liste
    elif option == "4":
        liste_de_courses.clear()



#sauvegarde de la list
with open(chemin_liste, "w") as f:
    json.dump(liste_de_courses, f, indent=4)
