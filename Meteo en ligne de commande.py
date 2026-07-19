import os,argparse,logging,requests,json


 #   GESTION SYSTEME OS
if os.path.exists("resultats_meteo"):
    os.chdir("resultats_meteo")
else:
    os.mkdir("resultats_meteo")
    os.chdir("resultats_meteo")


        #   ARGPARSE
parser = argparse.ArgumentParser(description='Verificateur de meteo')
parser.add_argument("ville", help="La ville a verifier")
parser.add_argument("--unite", default="Celsius",choices=["Celsius","Fahrenheit"],help="l'unite de la temp")

args = parser.parse_args()

        #   LOGGING
logging.basicConfig(filename="Meteo.log", level=logging.DEBUG ,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


        # CREATION DU DICTIONNAIRE
if os.path.exists("infos_meteo.json"):
    with open ("infos_meteo.json","r") as file :
        donnees = json.load(file)
else:
    donnees={

    }
        #   FONCTIONS

# Creation d'une erreur personalisee

class VilleError(Exception):
    pass
class UniteError(Exception):
    pass


def verifier_la_meteo(ville):
    global donnees
    try:
        if not args.ville :
            raise VilleError ("Ville non mentionne")
        else:
            if args.unite == "Celsius":
                meteo=requests.get(f"https://wttr.in/{ville}?format=j1",timeout=5).json()
                result=meteo["current_condition"][0]["temp_C"]
                donnees[args.ville]=result
                logging.info(f"Un utilisateur a consulte la meteo dans la ville de {ville} : {result} {args.unite}")
            elif args.unite == "Fahrenheit":
                meteo = requests.get(f"https://wttr.in/{ville}?format=j1", timeout=5).json()
                result=meteo["current_condition"][0]["temp_F"]
                donnees[args.ville] = result
                logging.info(f"Un utilisateur a consulte la meteo dans la ville de {ville} : {result} {args.unite}")
            else:
                raise UniteError ("Mauvaise unite")
            return f"La meteo dans la ville de {args.ville} est : {result}"
    except (requests.exceptions.ConnectionError,requests.exceptions.Timeout,VilleError,UniteError) as e:
        logging.error(e,exc_info=True)
        return f"Erreur : {e}"

        # APPEL DE LA FONCTION
verifier = verifier_la_meteo(args.ville)

  #   ENREGISTRE FICHIER JSON
with open ("infos_meteo.json","w") as f:
        json.dump(donnees,f)
print(donnees)

print(verifier)

