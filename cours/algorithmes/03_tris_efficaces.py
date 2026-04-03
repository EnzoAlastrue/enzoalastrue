# ============================================================
# 03 — Tris efficaces
# Tri fusion (Merge Sort) et Tri rapide (Quick Sort) — O(n log n)
# ============================================================

import random
import time

# ──────────────────────────────────────────────────────────
# 1. Tri fusion (Merge Sort) — O(n log n) garanti
# ──────────────────────────────────────────────────────────
#
# Paradigme : Diviser pour régner
#   1. Diviser la liste en deux moitiés
#   2. Trier récursivement chaque moitié
#   3. Fusionner les deux moitiés triées
#
# Complexité :
#   - Tous cas : O(n log n)  ← garantie forte
#   - Espace   : O(n)        ← mémoire supplémentaire pour la fusion
#   - Stable   : Oui

def fusionner(gauche, droite):
    """Fusionner deux listes triées en une seule liste triée."""
    resultat = []
    i = j = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])
    return resultat

def tri_fusion(lst):
    """Tri fusion récursif."""
    if len(lst) <= 1:
        return lst
    milieu = len(lst) // 2
    gauche = tri_fusion(lst[:milieu])
    droite = tri_fusion(lst[milieu:])
    return fusionner(gauche, droite)

# Version en place (évite les allocations)
def _fusionner_en_place(lst, debut, milieu, fin):
    gauche = lst[debut:milieu + 1]
    droite = lst[milieu + 1:fin + 1]
    i = j = 0
    k = debut
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            lst[k] = gauche[i]; i += 1
        else:
            lst[k] = droite[j]; j += 1
        k += 1
    while i < len(gauche):
        lst[k] = gauche[i]; i += 1; k += 1
    while j < len(droite):
        lst[k] = droite[j]; j += 1; k += 1

def tri_fusion_en_place(lst, debut=0, fin=None):
    if fin is None:
        fin = len(lst) - 1
    if debut < fin:
        milieu = (debut + fin) // 2
        tri_fusion_en_place(lst, debut, milieu)
        tri_fusion_en_place(lst, milieu + 1, fin)
        _fusionner_en_place(lst, debut, milieu, fin)
    return lst

# Visualisation
def tri_fusion_verbose(lst, profondeur=0):
    indent = "  " * profondeur
    print(f"{indent}tri_fusion({lst})")
    if len(lst) <= 1:
        print(f"{indent}→ {lst}")
        return lst
    milieu = len(lst) // 2
    gauche = tri_fusion_verbose(lst[:milieu], profondeur + 1)
    droite = tri_fusion_verbose(lst[milieu:], profondeur + 1)
    resultat = fusionner(gauche, droite)
    print(f"{indent}fusionner({gauche}, {droite}) → {resultat}")
    return resultat

tri_fusion_verbose([5, 3, 8, 1, 9, 2])


# ──────────────────────────────────────────────────────────
# 2. Tri rapide (Quick Sort) — O(n log n) moyen
# ──────────────────────────────────────────────────────────
#
# Paradigme : Diviser pour régner
#   1. Choisir un pivot
#   2. Partitionner : éléments < pivot à gauche, > pivot à droite
#   3. Trier récursivement les deux parties
#
# Complexité :
#   - Moyen    : O(n log n)
#   - Pire cas : O(n²)  — pivot toujours le plus petit/grand
#   - Espace   : O(log n) pile, O(1) en place
#   - Stable   : Non

def tri_rapide(lst):
    """Version simple (crée de nouvelles listes)."""
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    gauche  = [x for x in lst if x <  pivot]
    milieu  = [x for x in lst if x == pivot]
    droite  = [x for x in lst if x >  pivot]
    return tri_rapide(gauche) + milieu + tri_rapide(droite)

# Version en place — Partition de Lomuto
def partition_lomuto(lst, bas, haut):
    """Le pivot est le dernier élément."""
    pivot = lst[haut]
    i = bas - 1
    for j in range(bas, haut):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[haut] = lst[haut], lst[i + 1]
    return i + 1

def _tri_rapide_lomuto(lst, bas, haut):
    if bas < haut:
        pi = partition_lomuto(lst, bas, haut)
        _tri_rapide_lomuto(lst, bas, pi - 1)
        _tri_rapide_lomuto(lst, pi + 1, haut)

def tri_rapide_lomuto(lst):
    _tri_rapide_lomuto(lst, 0, len(lst) - 1)
    return lst

# Version en place — Partition de Hoare (plus efficace)
def partition_hoare(lst, bas, haut):
    """Le pivot est le premier élément."""
    pivot = lst[bas]
    i, j = bas - 1, haut + 1
    while True:
        i += 1
        while lst[i] < pivot:
            i += 1
        j -= 1
        while lst[j] > pivot:
            j -= 1
        if i >= j:
            return j
        lst[i], lst[j] = lst[j], lst[i]

def _tri_rapide_hoare(lst, bas, haut):
    if bas < haut:
        pi = partition_hoare(lst, bas, haut)
        _tri_rapide_hoare(lst, bas, pi)
        _tri_rapide_hoare(lst, pi + 1, haut)

def tri_rapide_hoare(lst):
    _tri_rapide_hoare(lst, 0, len(lst) - 1)
    return lst

# Quicksort avec pivot médian de 3 (réduit le risque O(n²))
def mediane_de_trois(lst, bas, haut):
    milieu = (bas + haut) // 2
    triplet = [(lst[bas], bas), (lst[milieu], milieu), (lst[haut], haut)]
    triplet.sort()
    # Placer le médian en haut
    _, idx_med = triplet[1]
    lst[idx_med], lst[haut] = lst[haut], lst[idx_med]

def _tri_rapide_med3(lst, bas, haut):
    if haut - bas < 10:   # utiliser insertion pour les petites listes
        for i in range(bas + 1, haut + 1):
            cle = lst[i]
            j = i - 1
            while j >= bas and lst[j] > cle:
                lst[j + 1] = lst[j]; j -= 1
            lst[j + 1] = cle
        return
    mediane_de_trois(lst, bas, haut)
    pi = partition_lomuto(lst, bas, haut)
    _tri_rapide_med3(lst, bas, pi - 1)
    _tri_rapide_med3(lst, pi + 1, haut)

def tri_rapide_med3(lst):
    _tri_rapide_med3(lst, 0, len(lst) - 1)
    return lst


# ──────────────────────────────────────────────────────────
# 3. Timsort — l'algorithme de Python (hybride)
# ──────────────────────────────────────────────────────────
#
# Python utilise Timsort dans sorted() et list.sort()
# - Détecte les "runs" (séquences déjà triées)
# - Utilise l'insertion sort pour les petits runs (< 64)
# - Fusionne les runs avec une variante de merge sort
# - Complexité : O(n log n) pire cas, O(n) si déjà trié
# - Stable : Oui

# Toujours préférer sorted() ou list.sort() en pratique !
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print(sorted(lst))          # nouvelle liste
lst.sort()                  # en place
print(lst)

# Trier des objets complexes
etudiants = [
    {"nom": "Alice", "note": 15},
    {"nom": "Bob",   "note": 12},
    {"nom": "Claire","note": 18},
]
etudiants.sort(key=lambda e: e["note"], reverse=True)
print(etudiants)

# Tri stable : l'ordre relatif des éléments égaux est préservé
from operator import attrgetter, itemgetter
etudiants.sort(key=itemgetter("nom"))  # puis par nom
etudiants.sort(key=itemgetter("note")) # d'abord par note (stable)


# ──────────────────────────────────────────────────────────
# 4. Comparaison des performances
# ──────────────────────────────────────────────────────────

def mesurer(algo, lst):
    copie = lst.copy()
    debut = time.perf_counter()
    resultat = algo(copie)
    fin = time.perf_counter()
    return fin - debut

tailles = [1_000, 5_000, 10_000]
for n in tailles:
    lst_alea = random.sample(range(n * 10), n)
    print(f"\n── n = {n} ──")
    for nom, algo in [
        ("Fusion", tri_fusion),
        ("Rapide (simple)", tri_rapide),
        ("Rapide (Lomuto)", tri_rapide_lomuto),
        ("Rapide (Hoare)", tri_rapide_hoare),
        ("Python sorted", sorted),
    ]:
        t = mesurer(algo, lst_alea)
        print(f"  {nom:20}: {t:.4f}s")


# ──────────────────────────────────────────────────────────
# 5. Récapitulatif
# ──────────────────────────────────────────────────────────

#  Algorithme  | Meilleur  | Moyen     | Pire      | Espace    | Stable
#  ------------|-----------|-----------|-----------|-----------|-------
#  Merge Sort  | O(n log n)| O(n log n)| O(n log n)| O(n)      | Oui
#  Quick Sort  | O(n log n)| O(n log n)| O(n²)     | O(log n)  | Non
#  Timsort     | O(n)      | O(n log n)| O(n log n)| O(n)      | Oui


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Compter les inversions avec le tri fusion
def compter_inversions(lst):
    """Compter le nombre d'inversions en O(n log n)."""
    if len(lst) <= 1:
        return lst, 0
    milieu = len(lst) // 2
    gauche, inv_g = compter_inversions(lst[:milieu])
    droite, inv_d = compter_inversions(lst[milieu:])
    fusionne = []
    inversions = inv_g + inv_d
    i = j = 0
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            fusionne.append(gauche[i]); i += 1
        else:
            fusionne.append(droite[j]); j += 1
            inversions += len(gauche) - i
    fusionne.extend(gauche[i:])
    fusionne.extend(droite[j:])
    return fusionne, inversions

_, inv = compter_inversions([2, 4, 1, 3, 5])
print(f"Inversions : {inv}")  # 3

# Ex 2 : k-ième plus petit élément (QuickSelect) — O(n) moyen
def quickselect(lst, k):
    """Trouver le k-ième plus petit élément en O(n) moyen."""
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

lst = [3, 1, 4, 1, 5, 9, 2, 6]
print(quickselect(lst, 0))  # 1  (le plus petit)
print(quickselect(lst, 4))  # 4  (le 5e plus petit)

# Ex 3 : Tri externe (simulation) — trier un très grand fichier
# Principe : diviser en chunks qui tiennent en mémoire, trier chaque chunk,
# puis fusionner avec un heap (heapq.merge)
import heapq

def tri_externe(data, chunk_size=3):
    """Simule un tri externe en mémoire limitée."""
    chunks_tries = []
    for i in range(0, len(data), chunk_size):
        chunk = sorted(data[i:i + chunk_size])
        chunks_tries.append(iter(chunk))
    return list(heapq.merge(*chunks_tries))

data = [5, 3, 8, 1, 9, 2, 7, 4, 6]
print(tri_externe(data, chunk_size=3))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
