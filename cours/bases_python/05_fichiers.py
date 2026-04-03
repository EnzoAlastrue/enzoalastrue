# ============================================================
# 05 — Fichiers
# Lecture/écriture, JSON, CSV
# ============================================================

import os
import json
import csv
from pathlib import Path

# ──────────────────────────────────────────────────────────
# 1. Ouvrir et lire un fichier texte
# ──────────────────────────────────────────────────────────

# Modes d'ouverture
# 'r'  — lecture (défaut)
# 'w'  — écriture (écrase le fichier)
# 'a'  — ajout (append)
# 'x'  — création (erreur si existe)
# 'rb' — lecture binaire
# 'wb' — écriture binaire

# Toujours utiliser 'with' pour fermer automatiquement le fichier
with open("exemple.txt", "w", encoding="utf-8") as f:
    f.write("Première ligne\n")
    f.write("Deuxième ligne\n")
    f.writelines(["Troisième\n", "Quatrième\n"])

# Lire tout le contenu
with open("exemple.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
print(contenu)

# Lire ligne par ligne (efficace en mémoire)
with open("exemple.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.rstrip())  # rstrip() supprime \n

# Lire toutes les lignes dans une liste
with open("exemple.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()      # liste avec \n
    # ou
with open("exemple.txt", "r", encoding="utf-8") as f:
    lignes = f.read().splitlines()  # liste sans \n

# Lire une seule ligne
with open("exemple.txt", "r", encoding="utf-8") as f:
    premiere = f.readline()

# Position dans le fichier
with open("exemple.txt", "r", encoding="utf-8") as f:
    print(f.tell())      # 0 (début)
    f.read(5)
    print(f.tell())      # 5
    f.seek(0)            # retour au début


# ──────────────────────────────────────────────────────────
# 2. Écrire dans un fichier
# ──────────────────────────────────────────────────────────

# Écriture simple
with open("sortie.txt", "w", encoding="utf-8") as f:
    for i in range(5):
        f.write(f"Ligne {i + 1}\n")

# Ajout à la fin
with open("sortie.txt", "a", encoding="utf-8") as f:
    f.write("Ligne ajoutée\n")

# print vers un fichier
with open("log.txt", "w", encoding="utf-8") as f:
    print("Message de log", file=f)
    print("Deuxième message", file=f)


# ──────────────────────────────────────────────────────────
# 3. Manipulation avec pathlib (recommandé)
# ──────────────────────────────────────────────────────────

# pathlib.Path est l'API moderne et portable
chemin = Path("exemple.txt")

# Vérifications
print(chemin.exists())      # True
print(chemin.is_file())     # True
print(chemin.is_dir())      # False

# Lire/écrire directement
texte = chemin.read_text(encoding="utf-8")
chemin.write_text("Nouveau contenu\n", encoding="utf-8")

# Informations sur le chemin
p = Path("/home/user/cours/fichier.py")
print(p.name)       # fichier.py
print(p.stem)       # fichier
print(p.suffix)     # .py
print(p.parent)     # /home/user/cours
print(p.parts)      # ('/', 'home', 'user', 'cours', 'fichier.py')

# Construire des chemins (portable Windows/Linux)
dossier = Path("cours") / "python" / "notes.txt"

# Lister les fichiers
dossier = Path(".")
for f in dossier.iterdir():
    print(f)

for py_file in dossier.glob("*.py"):
    print(py_file)

for py_file in dossier.rglob("*.py"):  # récursif
    print(py_file)

# Créer des dossiers
Path("mon_dossier/sous_dossier").mkdir(parents=True, exist_ok=True)


# ──────────────────────────────────────────────────────────
# 4. JSON
# ──────────────────────────────────────────────────────────

# json.dumps — objet Python → chaîne JSON
donnees = {
    "nom": "Enzo",
    "age": 21,
    "langages": ["Python", "Java"],
    "actif": True,
    "score": 15.5
}

json_str = json.dumps(donnees, indent=4, ensure_ascii=False)
print(json_str)

# json.loads — chaîne JSON → objet Python
recharge = json.loads(json_str)
print(recharge["nom"])  # Enzo

# json.dump — écrire dans un fichier
with open("donnees.json", "w", encoding="utf-8") as f:
    json.dump(donnees, f, indent=4, ensure_ascii=False)

# json.load — lire depuis un fichier
with open("donnees.json", "r", encoding="utf-8") as f:
    lu = json.load(f)
print(lu)

# Types Python ↔ JSON
# dict      ↔ object  {}
# list/tuple ↔ array  []
# str       ↔ string  ""
# int/float ↔ number
# True/False ↔ true/false
# None      ↔ null

# Sérialiser des objets personnalisés
import datetime

def serialiser(obj):
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    raise TypeError(f"Non sérialisable : {type(obj)}")

data = {"date": datetime.date.today(), "valeur": 42}
print(json.dumps(data, default=serialiser))


# ──────────────────────────────────────────────────────────
# 5. CSV
# ──────────────────────────────────────────────────────────

# Écrire un CSV
etudiants = [
    ["Nom",   "Note", "Mention"],
    ["Alice",  18,    "Très bien"],
    ["Bob",    12,    "Passable"],
    ["Claire", 15,    "Bien"],
]

with open("etudiants.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerows(etudiants)

# Lire un CSV
with open("etudiants.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    for ligne in reader:
        print(ligne)

# DictReader / DictWriter — plus pratique
with open("etudiants.csv", "w", newline="", encoding="utf-8") as f:
    champs = ["Nom", "Note", "Mention"]
    writer = csv.DictWriter(f, fieldnames=champs, delimiter=";")
    writer.writeheader()
    writer.writerows([
        {"Nom": "Alice",  "Note": 18, "Mention": "Très bien"},
        {"Nom": "Bob",    "Note": 12, "Mention": "Passable"},
    ])

with open("etudiants.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter=";")
    for etudiant in reader:
        print(f"{etudiant['Nom']} : {etudiant['Note']}/20")


# ──────────────────────────────────────────────────────────
# 6. Gestion des erreurs liées aux fichiers
# ──────────────────────────────────────────────────────────

def lire_fichier_safe(chemin):
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Fichier introuvable : {chemin}")
        return None
    except PermissionError:
        print(f"Permission refusée : {chemin}")
        return None
    except UnicodeDecodeError:
        print(f"Erreur d'encodage : {chemin}")
        return None

# Nettoyage des fichiers temporaires
import os
for f in ["exemple.txt", "sortie.txt", "log.txt", "donnees.json", "etudiants.csv"]:
    if os.path.exists(f):
        os.remove(f)


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Compter les mots dans un fichier
def compter_mots(chemin):
    try:
        texte = Path(chemin).read_text(encoding="utf-8")
        return len(texte.split())
    except FileNotFoundError:
        return 0

# Ex 2 : Fusionner deux fichiers JSON
def fusionner_json(fichier1, fichier2, sortie):
    with open(fichier1) as f1, open(fichier2) as f2:
        d1 = json.load(f1)
        d2 = json.load(f2)
    fusion = {**d1, **d2}
    with open(sortie, "w", encoding="utf-8") as f:
        json.dump(fusion, f, indent=4)

# Ex 3 : Calculer la moyenne des notes depuis un CSV
def moyenne_notes(chemin_csv):
    notes = []
    with open(chemin_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for ligne in reader:
            try:
                notes.append(float(ligne["Note"]))
            except (ValueError, KeyError):
                pass
    return sum(notes) / len(notes) if notes else 0
