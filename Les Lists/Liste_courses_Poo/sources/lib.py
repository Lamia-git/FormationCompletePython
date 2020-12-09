import logging
import constante
import os
import json
class Liste(list):
    
    def __init__(self,nom):
        self.nom=nom
    
    def ajouter(self,element):
      
        if not isinstance(element, str):
            raise ValueError("la liste des courses contient que des ")

        if element in self:
            logging.error("on ne peut pas ajouter un element qui existe") 
            return False  
        else:
            self.append(element)
            return True

    def enlever(self,element):
        if element not in self:
            logging.error(" cette element n'existe pas on peut pas le supprimer")
            return False
        else:
            self.remove(element)
            return True
    
    def afficher(self):
        print(f"le liste des {self.nom} :")
        for e in self:
            print(e)
    
    def sauvegarder(self):
        #sauvegarser ma liste dans un fichier json
        chemin=os.path.join(constante.data_path,f"liste{self.nom}.json")

        if not os.path.exists(constante.data_path):
            os.makedirs(constante.data_path)

        with open(chemin, "w")as fic:
            json.dump(self,fic,indent=4)
    
if __name__ == "__main__":
    l = Liste("courses")
    l.ajouter("pomme")
    l.ajouter("carotte")
    l.ajouter("haricos")
    l.ajouter("tomate")
    l.ajouter("banane")
    l.ajouter("pore")

    l.ajouter("potatos")
    l.enlever("xxxx")
    l.sauvegarder()