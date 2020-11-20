import os
import glob
import shutil


extentions={".mp3": "Musique",
              ".wav": "Musique",
              ".mp4": "Videos",
              ".mov": "Videos",
              ".jpeg": "Images",
              ".jpg": "Images",
              ".png": "Images",
              ".pdf": "Documents"}

#récupérer le chemin du scripts courant Chemin du dossier a trier
dossier_courant="c:/Users/pc/Desktop/UdemyPython/ExoPython/Trier_fichier/tri_fichiers_sources"

#ajouter les ** dasn le chemin sinon la fonction globe de récurssivité ne marchera pas
dossier=os.path.join(dossier_courant,"*")

files=glob.glob(dossier,recursive=True)#cette variable contient les chemis de chaque flichier(récurssive) dans le dossier 

for file in files:
    #recuperer l'extention de chaque fichier
    extention=os.path.splitext(file)[-1]
    dossier=extentions.get(extention)
    if dossier:
        chemin_dossier=os.path.join(dossier_courant,dossier)
        os.makedirs(chemin_dossier,exist_ok=True)
        shutil.move(file,chemin_dossier)
    