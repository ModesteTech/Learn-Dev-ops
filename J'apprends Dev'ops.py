import json,requests

donnees={
    "sites":[
        "https://www.google.com",
        "https://www.github.com",
        "https://www.siteinexistant12345.com",
    ]
}

with open("sites.json","w") as file:
    json.dump(donnees,file)

class Site:
    def __init__(self,url,status=None):
        self.url = url
        self.status = status

    def verifier(self):
        try:
            reponse = requests.get(self.url,timeout=5)
            if reponse.status_code==200:
                self.status = "EN L1GNE"
            else:
                self.status = "HORS LIGNE"
        except requests.exceptions.Timeout:
            print("Le serveur ne repond pas")
        except requests.exceptions.ConnectionError:
            print("Pas de connexion internet")

    def get_status(self):
        return self.status

with open("sites.json","r") as file:
    sites = json.load(file)
    resultat=[]
    for url in sites["sites"]:
        site=Site(url)
        site.verifier()
        print(site.get_status())
        resultat.append({"url:":url,"statut":site.get_status()})
with open("resultats.json","w") as file :
    json.dump(resultat,file)
