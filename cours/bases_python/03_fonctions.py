# ============================================================
# 03 — Fonctions
# Définition, paramètres, récursivité, décorateurs
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. Définition et appel
# ──────────────────────────────────────────────────────────

def saluer(nom):
    """Retourne une salutation personnalisée."""
    return f"Bonjour, {nom} !"

print(saluer("Enzo"))  # Bonjour, Enzo !

# Valeurs par défaut
def puissance(base, exposant=2):
    return base ** exposant

print(puissance(3))     # 9
print(puissance(3, 3))  # 27

# Arguments nommés (keyword arguments)
def afficher_personne(nom, age, ville="Paris"):
    print(f"{nom}, {age} ans, {ville}")

afficher_personne("Alice", 25)
afficher_personne(age=30, nom="Bob", ville="Lyon")


# ──────────────────────────────────────────────────────────
# 2. *args et **kwargs
# ──────────────────────────────────────────────────────────

# *args — nombre variable d'arguments positionnels
def somme(*nombres):
    return sum(nombres)

print(somme(1, 2, 3))        # 6
print(somme(10, 20, 30, 40)) # 100

# **kwargs — nombre variable d'arguments nommés
def afficher_infos(**infos):
    for cle, valeur in infos.items():
        print(f"  {cle}: {valeur}")

afficher_infos(nom="Enzo", age=21, formation="Licence Info")

# Combinaison
def tout(*args, **kwargs):
    print("args :", args)
    print("kwargs :", kwargs)

tout(1, 2, 3, couleur="rouge", taille="M")


# ──────────────────────────────────────────────────────────
# 3. Valeurs de retour multiples
# ──────────────────────────────────────────────────────────

def divmod_complet(a, b):
    return a // b, a % b  # retourne un tuple

quotient, reste = divmod_complet(17, 5)
print(f"17 ÷ 5 = {quotient} reste {reste}")

def statistiques(liste):
    return min(liste), max(liste), sum(liste) / len(liste)

mini, maxi, moyenne = statistiques([3, 7, 2, 9, 1])
print(f"min={mini}, max={maxi}, moy={moyenne}")


# ──────────────────────────────────────────────────────────
# 4. Portée des variables (scope)
# ──────────────────────────────────────────────────────────

x = 10  # variable globale

def modifier():
    x = 99  # variable locale, ne modifie pas x global
    print("local :", x)

modifier()
print("global :", x)  # 10

def modifier_global():
    global x
    x = 99  # modifie x global (éviter si possible)

# nonlocal — accéder à la variable de la fonction englobante
def externe():
    compteur = 0
    def incrementer():
        nonlocal compteur
        compteur += 1
        return compteur
    return incrementer

inc = externe()
print(inc())  # 1
print(inc())  # 2
print(inc())  # 3


# ──────────────────────────────────────────────────────────
# 5. Fonctions lambda (anonymes)
# ──────────────────────────────────────────────────────────

carre = lambda x: x ** 2
print(carre(5))  # 25

# Utile avec sorted, map, filter
nombres = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(nombres))               # ordre croissant
print(sorted(nombres, reverse=True)) # ordre décroissant

# Trier des tuples par le 2e élément
paires = [(1, 3), (4, 1), (2, 2)]
print(sorted(paires, key=lambda t: t[1]))  # [(4, 1), (2, 2), (1, 3)]

# map — appliquer une fonction à chaque élément
carres = list(map(lambda x: x**2, range(6)))
print(carres)  # [0, 1, 4, 9, 16, 25]

# filter — filtrer selon un critère
pairs = list(filter(lambda x: x % 2 == 0, range(10)))
print(pairs)  # [0, 2, 4, 6, 8]


# ──────────────────────────────────────────────────────────
# 6. Récursivité
# ──────────────────────────────────────────────────────────

# Factorielle
def factorielle(n):
    """n! = n × (n-1) × ... × 1,  0! = 1"""
    if n <= 1:        # cas de base
        return 1
    return n * factorielle(n - 1)  # appel récursif

for i in range(8):
    print(f"{i}! = {factorielle(i)}")

# Fibonacci récursif (naïf — exponentiel)
def fib_naif(n):
    if n <= 1:
        return n
    return fib_naif(n - 1) + fib_naif(n - 2)

# Fibonacci avec mémoïsation
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print([fib(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Somme récursive d'une liste
def somme_rec(liste):
    if not liste:
        return 0
    return liste[0] + somme_rec(liste[1:])

print(somme_rec([1, 2, 3, 4, 5]))  # 15

# Tour de Hanoï
def hanoi(n, source="A", cible="C", auxiliaire="B"):
    if n == 1:
        print(f"Disque 1 : {source} → {cible}")
        return
    hanoi(n - 1, source, auxiliaire, cible)
    print(f"Disque {n} : {source} → {cible}")
    hanoi(n - 1, auxiliaire, cible, source)

hanoi(3)


# ──────────────────────────────────────────────────────────
# 7. Fonctions d'ordre supérieur & fermetures (closures)
# ──────────────────────────────────────────────────────────

def creer_multiplicateur(facteur):
    """Retourne une fonction qui multiplie par facteur."""
    def multiplier(x):
        return x * facteur
    return multiplier

doubler  = creer_multiplicateur(2)
tripler  = creer_multiplicateur(3)
print(doubler(5))  # 10
print(tripler(5))  # 15

# Fonction qui prend une fonction en argument
def appliquer_deux_fois(f, x):
    return f(f(x))

print(appliquer_deux_fois(doubler, 3))  # 12


# ──────────────────────────────────────────────────────────
# 8. Décorateurs
# ──────────────────────────────────────────────────────────

import time

# Décorateur simple : mesure le temps d'exécution
def chrono(fonction):
    def wrapper(*args, **kwargs):
        debut = time.perf_counter()
        resultat = fonction(*args, **kwargs)
        fin = time.perf_counter()
        print(f"{fonction.__name__} : {fin - debut:.6f} s")
        return resultat
    return wrapper

@chrono
def calcul_long():
    return sum(range(10_000_000))

calcul_long()

# Décorateur avec paramètres
def repeter(n):
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                fonction(*args, **kwargs)
        return wrapper
    return decorateur

@repeter(3)
def dire_bonjour():
    print("Bonjour !")

dire_bonjour()  # affiche "Bonjour !" 3 fois

# Décorateur de validation
def valider_positif(fonction):
    def wrapper(n):
        if n < 0:
            raise ValueError(f"Argument négatif : {n}")
        return fonction(n)
    return wrapper

@valider_positif
def racine(n):
    return n ** 0.5

print(racine(16))  # 4.0


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Fonction qui vérifie si un nombre est premier
def est_premier(n):
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True

premiers = [n for n in range(50) if est_premier(n)]
print(premiers)

# Ex 2 : Décorateur qui compte les appels
def compte_appels(fonction):
    def wrapper(*args, **kwargs):
        wrapper.nb_appels += 1
        print(f"Appel #{wrapper.nb_appels} de {fonction.__name__}")
        return fonction(*args, **kwargs)
    wrapper.nb_appels = 0
    return wrapper

@compte_appels
def hello():
    print("Hello!")

hello(); hello(); hello()
print(f"Total : {hello.nb_appels} appels")

# Ex 3 : Récursion — puissance sans **
def puiss(base, exp):
    if exp == 0:
        return 1
    if exp % 2 == 0:
        moitie = puiss(base, exp // 2)
        return moitie * moitie
    return base * puiss(base, exp - 1)

print(puiss(2, 10))  # 1024
