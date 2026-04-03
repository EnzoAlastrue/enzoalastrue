# ============================================================
# 01 — Types & Variables
# Fondamentaux Python : types, opérateurs, conversions
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. Types de base
# ──────────────────────────────────────────────────────────

# Entier (int)
age = 21
annee = 2024
negatif = -42

# Flottant (float)
pi = 3.14159
temperature = -7.5
scientifique = 1.5e10  # 15 000 000 000

# Booléen (bool)
est_majeur = True
est_connecte = False

# Chaîne de caractères (str)
prenom = "Enzo"
message = 'Bonjour le monde'
multilignes = """Ceci est
un texte
sur plusieurs lignes."""

# NoneType
valeur_inconnue = None

# Vérification du type
print(type(age))           # <class 'int'>
print(type(pi))            # <class 'float'>
print(type(est_majeur))    # <class 'bool'>
print(type(prenom))        # <class 'str'>
print(type(valeur_inconnue))  # <class 'NoneType'>


# ──────────────────────────────────────────────────────────
# 2. Opérateurs arithmétiques
# ──────────────────────────────────────────────────────────

a, b = 17, 5

print(a + b)   # 22  — addition
print(a - b)   # 12  — soustraction
print(a * b)   # 85  — multiplication
print(a / b)   # 3.4 — division réelle
print(a // b)  # 3   — division entière (floor)
print(a % b)   # 2   — modulo (reste)
print(a ** b)  # 1419857 — puissance

# Priorité : ** > * / // % > + -
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20


# ──────────────────────────────────────────────────────────
# 3. Opérateurs de comparaison
# ──────────────────────────────────────────────────────────

x = 10
print(x == 10)  # True  — égal
print(x != 9)   # True  — différent
print(x > 5)    # True  — supérieur
print(x < 5)    # False — inférieur
print(x >= 10)  # True  — supérieur ou égal
print(x <= 9)   # False — inférieur ou égal


# ──────────────────────────────────────────────────────────
# 4. Opérateurs logiques
# ──────────────────────────────────────────────────────────

p, q = True, False
print(p and q)  # False
print(p or q)   # True
print(not p)    # False

# Court-circuit : Python n'évalue pas la 2e condition si inutile
print(True or (1 / 0))   # True  (pas d'erreur)
print(False and (1 / 0)) # False (pas d'erreur)


# ──────────────────────────────────────────────────────────
# 5. Conversions de types (casting)
# ──────────────────────────────────────────────────────────

# str → int / float
s = "42"
n = int(s)        # 42
f = float(s)      # 42.0

# int / float → str
texte = str(3.14) # "3.14"

# float → int (troncature)
print(int(9.9))   # 9  (pas d'arrondi !)
print(int(-9.9))  # -9

# Fonctions utiles
print(abs(-7))        # 7
print(round(3.14159, 2))  # 3.14
print(min(4, 7, 1))       # 1
print(max(4, 7, 1))       # 7


# ──────────────────────────────────────────────────────────
# 6. Chaînes de caractères — opérations essentielles
# ──────────────────────────────────────────────────────────

nom = "Python"

# Longueur
print(len(nom))          # 6

# Indexation (commence à 0)
print(nom[0])            # P
print(nom[-1])           # n  (dernier)

# Slicing [début:fin:pas]
print(nom[0:3])          # Pyt
print(nom[::2])          # Pto
print(nom[::-1])         # nohtyP  (inversion)

# Méthodes
print(nom.upper())       # PYTHON
print(nom.lower())       # python
print("  bonjour  ".strip())  # "bonjour"
print("a,b,c".split(","))     # ['a', 'b', 'c']
print(",".join(["a","b","c"])) # a,b,c
print(nom.replace("P", "J"))  # Jython
print("on" in nom)       # True

# f-strings (formatage moderne)
age = 21
print(f"J'ai {age} ans")         # J'ai 21 ans
print(f"Pi ≈ {3.14159:.2f}")     # Pi ≈ 3.14
print(f"{1000000:,}")            # 1,000,000


# ──────────────────────────────────────────────────────────
# 7. Variables et affectation
# ──────────────────────────────────────────────────────────

# Affectation multiple
x = y = z = 0

# Déballage (unpacking)
a, b, c = 1, 2, 3
premier, *reste = [10, 20, 30, 40]
print(premier)  # 10
print(reste)    # [20, 30, 40]

# Échange sans variable temporaire
a, b = b, a

# Opérateurs d'affectation augmentée
n = 10
n += 5   # n = 15
n -= 3   # n = 12
n *= 2   # n = 24
n //= 4  # n = 6
print(n) # 6


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Demander le rayon d'un cercle et afficher son aire et périmètre
import math

rayon = float(input("Rayon du cercle : "))
aire = math.pi * rayon ** 2
perimetre = 2 * math.pi * rayon
print(f"Aire : {aire:.4f}")
print(f"Périmètre : {perimetre:.4f}")

# Ex 2 : Convertir des degrés Celsius en Fahrenheit
celsius = float(input("Température en °C : "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C = {fahrenheit:.1f}°F")

# Ex 3 : Palindrome
mot = input("Entrez un mot : ").lower().strip()
if mot == mot[::-1]:
    print(f"'{mot}' est un palindrome.")
else:
    print(f"'{mot}' n'est pas un palindrome.")
