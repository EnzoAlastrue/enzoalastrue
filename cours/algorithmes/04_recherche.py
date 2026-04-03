# ============================================================
# 04 — Recherche
# Linéaire, binaire, QuickSelect, interpolation
# ============================================================

import random
import time
import bisect

# ──────────────────────────────────────────────────────────
# 1. Recherche linéaire — O(n)
# ──────────────────────────────────────────────────────────

def recherche_lineaire(lst, cible):
    """Parcourir chaque élément jusqu'à trouver la cible."""
    for i, val in enumerate(lst):
        if val == cible:
            return i
    return -1

def recherche_lineaire_toutes(lst, cible):
    """Retourner tous les indices où cible apparaît."""
    return [i for i, val in enumerate(lst) if val == cible]

def recherche_min_max(lst):
    """Trouver min et max en une seule passe — O(n)."""
    if not lst:
        return None, None
    minimum = maximum = lst[0]
    for val in lst[1:]:
        if val < minimum:
            minimum = val
        elif val > maximum:
            maximum = val
    return minimum, maximum

# Test
lst = [64, 25, 12, 22, 11, 90, 34, 12, 22]
print(recherche_lineaire(lst, 22))       # 3
print(recherche_lineaire_toutes(lst, 22)) # [3, 8]
print(recherche_min_max(lst))            # (11, 90)


# ──────────────────────────────────────────────────────────
# 2. Recherche binaire — O(log n)
# ──────────────────────────────────────────────────────────
# Prérequis : liste triée

def recherche_binaire_iterative(lst, cible):
    """Version itérative — O(log n), O(1) espace."""
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

def recherche_binaire_recursive(lst, cible, gauche=0, droite=None):
    """Version récursive — O(log n), O(log n) espace (pile)."""
    if droite is None:
        droite = len(lst) - 1
    if gauche > droite:
        return -1
    milieu = (gauche + droite) // 2
    if lst[milieu] == cible:
        return milieu
    elif lst[milieu] < cible:
        return recherche_binaire_recursive(lst, cible, milieu + 1, droite)
    else:
        return recherche_binaire_recursive(lst, cible, gauche, milieu - 1)

# Avec le module bisect (intégré, très rapide)
def recherche_bisect(lst, cible):
    """Utilise bisect pour une recherche binaire optimisée."""
    idx = bisect.bisect_left(lst, cible)
    if idx < len(lst) and lst[idx] == cible:
        return idx
    return -1

# Variantes utiles de la recherche binaire :

def premier_indice(lst, cible):
    """Première occurrence de cible dans une liste triée."""
    gauche, droite = 0, len(lst) - 1
    resultat = -1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if lst[milieu] == cible:
            resultat = milieu
            droite = milieu - 1  # continuer à gauche
        elif lst[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return resultat

def dernier_indice(lst, cible):
    """Dernière occurrence de cible dans une liste triée."""
    gauche, droite = 0, len(lst) - 1
    resultat = -1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if lst[milieu] == cible:
            resultat = milieu
            gauche = milieu + 1  # continuer à droite
        elif lst[milieu] < cible:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return resultat

def compter_occurrences(lst_triee, cible):
    """Compter les occurrences en O(log n)."""
    debut = bisect.bisect_left(lst_triee, cible)
    fin   = bisect.bisect_right(lst_triee, cible)
    return fin - debut

def plus_proche(lst_triee, cible):
    """Trouver l'élément le plus proche de cible."""
    idx = bisect.bisect_left(lst_triee, cible)
    candidats = []
    if idx < len(lst_triee):
        candidats.append(lst_triee[idx])
    if idx > 0:
        candidats.append(lst_triee[idx - 1])
    return min(candidats, key=lambda x: abs(x - cible))

# Tests
lst_triee = [1, 2, 2, 2, 3, 4, 5, 5, 6]
print(premier_indice(lst_triee, 2))      # 1
print(dernier_indice(lst_triee, 2))      # 3
print(compter_occurrences(lst_triee, 2)) # 3
print(plus_proche(lst_triee, 4))         # 4


# ──────────────────────────────────────────────────────────
# 3. Recherche par interpolation — O(log log n) moyen
# ──────────────────────────────────────────────────────────
# Comme la recherche binaire, mais estime la position du pivot
# en supposant une distribution uniforme.
# Très efficace sur des données uniformément distribuées.

def recherche_interpolation(lst, cible):
    """Efficace si les données sont uniformément distribuées."""
    gauche, droite = 0, len(lst) - 1
    while (gauche <= droite and
           lst[gauche] <= cible <= lst[droite]):
        if lst[droite] == lst[gauche]:
            if lst[gauche] == cible:
                return gauche
            break
        # Estimation de la position par interpolation linéaire
        pos = gauche + int(
            (cible - lst[gauche]) * (droite - gauche)
            / (lst[droite] - lst[gauche])
        )
        if lst[pos] == cible:
            return pos
        elif lst[pos] < cible:
            gauche = pos + 1
        else:
            droite = pos - 1
    return -1

lst_uniform = sorted(random.sample(range(0, 100000), 1000))
print(recherche_interpolation(lst_uniform, lst_uniform[500]))  # 500


# ──────────────────────────────────────────────────────────
# 4. Recherche exponentielle — O(log n)
# ──────────────────────────────────────────────────────────
# Utile quand la liste est de taille inconnue ou très grande.
# Trouve d'abord le domaine, puis fait une recherche binaire.

def recherche_exponentielle(lst, cible):
    if lst[0] == cible:
        return 0
    n = len(lst)
    i = 1
    while i < n and lst[i] <= cible:
        i *= 2
    gauche = i // 2
    droite = min(i, n - 1)
    return recherche_binaire_iterative(lst[gauche:droite + 1], cible)


# ──────────────────────────────────────────────────────────
# 5. QuickSelect — O(n) moyen
# ──────────────────────────────────────────────────────────
# Trouver le k-ième plus petit élément SANS trier entièrement.

def quickselect(lst, k):
    """
    Retourne le k-ième plus petit élément (0-indexé).
    O(n) en moyenne, O(n²) pire cas.
    """
    if len(lst) == 1:
        return lst[0]
    pivot = random.choice(lst)
    gauche  = [x for x in lst if x <  pivot]
    milieu  = [x for x in lst if x == pivot]
    droite  = [x for x in lst if x >  pivot]

    if k < len(gauche):
        return quickselect(gauche, k)
    elif k < len(gauche) + len(milieu):
        return pivot
    else:
        return quickselect(droite, k - len(gauche) - len(milieu))

# Médiane en O(n) moyen
def mediane(lst):
    n = len(lst)
    if n % 2 == 1:
        return quickselect(lst, n // 2)
    else:
        return (quickselect(lst, n // 2 - 1) + quickselect(lst, n // 2)) / 2

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(f"Médiane : {mediane(lst)}")         # 4
print(f"3e plus petit : {quickselect(lst, 2)}")  # 2

# Vérification
lst_tri = sorted(lst)
print(f"Vérifié : {lst_tri[2]}")           # 2


# ──────────────────────────────────────────────────────────
# 6. Recherche dans une matrice triée — O(n + m)
# ──────────────────────────────────────────────────────────
# Matrice où chaque ligne et colonne est triée.
# Algorithme de l'escalier : partir du coin haut-droit.

def chercher_matrice(matrice, cible):
    if not matrice:
        return -1, -1
    lignes, cols = len(matrice), len(matrice[0])
    ligne, col = 0, cols - 1
    while ligne < lignes and col >= 0:
        if matrice[ligne][col] == cible:
            return ligne, col
        elif matrice[ligne][col] < cible:
            ligne += 1
        else:
            col -= 1
    return -1, -1

matrice = [
    [ 1,  4,  7, 11],
    [ 2,  5,  8, 12],
    [ 3,  6,  9, 16],
    [10, 13, 14, 17],
]
print(chercher_matrice(matrice, 9))   # (2, 2)
print(chercher_matrice(matrice, 100)) # (-1, -1)


# ──────────────────────────────────────────────────────────
# 7. Comparaison des performances
# ──────────────────────────────────────────────────────────

n = 1_000_000
lst_tri = list(range(n))
cible = n - 1  # pire cas pour la recherche linéaire

def chrono(algo, *args):
    debut = time.perf_counter()
    res = algo(*args)
    fin = time.perf_counter()
    return fin - debut, res

for nom, algo, args in [
    ("Linéaire",      recherche_lineaire,         (lst_tri, cible)),
    ("Binaire iter.", recherche_binaire_iterative, (lst_tri, cible)),
    ("Binaire recur.",recherche_binaire_recursive, (lst_tri, cible)),
    ("bisect",        recherche_bisect,            (lst_tri, cible)),
    ("Interpolation", recherche_interpolation,     (lst_tri, cible)),
]:
    t, r = chrono(algo, *args)
    print(f"{nom:20}: indice={r}, temps={t:.6f}s")


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Recherche dans une liste circulaire triée
def chercher_circulaire(lst, cible):
    """Liste triée mais pivotée (ex: [4,5,6,7,0,1,2])."""
    gauche, droite = 0, len(lst) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if lst[milieu] == cible:
            return milieu
        # Moitié gauche triée ?
        if lst[gauche] <= lst[milieu]:
            if lst[gauche] <= cible < lst[milieu]:
                droite = milieu - 1
            else:
                gauche = milieu + 1
        else:  # Moitié droite triée
            if lst[milieu] < cible <= lst[droite]:
                gauche = milieu + 1
            else:
                droite = milieu - 1
    return -1

print(chercher_circulaire([4,5,6,7,0,1,2], 0))  # 4
print(chercher_circulaire([4,5,6,7,0,1,2], 3))  # -1

# Ex 2 : Trouver la borne inférieure d'insertion (position d'insertion)
def position_insertion(lst_triee, valeur):
    """Trouver l'indice où insérer valeur pour garder l'ordre."""
    return bisect.bisect_left(lst_triee, valeur)

lst = [1, 3, 5, 7, 9]
print(position_insertion(lst, 4))  # 2 (entre 3 et 5)
print(position_insertion(lst, 0))  # 0 (avant tout)
print(position_insertion(lst, 9))  # 4 (à la place du 9)

# Ex 3 : Compter les paires avec une somme donnée — O(n log n)
def paires_somme(lst, cible):
    """O(n log n) avec tri + deux pointeurs."""
    lst_triee = sorted(lst)
    gauche, droite = 0, len(lst_triee) - 1
    paires = []
    while gauche < droite:
        s = lst_triee[gauche] + lst_triee[droite]
        if s == cible:
            paires.append((lst_triee[gauche], lst_triee[droite]))
            gauche += 1; droite -= 1
        elif s < cible:
            gauche += 1
        else:
            droite -= 1
    return paires

print(paires_somme([1, 2, 3, 4, 5, 6, 7], 8))  # [(1,7),(2,6),(3,5)]
