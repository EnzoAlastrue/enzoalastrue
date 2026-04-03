# ============================================================
# 04 — Collections : Listes, Tuples, Dicts, Ensembles
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. Listes (list) — mutables, ordonnées
# ──────────────────────────────────────────────────────────

# Création
vide = []
nombres = [1, 2, 3, 4, 5]
mixte  = [1, "deux", 3.0, True, None]
matrice = [[1, 2], [3, 4], [5, 6]]

# Accès et slicing
print(nombres[0])     # 1
print(nombres[-1])    # 5
print(nombres[1:4])   # [2, 3, 4]
print(nombres[::2])   # [1, 3, 5]
print(nombres[::-1])  # [5, 4, 3, 2, 1]

# Modification
nombres[0] = 10
nombres[1:3] = [20, 30]
print(nombres)  # [10, 20, 30, 4, 5]

# Méthodes principales
lst = [3, 1, 4, 1, 5, 9, 2, 6]

lst.append(7)          # ajouter à la fin
lst.insert(0, 0)       # insérer à l'indice 0
lst.extend([8, 9])     # concatener une liste

lst.remove(1)          # supprimer la 1re occurrence de 1
element = lst.pop()    # supprimer et retourner le dernier
element = lst.pop(0)   # supprimer et retourner l'indice 0

print(lst.count(1))    # nombre d'occurrences de 1
print(lst.index(9))    # indice de la 1re occurrence

lst.sort()             # tri en place (modifie la liste)
lst.sort(reverse=True) # tri décroissant
lst.reverse()          # inverser en place

copie = lst.copy()     # copie superficielle
lst.clear()            # vider la liste

# Fonctions built-in
nums = [3, 1, 4, 1, 5, 9]
print(len(nums))        # 6
print(min(nums))        # 1
print(max(nums))        # 9
print(sum(nums))        # 23
print(sorted(nums))     # [1, 1, 3, 4, 5, 9]  — nouvelle liste
print(list(reversed(nums)))  # [9, 5, 1, 4, 1, 3]

# any / all
print(any(x > 8 for x in nums))   # True
print(all(x > 0 for x in nums))   # True


# ──────────────────────────────────────────────────────────
# 2. Tuples (tuple) — immuables, ordonnés
# ──────────────────────────────────────────────────────────

# Création
vide = ()
singleton = (1,)       # virgule obligatoire pour 1 élément !
coords = (48.8566, 2.3522)
rgb = 255, 128, 0      # les parenthèses sont optionnelles

# Accès (identique aux listes, mais pas de modification)
print(coords[0])       # 48.8566
print(rgb[-1])         # 0

# Déballage
latitude, longitude = coords
r, g, b = rgb

# Tuples nommés (namedtuple)
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)        # 3 4
print(p[0], p[1])      # 3 4

# Usage : retourner plusieurs valeurs, clés de dictionnaire
memo = {}
key = (1, 2)           # tuple comme clé (hashable)
memo[key] = "valeur"

# Performances : les tuples sont plus rapides et moins gourmands en mémoire
import sys
lst_  = [0] * 100
tup_  = (0,) * 100
print(sys.getsizeof(lst_))  # plus grand
print(sys.getsizeof(tup_))  # plus petit


# ──────────────────────────────────────────────────────────
# 3. Dictionnaires (dict) — mutables, ordonnés (Python 3.7+)
# ──────────────────────────────────────────────────────────

# Création
vide = {}
etudiant = {"nom": "Enzo", "age": 21, "note": 15.5}
d = dict(nom="Alice", age=25)

# Accès
print(etudiant["nom"])              # Enzo
print(etudiant.get("prenom", "?")) # ? (clé inexistante → valeur par défaut)

# Modification
etudiant["ville"] = "Paris"   # ajout
etudiant["age"] = 22          # modification
del etudiant["note"]          # suppression

# Méthodes
print(etudiant.keys())         # dict_keys([...])
print(etudiant.values())       # dict_values([...])
print(etudiant.items())        # dict_items([...])

# Itération
for cle, val in etudiant.items():
    print(f"  {cle}: {val}")

# pop / popitem
val = etudiant.pop("ville", None)   # supprime et retourne
cle, val = etudiant.popitem()       # supprime le dernier

# update — fusionner
etudiant.update({"note": 16, "mention": "Bien"})

# setdefault — ajouter si la clé n'existe pas
etudiant.setdefault("pays", "France")

# Fusion (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
fusion = d1 | d2          # {"a": 1, "b": 3, "c": 4}
d1 |= d2                  # modification en place

# defaultdict — valeur par défaut automatique
from collections import defaultdict

compteur = defaultdict(int)
mots = "le chat est sur le tapis le chat".split()
for mot in mots:
    compteur[mot] += 1
print(dict(compteur))  # {'le': 3, 'chat': 2, ...}

# Counter
from collections import Counter
c = Counter(mots)
print(c.most_common(2))  # [('le', 3), ('chat', 2)]

# OrderedDict (Python 3.7+ : dict standard déjà ordonné)
from collections import OrderedDict
od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

# Compréhension de dictionnaire
carres = {x: x**2 for x in range(6)}
print(carres)  # {0: 0, 1: 1, 2: 4, ...}

# Inverser clés/valeurs
inverse = {v: k for k, v in carres.items()}


# ──────────────────────────────────────────────────────────
# 4. Ensembles (set) — mutables, non ordonnés, uniques
# ──────────────────────────────────────────────────────────

# Création
vide = set()           # {} crée un dict, pas un set !
couleurs = {"rouge", "vert", "bleu"}
depuis_liste = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Modification
couleurs.add("jaune")
couleurs.discard("violet")  # pas d'erreur si absent
couleurs.remove("rouge")    # KeyError si absent

# Opérations ensemblistes
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A | B)   # union         {1,2,3,4,5,6,7,8}
print(A & B)   # intersection  {4,5}
print(A - B)   # différence    {1,2,3}
print(A ^ B)   # diff. symétrique {1,2,3,6,7,8}

print(A.issubset({1, 2, 3, 4, 5, 6}))   # True
print(A.issuperset({1, 2}))              # True
print(A.isdisjoint({10, 11}))            # True

# frozenset — ensemble immuable (peut être clé de dict)
fs = frozenset([1, 2, 3])


# ──────────────────────────────────────────────────────────
# 5. Opérations communes & bonnes pratiques
# ──────────────────────────────────────────────────────────

# Test d'appartenance — O(1) pour set/dict, O(n) pour list/tuple
big_list = list(range(10000))
big_set  = set(range(10000))

import time

t0 = time.perf_counter()
for _ in range(10000):
    _ = 9999 in big_list
print(f"list  : {time.perf_counter()-t0:.4f}s")

t0 = time.perf_counter()
for _ in range(10000):
    _ = 9999 in big_set
print(f"set   : {time.perf_counter()-t0:.4f}s")

# Copie profonde vs superficielle
import copy
original = [[1, 2], [3, 4]]
superficielle = original.copy()
profonde = copy.deepcopy(original)

original[0][0] = 99
print(superficielle)  # [[99, 2], [3, 4]] — affecté !
print(profonde)       # [[1, 2], [3, 4]]  — protégé


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Fréquence des caractères dans une chaîne
def frequence(texte):
    return Counter(c for c in texte.lower() if c.isalpha())

print(frequence("Python est super"))

# Ex 2 : Grouper les anagrammes
def grouper_anagrammes(mots):
    groupes = defaultdict(list)
    for mot in mots:
        cle = tuple(sorted(mot))
        groupes[cle].append(mot)
    return list(groupes.values())

print(grouper_anagrammes(["eat","tea","tan","ate","nat","bat"]))

# Ex 3 : Intersection de listes sans doublons
def intersection(*listes):
    return list(set(listes[0]).intersection(*listes[1:]))

print(intersection([1,2,3,4], [2,4,6], [2,4,8]))  # [2, 4]
