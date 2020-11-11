from base_donnee import Base_donnee
from fichier_mail import Fichier
from apprenant import Apprenant

import mysql.connector as mysqlcon
from unidecode import unidecode as ud

#from apprenant import Apprenant


liste_mails = Fichier().lire_mails("apprenantmail.txt")

for x in range(0,len(liste_mails)):
    liste_mails[x]= [liste_mails[x], liste_mails[x].split("@")[0].split(".")]
print(liste_mails)

for x in range(0,len(liste_mails)):
    liste_mails[x][1][0]= liste_mails[x][1][0].replace('-', ' ').replace("'", ' ')
    liste_mails[x][1][1]= liste_mails[x][1][1].replace('-', ' ').replace("'", ' ')
print(liste_mails)



base = Base_donnee()
bdd = base.connection(8081, 'localhost', 'root', 'root', 'binomotron')

curseur = base.creer_curseur(bdd)

print(bdd.is_connected())

liste_apprenants = []
curseur.execute('SELECT id_apprenant, nom, prenom, mail FROM apprenants;')

for x in curseur.fetchall():
    liste_apprenants.append(x)

objets = []

for x in liste_apprenants:
    nouvelle_instance = Apprenant(x)
    objets.append(nouvelle_instance)

for x in range(0,len(objets)):
    for y in range(0,len(liste_mails)):
        if ud(objets[x].prenom.lower()).replace("'", '') == liste_mails[y][1][0]:
            if ud(objets[x].nom.lower()).replace("'", '') == liste_mails[y][1][1]:
                objets[x].mail = liste_mails[y][0]

for x in range(0,len(objets)):
    curseur.execute(f"UPDATE apprenants SET mail = '{objets[x].mail}' WHERE id_apprenant = {objets[x].id};")
    bdd.commit()

for x in range(0,len(objets)):
    print(objets[x].__dict__.items())