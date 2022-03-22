import random
import sqlite3

lettre = "abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@-_$%&#"


def generation_mdp(long):
    password = ""
    for i in range(0, long):
        mot = random.choice(lettre)
        password = password + mot
    return password


def ajout_bdd(site, mdp):
    try:
        connection = sqlite3.connect("base.db")
        cursor = connection.cursor()

        new_mdp = (cursor.lastrowid, site, mdp)
        cursor.execute('INSERT INTO mdp VALUES(?, ?, ?)', new_mdp)
        connection.commit()
    except Exception as e:
        print(("[ERREUR]", e))
        connection.rollback()
    finally:
        connection.close()


def afficher_tout_mdp():
    try:
        connection = sqlite3.connect("base.db")
        cursor = connection.cursor()
        req = cursor.execute('SELECT * FROM mdp')
        for row in req.fetchall():
            print (f"Le mot de passe pour {row[1]} est {row[2]}")
    except Exception as e:
        print("[ERREUR]", e)
        connection.rollback()
    finally:
        connection.close()


def afficher_un_mdp(nom_site):
    try:
        connection = sqlite3.connect("base.db")
        cursor = connection.cursor()
        my_site = (nom_site,)
        cursor.execute('SELECT * FROM mdp WHERE mdp_site =?', my_site)
        print(f"le mot de passe est {cursor.fetchone()[2]}")

    except Exception as e:
        print("[ERREUR]", e)
    finally:
        connection.close()


choix = input("Que voulez vous faire 1-nouveau mot de passe 2-voir tout les mot de passe 3- voir mot de passe pour un site : ")
if choix == "1":
    site_mdp = input("quelle site le mot de passe : ")
    longueur_mdp = input("De quelle longueur le mot de passe : ")

    mot_de_passe = generation_mdp(int(longueur_mdp))
    ajout_bdd(site_mdp, mot_de_passe)
elif choix == "2":
    afficher_tout_mdp()
elif choix == "3":
    reponse = input("Quelle site voulez vous voir le mot de passe : ")
    afficher_un_mdp(reponse)
else:
    print("[ERREUR]")
