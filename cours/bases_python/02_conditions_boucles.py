# ============================================================
# 02 — Conditions & Boucles
# if/elif/else, for, while, compréhensions de liste
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. Conditions if / elif / else
# ──────────────────────────────────────────────────────────

note = 14

if note >= 16:
    mention = "Très bien"
elif note >= 14:
    mention = "Bien"
elif note >= 12:
    mention = "Assez bien"
elif note >= 10:
    mention = "Passable"
else:
    mention = "Insuffisant"

print(f"Note : {note}/20 → {mention}")

# Expression ternaire (opérateur conditionnel)
age = 20
statut = "majeur" if age >= 18 else "mineur"
print(statut)  # majeur

# Conditions composées
x = 15
if 10 <= x <= 20:  # équivalent à x >= 10 and x <= 20
    print(f"{x} est entre 10 et 20")

# Vérifier si une valeur est dans une liste
couleurs = ["rouge", "vert", "bleu"]
if "vert" in couleurs:
    print("Vert est disponible")

# Valeurs "falsy" en Python
# False, None, 0, 0.0, "", [], {}, ()
liste_vide = []
if not liste_vide:
    print("La liste est vide")


# ──────────────────────────────────────────────────────────
# 2. Boucle for
# ──────────────────────────────────────────────────────────

# Parcourir une liste
fruits = ["pomme", "banane", "cerise"]
for fruit in fruits:
    print(fruit)

# range(debut, fin, pas)  — fin exclue
for i in range(5):          # 0 1 2 3 4
    print(i, end=" ")
print()

for i in range(2, 10, 2):  # 2 4 6 8
    print(i, end=" ")
print()

for i in range(5, 0, -1):  # 5 4 3 2 1
    print(i, end=" ")
print()

# enumerate — indice + valeur
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# zip — itérer sur plusieurs listes en parallèle
noms   = ["Alice", "Bob", "Charlie"]
scores = [90, 75, 88]
for nom, score in zip(noms, scores):
    print(f"{nom} : {score}")

# Parcourir un dictionnaire
personne = {"nom": "Enzo", "age": 21, "ville": "Paris"}
for cle, valeur in personne.items():
    print(f"{cle} = {valeur}")


# ──────────────────────────────────────────────────────────
# 3. Boucle while
# ──────────────────────────────────────────────────────────

# Compter jusqu'à 5
compteur = 0
while compteur < 5:
    print(compteur, end=" ")
    compteur += 1
print()

# Boucle infinie avec break
import random
secret = random.randint(1, 10)
while True:
    essai = int(input("Devinez le nombre (1-10) : "))
    if essai == secret:
        print("Bravo !")
        break
    elif essai < secret:
        print("Trop petit.")
    else:
        print("Trop grand.")

# do-while simulé en Python
while True:
    reponse = input("Entrez 'oui' pour continuer : ")
    if reponse.lower() == "oui":
        break


# ──────────────────────────────────────────────────────────
# 4. Instructions de contrôle de boucle
# ──────────────────────────────────────────────────────────

# break — quitter la boucle immédiatement
for n in range(10):
    if n == 5:
        break
    print(n, end=" ")  # 0 1 2 3 4
print()

# continue — passer à l'itération suivante
for n in range(10):
    if n % 2 == 0:
        continue
    print(n, end=" ")  # 1 3 5 7 9
print()

# else sur une boucle (exécuté si pas de break)
for n in range(2, 10):
    for diviseur in range(2, n):
        if n % diviseur == 0:
            break
    else:
        print(f"{n} est premier")


# ──────────────────────────────────────────────────────────
# 5. Compréhensions de liste
# ──────────────────────────────────────────────────────────

# Syntaxe : [expression for element in iterable if condition]

# Carrés des nombres de 0 à 9
carres = [x**2 for x in range(10)]
print(carres)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Filtrer les pairs
pairs = [x for x in range(20) if x % 2 == 0]
print(pairs)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Transformer une liste de chaînes
mots = ["bonjour", "monde", "python"]
majuscules = [mot.upper() for mot in mots]
print(majuscules)  # ['BONJOUR', 'MONDE', 'PYTHON']

# Compréhension imbriquée (matrice 3×3)
matrice = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrice)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Aplatir une liste de listes
liste_2d = [[1, 2], [3, 4], [5, 6]]
plat = [x for sous_liste in liste_2d for x in sous_liste]
print(plat)  # [1, 2, 3, 4, 5, 6]

# Compréhensions de dictionnaire et d'ensemble
carre_dict = {x: x**2 for x in range(6)}
print(carre_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

carre_set = {x**2 for x in range(-3, 4)}
print(carre_set)   # {0, 1, 4, 9}


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Table de multiplication
n = int(input("Table de multiplication de : "))
for i in range(1, 11):
    print(f"{n} × {i:2} = {n * i:3}")

# Ex 2 : FizzBuzz classique
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Ex 3 : Suite de Fibonacci jusqu'à N
n = int(input("Fibonacci jusqu'à : "))
a, b = 0, 1
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print()

# Ex 4 : Nombres premiers jusqu'à 50
premiers = [n for n in range(2, 51)
            if all(n % d != 0 for d in range(2, int(n**0.5) + 1))]
print(premiers)
