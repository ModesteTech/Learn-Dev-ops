import logging

logging.basicConfig(filename='log.log', filemode='w', level=logging.INFO, format='%(asctime)s %(message)s')

reussi=0
echec=0

def sauvegarder_fichier(nom_fichier):
    global reussi
    global echec
    logging.info("Debut de la sauvegarde de : {}".format(nom_fichier))
    try:
        if "corrompu" in nom_fichier :
            echec+=1
            raise ValueError ("Fichier corrompu")
        else:
            logging.info("Sauvegarde reussi pour {}".format(nom_fichier))
            reussi+=1
    except ValueError :
        logging.error("le fichier est corrompu",exc_info=True)

fichiers=["rapport.txt","config.yaml","fichier_corrompu.txt","notes.json"]
for fichier in fichiers:
    sauvegarder_fichier(fichier)

logging.info(f"\nFichier sauvegarde : {reussi}\nFichiers Non sauvegarder : {echec}")