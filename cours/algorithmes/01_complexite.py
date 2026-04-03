# ============================================================
# 01 — Complexité algorithmique
# Notation Big-O, analyse temporelle et spatiale
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. Introduction à la complexité
# ──────────────────────────────────────────────────────────

# La complexité mesure la croissance du temps (ou de l'espace)
# d'un algorithme en fonction de la taille de l'entrée n.
#
# On distingue :
#  - Cas meilleur  (Ω — Omega)
#  - Cas moyen     (Θ — Theta)
#  - Cas pire      (O — Big-O)  ← le plus utilisé
#
# Ordre de croissance (du plus rapide au plus lent) :
#  O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)

import time
import random


# ──────────────────────────────────────────────────────────
# 2. O(1) — Temps constant
# ──────────────────────────────────────────────────────────

def premier_element(liste):
    """Retourne le premier élément — toujours 1 opération."""
    return liste[0]

def est_pair(n):
    """Le modulo est une seule opération."""
    return n % 2 == 0

# Accès à un dictionnaire / set : O(1) amorti
def contient(ensemble, valeur):
    return valeur in ensemble  # hash lookup O(1)


# ──────────────────────────────────────────────────────────
# 3. O(log n) — Logarithmique
# ──────────────────────────────────────────────────────────

def recherche_binaire(lst, cible):
    """Divise l'espace de recherche par 2 à chaque étape."""
    gauche, droite = 0, len(lst) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if lst[milieu] == cible:
            return milieu
        elif lst[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return -1

# log₂(1 000 000) ≈ 20 : seulement ~20 étapes pour 1 million d'éléments !

def puissance_rapide(base, exp):
    """Exponentiation rapide : O(log exp)."""
    if exp == 0:
        return 1
    if exp % 2 == 0:
        moitie = puissance_rapide(base, exp // 2)
        return moitie * moitie
    return base * puissance_rapide(base, exp - 1)


# ──────────────────────────────────────────────────────────
# 4. O(n) — Linéaire
# ──────────────────────────────────────────────────────────

def somme(liste):
    """Parcourir une fois : n opérations."""
    total = 0
    for x in liste:
        total += x
    return total

def trouver_max(liste):
    """Trouver le max sans tri : O(n)."""
    maximum = liste[0]
    for x in liste[1:]:
        if x > maximum:
            maximum = x
    return maximum

def compter_occurrences(liste, valeur):
    return sum(1 for x in liste if x == valeur)


# ──────────────────────────────────────────────────────────
# 5. O(n log n) — Quasi-linéaire
# ──────────────────────────────────────────────────────────

def tri_fusion(lst):
    """Merge sort : O(n log n) garanti."""
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    gauche = tri_fusion(lst[:mid])
    droite = tri_fusion(lst[mid:])
    return fusionner(gauche, droite)

def fusionner(g, d):
    resultat = []
    i = j = 0
    while i < len(g) and j < len(d):
        if g[i] <= d[j]:
            resultat.append(g[i]); i += 1
        else:
            resultat.append(d[j]); j += 1
    resultat.extend(g[i:])
    resultat.extend(d[j:])
    return resultat

# Python utilise Timsort (hybride mergesort+insertion) : O(n log n)


# ──────────────────────────────────────────────────────────
# 6. O(n²) — Quadratique
# ──────────────────────────────────────────────────────────

def tri_bulles(lst):
    """Bubble sort : O(n²) dans le pire cas."""
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def paires_avec_somme(liste, cible):
    """Trouver toutes les paires dont la somme = cible : O(n²) naïf."""
    paires = []
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i] + liste[j] == cible:
                paires.append((liste[i], liste[j]))
    return paires

def paires_avec_somme_rapide(liste, cible):
    """Version O(n) avec ensemble."""
    vus = set()
    paires = []
    for x in liste:
        complement = cible - x
        if complement in vus:
            paires.append((complement, x))
        vus.add(x)
    return paires


# ──────────────────────────────────────────────────────────
# 7. O(2ⁿ) — Exponentiel
# ──────────────────────────────────────────────────────────

def fibonacci_naif(n):
    """Calcul naïf : arbre de récursion → O(2ⁿ) appels."""
    if n <= 1:
        return n
    return fibonacci_naif(n - 1) + fibonacci_naif(n - 2)

def sous_ensembles(lst):
    """Générer tous les sous-ensembles : O(2ⁿ)."""
    if not lst:
        return [[]]
    premier, reste = lst[0], lst[1:]
    sans = sous_ensembles(reste)
    avec = [[premier] + s for s in sans]
    return sans + avec

print(sous_ensembles([1, 2, 3]))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]


# ──────────────────────────────────────────────────────────
# 8. O(n!) — Factoriel
# ──────────────────────────────────────────────────────────

from itertools import permutations

def toutes_permutations(lst):
    """Générer toutes les permutations : O(n!)."""
    return list(permutations(lst))

# 10! = 3 628 800
# 20! = 2 432 902 008 176 640 000 → impossible en pratique


# ──────────────────────────────────────────────────────────
# 9. Complexité spatiale
# ──────────────────────────────────────────────────────────

# O(1) — espace constant
def somme_tableau(lst):
    total = 0  # une seule variable
    for x in lst:
        total += x
    return total

# O(n) — espace linéaire
def doubler(lst):
    return [x * 2 for x in lst]  # nouvelle liste de taille n

# O(log n) — pile d'appels de la récursion binaire
def bs_espace(lst, cible, g=0, d=None):
    if d is None:
        d = len(lst) - 1
    if g > d:
        return -1
    m = (g + d) // 2
    if lst[m] == cible:
        return m
    elif lst[m] < cible:
        return bs_espace(lst, cible, m + 1, d)
    else:
        return bs_espace(lst, cible, g, m - 1)


# ──────────────────────────────────────────────────────────
# 10. Mesurer la complexité empiriquement
# ──────────────────────────────────────────────────────────

def mesurer(algo, *args):
    debut = time.perf_counter()
    resultat = algo(*args)
    fin = time.perf_counter()
    return fin - debut, resultat

# Comparer la recherche linéaire vs binaire
tailles = [1_000, 10_000, 100_000, 1_000_000]

for n in tailles:
    lst = list(range(n))
    cible = n - 1  # pire cas : élément en fin de liste

    t_lineaire, _ = mesurer(lambda l, c: c in l, lst, cible)
    t_binaire,  _ = mesurer(recherche_binaire, lst, cible)

    print(f"n={n:>10}: linéaire={t_lineaire:.4f}s  binaire={t_binaire:.6f}s")


# ──────────────────────────────────────────────────────────
# Tableau récapitulatif
# ──────────────────────────────────────────────────────────

#  n         O(1)   O(log n)  O(n)      O(n log n)  O(n²)        O(2ⁿ)
#  10        1      3         10        33          100          1 024
#  100       1      7         100       664         10 000       1.27e30
#  1 000     1      10        1 000     9 966       1 000 000    —
#  1 000 000 1      20        1 000 000 19 931 568  1e12         —


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Quelle est la complexité de ces fonctions ?

def f1(n):               # O(n)
    for i in range(n):
        print(i)

def f2(n):               # O(n²)
    for i in range(n):
        for j in range(n):
            print(i, j)

def f3(n):               # O(log n)
    while n > 1:
        n //= 2

def f4(lst):             # O(n) — max() parcourt une fois
    return max(lst)

def f5(lst):             # O(n²) — deux boucles imbriquées
    for i in lst:
        for j in lst:
            pass

# Ex 2 : Optimiser — deux sommes
# Naïf O(n²) : trouver deux indices i,j tels que lst[i]+lst[j] = cible
# Optimal O(n) : utiliser un dictionnaire

def deux_sommes_optimal(lst, cible):
    vus = {}
    for i, val in enumerate(lst):
        complement = cible - val
        if complement in vus:
            return (vus[complement], i)
        vus[val] = i
    return None

print(deux_sommes_optimal([2, 7, 11, 15], 9))  # (0, 1)
