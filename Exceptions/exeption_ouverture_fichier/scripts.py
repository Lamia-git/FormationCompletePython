import os

#demander a lu'tilisateur de saisir un chemin du fichier 

fichier=input("veuillez saisir un chemin")
#gérer l'existance du fichier   FileNotFoundError
#s'il est existe, est ce que python peut l'ouvrir UnicodeDecodeError:
#il faut fermer le fichier    



try:
    file=open(fichier,"r",encoding="utf_8")
    contenu=file.read()
    print(contenu)

except FileNotFoundError :
    print("Le fichier n'existe pas")

except UnicodeDecodeError:
    print("le format du fichier n'est pas valide")
else:
    file.close()