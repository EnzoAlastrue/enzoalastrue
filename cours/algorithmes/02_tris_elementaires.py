# ============================================================
# 02 — Tris élémentaires
# Tri à bulles, insertion, sélection — O(n²)
# ============================================================

import time
import random

# ──────────────────────────────────────────────────────────
# Utilitaire : mesurer et afficher
# ──────────────────────────────────────────────────────────

def mesurer_tri(algo, lst):
    copie = lst.copy()
    debut = time.perf_counter()
    tri = algo(copie)
    fin = time.perf_counter()
    assert tri == sorted(lst), "Erreur de tri !"
    return fin - debut

def afficher(lst, label=""):
    print(f"{label}: {lst}")


# ──────────────────────────────────────────────────────────
# 1. Tri à bulles (Bubble Sort) — O(n²)
# ──────────────────────────────────────────────────────────
#
# Principe :
#   Parcourir la liste en comparant des paires adjacentes.
#   Si lst[j] > lst[j+1], les échanger.
#   À chaque passe, le plus grand élément "remonte" à sa place.
#
# Complexité :
#   - Pire cas  : O(n²)  — liste inversée
#   - Meilleur  : O(n)   — liste déjà triée (avec optimisation)
#   - Espace    : O(1)   — en place

def tri_bulles(lst):
    n = len(lst)
    for i in range(n):
        echange = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                echange = True
        if not echange:   # optimisation : déjà trié
            break
    return lst

# Visualisation pas à pas
def tri_bulles_verbose(lst):
    n = len(lst)
    print(f"Départ  : {lst}")
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        print(f"Passe {i+1} : {lst}")
    return lst

exemple = [64, 34, 25, 12, 22, 11, 90]
tri_bulles_verbose(exemple[:])


# ──────────────────────────────────────────────────────────
# 2. Tri par insertion (Insertion Sort) — O(n²)
# ──────────────────────────────────────────────────────────
#
# Principe :
#   Construire la partie triée de gauche à droite.
#   Pour chaque élément, l'insérer à sa bonne position
#   dans la partie déjà triée (comme trier des cartes à jouer).
#
# Complexité :
#   - Pire cas  : O(n²)  — liste inversée
#   - Meilleur  : O(n)   — liste presque triée ← avantage !
#   - Espace    : O(1)   — en place

def tri_insertion(lst):
    for i in range(1, len(lst)):
        cle = lst[i]
        j = i - 1
        # Décaler les éléments plus grands que la clé vers la droite
        while j >= 0 and lst[j] > cle:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = cle
    return lst

# Variante : avec recherche binaire pour trouver la position
import bisect

def tri_insertion_binaire(lst):
    """Insertion binaire : O(n log n) comparaisons, O(n²) déplacements."""
    for i in range(1, len(lst)):
        cle = lst[i]
        pos = bisect.bisect_left(lst, cle, 0, i)
        lst[i:pos:-1] = lst[i-1:pos-1:-1]  # décalage slice
        lst[pos] = cle
    return lst

def tri_insertion_verbose(lst):
    print(f"Départ  : {lst}")
    for i in range(1, len(lst)):
        cle = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > cle:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = cle
        print(f"Étape {i} : {lst}  (inséré {cle})")
    return lst

tri_insertion_verbose([5, 3, 8, 1, 9, 2][:])


# ──────────────────────────────────────────────────────────
# 3. Tri par sélection (Selection Sort) — O(n²)
# ──────────────────────────────────────────────────────────
#
# Principe :
#   Trouver le minimum de la partie non triée,
#   l'échanger avec le premier élément non trié.
#   Répéter jusqu'à la fin.
#
# Complexité :
#   - Tous les cas : O(n²)  — toujours n(n-1)/2 comparaisons
#   - Échanges     : O(n)   — au plus n échanges ← avantage
#   - Espace       : O(1)   — en place

def tri_selection(lst):
    n = len(lst)
    for i in range(n):
        # Trouver l'indice du minimum dans lst[i:]
        idx_min = i
        for j in range(i + 1, n):
            if lst[j] < lst[idx_min]:
                idx_min = j
        # Échanger
        if idx_min != i:
            lst[i], lst[idx_min] = lst[idx_min], lst[i]
    return lst

def tri_selection_verbose(lst):
    n = len(lst)
    print(f"Départ  : {lst}")
    for i in range(n):
        idx_min = i
        for j in range(i + 1, n):
            if lst[j] < lst[idx_min]:
                idx_min = j
        lst[i], lst[idx_min] = lst[idx_min], lst[i]
        print(f"Étape {i+1} : {lst}  (mis {lst[i]} en position {i})")
    return lst

tri_selection_verbose([29, 10, 14, 37, 13][:])


# ──────────────────────────────────────────────────────────
# 4. Tri cocktail (variante de bubble sort) — O(n²)
# ──────────────────────────────────────────────────────────
#
# Bidirectionnel : une passe de gauche à droite, puis de droite à gauche.
# Réduit le problème des "tortues" (petits éléments à droite).

def tri_cocktail(lst):
    n = len(lst)
    gauche, droite = 0, n - 1
    while gauche < droite:
        echange = False
        for i in range(gauche, droite):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                echange = True
        droite -= 1
        for i in range(droite, gauche, -1):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                echange = True
        gauche += 1
        if not echange:
            break
    return lst


# ──────────────────────────────────────────────────────────
# 5. Tri à peigne (Comb Sort) — O(n²) pire, O(n log n) moy.
# ──────────────────────────────────────────────────────────
#
# Amélioration du tri à bulles : compare des éléments distants
# (écart = gap), réduit le gap à chaque passe.

def tri_peigne(lst):
    n = len(lst)
    gap = n
    shrink = 1.3
    trie = False
    while not trie:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            trie = True
        i = 0
        while i + gap < n:
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                trie = False
            i += 1
    return lst


# ──────────────────────────────────────────────────────────
# 6. Comparaison des performances
# ──────────────────────────────────────────────────────────

def comparer_tris(n=2000):
    algos = {
        "Bulles"    : tri_bulles,
        "Insertion" : tri_insertion,
        "Sélection" : tri_selection,
        "Cocktail"  : tri_cocktail,
        "Peigne"    : tri_peigne,
    }

    cas = {
        "Aléatoire"  : random.sample(range(n * 10), n),
        "Presque trié": sorted(random.sample(range(n * 10), n))[:n - 5] + random.sample(range(n * 10), 5),
        "Inversé"    : list(range(n, 0, -1)),
    }

    for nom_cas, lst in cas.items():
        print(f"\n── {nom_cas} (n={n}) ──")
        for nom_algo, algo in algos.items():
            t = mesurer_tri(algo, lst)
            print(f"  {nom_algo:12}: {t:.4f}s")

comparer_tris(1000)


# ──────────────────────────────────────────────────────────
# 7. Récapitulatif
# ──────────────────────────────────────────────────────────

#  Algorithme   | Meilleur | Moyen  | Pire   | Espace | Stable
#  -------------|----------|--------|--------|--------|-------
#  Bulles       | O(n)     | O(n²)  | O(n²)  | O(1)   | Oui
#  Insertion    | O(n)     | O(n²)  | O(n²)  | O(1)   | Oui
#  Sélection    | O(n²)    | O(n²)  | O(n²)  | O(1)   | Non
#  Cocktail     | O(n)     | O(n²)  | O(n²)  | O(1)   | Oui
#  Peigne       | O(n log) | O(n²)  | O(n²)  | O(1)   | Non
#
# Stable = deux éléments égaux gardent leur ordre relatif

# Quand utiliser ces tris ?
# - Insertion : excellent pour les petites listes ou presque triées (< 20 éléments)
# - Sélection : quand les échanges sont coûteux (écriture disque)
# - En pratique : toujours utiliser sorted() ou list.sort() (Timsort)


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Trier par ordre décroissant
def tri_insertion_desc(lst):
    for i in range(1, len(lst)):
        cle = lst[i]
        j = i - 1
        while j >= 0 and lst[j] < cle:  # < au lieu de >
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = cle
    return lst

print(tri_insertion_desc([3, 1, 4, 1, 5, 9, 2, 6]))  # [9, 6, 5, 4, 3, 2, 1, 1]

# Ex 2 : Tri par critère personnalisé
etudiants = [("Alice", 15), ("Bob", 12), ("Claire", 18), ("David", 10)]

# Trier par note (2e élément du tuple) avec insertion
def tri_par_cle(lst, cle):
    for i in range(1, len(lst)):
        actuel = lst[i]
        j = i - 1
        while j >= 0 and cle(lst[j]) > cle(actuel):
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = actuel
    return lst

print(tri_par_cle(etudiants[:], key=lambda e: e[1]))

# Ex 3 : Compter les inversions dans une liste
def compter_inversions(lst):
    """Nombre de paires (i,j) telles que i<j et lst[i]>lst[j]."""
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                count += 1
    return count

print(compter_inversions([2, 4, 1, 3, 5]))  # 3
