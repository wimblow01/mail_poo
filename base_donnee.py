import mysql.connector as mysqlcon

class Base_donnee:

    def connection (self, port, host, user, password, base):
        bdd = mysqlcon.connect(port=port,
                                    host= host,
                                    user= user,
                                    password= password,
                                    database= base)
        return bdd

    def creer_curseur(self, bdd):
        curseur = bdd.cursor()
        return curseur

    def ajout_colonne(self, curseur, nom_table, nom_colonne):
        query = f"ALTER TABLE {nom_table} ADD COLUMN {nom_colonne} VARCHAR(255)"
        curseur.execute(query)
        del query

""" #Connexion à notre serveur sql et création de notre objet connecteur :
bdd = mysqlcon.connect(port=8081,
                                    host='localhost',
                                    user= 'root',
                                    password= 'root')

#Création de notre objet curseur sql :
mycursor = bdd.cursor()

#Création de notre database :
mycursor.execute("CREATE DATABASE Binomotron")

#Connexion à notre db nouvellement crée :
bdd.config(database = 'Binomotron')
bdd.reconnect()

#Régénération du curseur sur la nouvelle connexion :
mycursor = bdd.cursor()

#Création de notre table d'apprenants :
mycursor.execute("CREATE TABLE apprenants (id_apprenant INT(11) PRIMARY KEY AUTO_INCREMENT, nom VARCHAR(50), prenom VARCHAR(50), photo VARCHAR(50))")


#Insertion de tout le monde dans la table :
mycursor.execute("INSERT INTO apprenants (nom, prenom, photo)\
    VALUES \
    ('Bonneau', 'Amaury', NULL),\
    ('Pertron', 'Aude ', NULL),\
    ('Le Berre', 'Baptiste', NULL),\
    ('Le Goff', 'Baptiste', NULL),\
    ('Guillen', 'Celine', NULL),\
    ('Karfaoui', 'Christelle', NULL),\
    ('Mbarga Mvogo', 'Christian', NULL),\
    ('Cloatre', 'Erwan', NULL),\
    ('Moulard', 'Eva', NULL),\
    ('Verpoest', 'Guillaume', NULL),\
    ('Ibanni', 'Jamal', NULL),\
    ('Le Joncour', 'Jérémy', NULL),\
    ('Furiga', 'Julien', NULL),\
    ('Maintier', 'Ludivine', NULL),\
    ('Bokalli', 'Luigi', NULL),\
    ('Le Moal', 'Patricia', NULL),\
    ('Sabia', 'Paul', NULL),\
    ('Hergoualc''h', 'Pereg', NULL),\
    ('Rioual', 'Ronan', NULL),\
    ('Chaigneau', 'Thomas', NULL);")
bdd.commit()

#Création de notre table de groupes :
mycursor.execute("CREATE TABLE groupes (id_groupe INT(11) PRIMARY KEY AUTO_INCREMENT, libelle VARCHAR (50));")

#Création de notre table de projets :
mycursor.execute("CREATE TABLE projets (id_projet INT(11) PRIMARY KEY AUTO_INCREMENT, libelle VARCHAR (50), date_debut DATE, date_fin DATE);")

#Création de notre table intermédaire qui relie toutes les autres :
mycursor.execute("CREATE TABLE apprenants_groupes (\
    id_apprenant int(11),\
    id_groupe int(11),\
    id_projet int(11),\
    FOREIGN KEY (id_apprenant) REFERENCES apprenants(id_apprenant),\
    FOREIGN KEY (id_groupe) REFERENCES groupes(id_groupe),\
    FOREIGN KEY (id_projet) REFERENCES projets(id_projet)\
    );")
 """