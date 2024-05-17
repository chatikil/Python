import os
import random

dossier = r""  # <-- Chemin du dossier
fichiers = os.listdir(dossier)  # Liste des fichiers dans le dossier

if fichiers:
    fichier_aleatoire = random.choice(fichiers)  # Choix aléatoire d'un fichier
    chemin_complet = os.path.join(dossier, fichier_aleatoire)  # Chemin complet du fichier
    os.startfile(chemin_complet)  # Ouvrir le fichier avec le programme par défaut
else:
    print("Le dossier est vide.")
