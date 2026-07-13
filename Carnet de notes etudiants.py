import json,time

fichier={
    "etudiants":[
        {"nom":"Modeste","notes":[12,15,10]},
        {"nom":"Sarah","notes":[8,9,7]},
        {"nom":"Paul","notes":[18,14,16]}
    ]
}

with open("etudiants.json","w") as file:
    json.dump(fichier,file)

class Etudiant:
    def __init__(self,nom,notes,moyenne=None):
        self.nom = nom
        self.notes = notes
        self.moyenne = moyenne

    def calculer_moyenne(self):
        self.moyenne=sum(self.notes)/len(self.notes)

    def resultat(self):
        if self.moyenne>=10:
            return "Admis"
        elif self.moyenne<10:
            return "Recale"
        else:
            return self.moyenne

    def get_moyenne(self):
        return self.moyenne

with open("etudiants.json","r") as file:
    fichier=json.load(file)
    bulletin=[]
    for i in fichier["etudiants"]:
        etudiant=Etudiant(i["nom"],i["notes"])
        etudiant.calculer_moyenne()
        print("Nom :",i["nom"],"  Moyenne :",round(etudiant.get_moyenne(),2),"  Statut :",etudiant.resultat())
        bulletin.append({"nom :":i["nom"],"Moyenne :":f"{etudiant.get_moyenne():.2f}","notes :":i["notes"]})
        time.sleep(1)

with open("bulletins.json","w") as file:
    json.dump(bulletin,file)

