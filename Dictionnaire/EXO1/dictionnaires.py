from pprint import pprint
employes={}
employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }
            

cles=employes.keys()

for cle in cles:
        #Supprimer l'employer patrick.
    if employes[cle]["prenom"]=="Patrick":
        del employes[cle]
        print("l'employer Patrick nous a quitter")
        break
    
    # changer l'age de julie a 26 ans.
    if employes[cle]["prenom"]=="Julie":
        employes[cle]["age"]=26

    #recupérer l'age de Paul.
    if employes[cle]["prenom"]=="Paul":
        print("Paul a",employes[cle]["age"]," Ans")


pprint(employes)