import json
import os
import glob # pour récupérer les fichier d'une façon récurssive



#récupérer le chemin du scripts courant 
dossier_courant=os.path.dirname(__file__)

#ajouter les ** dasn le chemin sinon la fonction globe de récurssivité ne marchera pas
dossier=os.path.join(dossier_courant,"**")

files=glob.glob(dossier,recursive=True)#cette variable contient les chemis de chaque flichier(récurssive) dans le dossier 

#récuperer Credit Mutuel du fichier .json sécurité sociale.text

for file in files:
    if file.endswith(".json"):
        with open(file, "r") as f:
            contenu = json.load(f)
            if "Credit Mutuel" in contenu:
                print("le numéro de compte est :",contenu["Credit Mutuel"]["Numero de compte"])
    
    elif file.endswith(".txt"):
        with open(file,"r",encoding="utf_8") as f:
            contenu=f.read()
            if "Numéro de sécurité sociale" in contenu:
                numero_securite_sociale = contenu.split(":")[-1] #elle retourne une liste avec 2 element liste[-1] pour récupérer dernier element
                print(numero_securite_sociale)
           
            