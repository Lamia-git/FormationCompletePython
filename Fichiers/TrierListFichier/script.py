import os

prenoms= []

#récupérer le chemin du scripts courant 
dossier_courant=os.path.dirname(__file__)
file=os.path.join(dossier_courant,"prenom.txt")
#ouvrire le fichier prenom.text


with open(file,"r",encoding="utf_8") as f:
    lines_contenu=f.read().splitlines()


for line in lines_contenu:
    prenoms.extend(line.split())
    
prenoms_final = [prenom.strip(",. ") for prenom in prenoms]
chemin_final=os.path.join(dossier_courant,"prenom_final")
with open(chemin_final, "w",encoding="utf_8") as f:
    f.write("\n".join(sorted(prenoms_final)))