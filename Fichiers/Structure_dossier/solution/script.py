import os


"""parcourir le dictionnaire
Pour chaque cle on crée un dossier 
pour chaque valeurs on creer des sous dossiers
"""
#recupérer le chemin vers le script courant
dossier_courant = os.path.dirname(__file__)
print(dossier_courant)

d= {"Films": ["Le seigneur des anneaux",
			   "Harry Potter",
			   "Moon",
			   "Forrest Gump"],
	 "Employes": ["Paul",
	 		      "Pierre",
				  "Marie"],
	 "Exercices": ["les_variables",
	 			   "les_fichiers",
				   "les_boucles"]}

#Parcourir le dictionnaire
cles = d.keys()
for cle in cles:
    
    nouveau_chemin=os.path.join(dossier_courant,cle) #contruire le nouveau chemin de chaque repertoir.
    
    if not os.path.exists(nouveau_chemin): #verifier si le dossier n'existe pas.
        os.makedirs(nouveau_chemin)
    
    for element in d[cle]: #Parcourir la liste des values pour chaque cle.
        chemin_sous_repo=os.path.join(nouveau_chemin,element)
        if not os.path.exists(chemin_sous_repo): #verifier si le sous dossier n'existe pas.
            os.makedirs(chemin_sous_repo)
