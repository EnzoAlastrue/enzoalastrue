# ============================================================
# 05 — Diviser pour Régner
# Tours de Hanoï, Karatsuba, Sous-tableau maximum, Puissance
# ============================================================

# Paradigme : Diviser pour Régner (Divide & Conquer)
#   1. DIVISER  : découper le problème en sous-problèmes plus petits
#   2. RÉGNER   : résoudre chaque sous-problème récursivement
#   3. COMBINER : fusionner les solutions des sous-problèmes
#
# Exemples célèbres : Merge Sort, Quick Sort, FFT, Strassen

# ──────────────────────────────────────────────────────────
# 1. Tours de Hanoï — O(2ⁿ)
# ──────────────────────────────────────────────────────────
#
# Problème : Déplacer n disques de la source à la cible
#   - Un seul disque déplacé à la fois
#   - Un disque plus grand ne peut pas poser sur un plus petit
#
# Solution récursive :
#   - Déplacer n-1 disques de source vers auxiliaire
#   - Déplacer le plus grand disque vers la cible
#   - Déplacer n-1 disques de auxiliaire vers cible
#
# Nombre minimum de mouvements : 2ⁿ - 1

mouvements = []

def hanoi(n, source="A", cible="C", auxiliaire="B"):
    """Résoudre les tours de Hanoï pour n disques."""
    if n == 1:
        mouvement = f"Disque 1 : {source} → {cible}"
        mouvements.append(mouvement)
        print(mouvement)
        return
    hanoi(n - 1, source, auxiliaire, cible)
    mouvement = f"Disque {n} : {source} → {cible}"
    mouvements.append(mouvement)
    print(mouvement)
    hanoi(n - 1, auxiliaire, cible, source)

def hanoi_iteratif(n):
    """Version itérative des tours de Hanoï."""
    import math
    total = 2**n - 1
    piquets = ["A", "B", "C"]

    if n % 2 == 0:
        piquets[1], piquets[2] = piquets[2], piquets[1]

    tours = [list(range(n, 0, -1)), [], []]
    source, auxiliaire, cible = 0, 1, 2

    for i in range(1, total + 1):
        if i % 3 == 1:
            _deplacer(tours, source, cible, piquets)
        elif i % 3 == 2:
            _deplacer(tours, source, auxiliaire, piquets)
        else:
            _deplacer(tours, auxiliaire, cible, piquets)

def _deplacer(tours, de, vers, piquets):
    if not tours[de] and not tours[vers]:
        return
    if not tours[de]:
        de, vers = vers, de
    elif tours[vers] and tours[de][-1] > tours[vers][-1]:
        de, vers = vers, de
    disque = tours[de].pop()
    tours[vers].append(disque)
    print(f"Disque {disque} : {piquets[de]} → {piquets[vers]}")

print("=== Tours de Hanoï (n=3) ===")
hanoi(3)
print(f"Nombre de mouvements : {len(mouvements)}")  # 7 = 2³ - 1


# ──────────────────────────────────────────────────────────
# 2. Multiplication de Karatsuba — O(n^1.585)
# ──────────────────────────────────────────────────────────
#
# Multiplication naïve de grands entiers : O(n²)
# Karatsuba : O(n^log₂(3)) ≈ O(n^1.585)
#
# Formule :
#   x = x₁ * B^m + x₀
#   y = y₁ * B^m + y₀
#   x*y = z₂*B^2m + z₁*B^m + z₀
#   où :
#     z₂ = x₁ * y₁
#     z₀ = x₀ * y₀
#     z₁ = (x₁+x₀)(y₁+y₀) - z₂ - z₀  ← 3 mult. au lieu de 4 !

def karatsuba(x, y):
    """Multiplication de grands entiers par Karatsuba."""
    # Cas de base
    if x < 10 or y < 10:
        return x * y

    # Taille
    n = max(len(str(x)), len(str(y)))
    m = n // 2

    # Découpage
    facteur = 10 ** m
    x1, x0 = divmod(x, facteur)
    y1, y0 = divmod(y, facteur)

    # Récursion (3 multiplications au lieu de 4)
    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1 + x0, y1 + y0) - z2 - z0

    return z2 * (10 ** (2 * m)) + z1 * (10 ** m) + z0

# Test
a = 12345678901234567890
b = 98765432109876543210
res_karatsuba = karatsuba(a, b)
res_python    = a * b
print(f"Karatsuba  : {res_karatsuba}")
print(f"Python     : {res_python}")
print(f"Correct ?  : {res_karatsuba == res_python}")


# ──────────────────────────────────────────────────────────
# 3. Sous-tableau de somme maximale (Algorithme de Kadane modifié D&C)
# ──────────────────────────────────────────────────────────
#
# Problème : trouver la sous-séquence contiguë dont la somme est maximale.
#
# Approche Diviser pour Régner : O(n log n)
#   - Diviser : milieu
#   - Cas 1   : sous-tableau entièrement dans la moitié gauche
#   - Cas 2   : sous-tableau entièrement dans la moitié droite
#   - Cas 3   : sous-tableau qui passe par le milieu

def sous_tableau_max_crossing(lst, bas, milieu, haut):
    """Trouver la somme max d'un sous-tableau passant par milieu."""
    # Partie gauche (de milieu vers bas)
    somme = 0
    somme_gauche = float("-inf")
    idx_gauche = milieu
    for i in range(milieu, bas - 1, -1):
        somme += lst[i]
        if somme > somme_gauche:
            somme_gauche = somme
            idx_gauche = i

    # Partie droite (de milieu+1 vers haut)
    somme = 0
    somme_droite = float("-inf")
    idx_droite = milieu + 1
    for i in range(milieu + 1, haut + 1):
        somme += lst[i]
        if somme > somme_droite:
            somme_droite = somme
            idx_droite = i

    return idx_gauche, idx_droite, somme_gauche + somme_droite

def sous_tableau_max_dc(lst, bas, haut):
    """Diviser pour régner : O(n log n)."""
    if bas == haut:
        return bas, haut, lst[bas]

    milieu = (bas + haut) // 2
    g_bas, g_haut, g_somme = sous_tableau_max_dc(lst, bas, milieu)
    d_bas, d_haut, d_somme = sous_tableau_max_dc(lst, milieu + 1, haut)
    c_bas, c_haut, c_somme = sous_tableau_max_crossing(lst, bas, milieu, haut)

    if g_somme >= d_somme and g_somme >= c_somme:
        return g_bas, g_haut, g_somme
    elif d_somme >= g_somme and d_somme >= c_somme:
        return d_bas, d_haut, d_somme
    else:
        return c_bas, c_haut, c_somme

# Version O(n) — Algorithme de Kadane (plus simple)
def kadane(lst):
    """Sous-tableau de somme maximale en O(n)."""
    max_courant = max_global = lst[0]
    debut = fin = debut_courant = 0
    for i in range(1, len(lst)):
        if lst[i] > max_courant + lst[i]:
            max_courant = lst[i]
            debut_courant = i
        else:
            max_courant += lst[i]
        if max_courant > max_global:
            max_global = max_courant
            debut = debut_courant
            fin = i
    return debut, fin, max_global

lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
bas, haut, somme = sous_tableau_max_dc(lst, 0, len(lst) - 1)
print(f"D&C     : lst[{bas}:{haut+1}] = {lst[bas:haut+1]}, somme = {somme}")

d, f, s = kadane(lst)
print(f"Kadane  : lst[{d}:{f+1}] = {lst[d:f+1]}, somme = {s}")


# ──────────────────────────────────────────────────────────
# 4. Exponentiation rapide — O(log n)
# ──────────────────────────────────────────────────────────
#
# base^exp :
#   Si exp est pair  : (base²)^(exp/2)
#   Si exp est impair: base * base^(exp-1)

def puissance_rapide(base, exp, mod=None):
    """Exponentiation rapide avec modulo optionnel."""
    if exp == 0:
        return 1
    if exp < 0:
        return puissance_rapide(1 / base, -exp, mod)

    if exp % 2 == 0:
        moitie = puissance_rapide(base, exp // 2, mod)
        resultat = moitie * moitie
    else:
        resultat = base * puissance_rapide(base, exp - 1, mod)

    return resultat % mod if mod else resultat

# Version itérative (évite la récursion)
def puissance_rapide_iter(base, exp, mod=None):
    resultat = 1
    while exp > 0:
        if exp % 2 == 1:
            resultat = (resultat * base) % mod if mod else resultat * base
        base = (base * base) % mod if mod else base * base
        exp //= 2
    return resultat

print(puissance_rapide(2, 10))          # 1024
print(puissance_rapide_iter(2, 100))    # 1267650600228229401496703205376

# Chiffrement RSA utilise pow(base, exp, mod) — Python utilise l'exp. rapide
print(pow(2, 10, 1000))               # 24 = 1024 % 1000


# ──────────────────────────────────────────────────────────
# 5. Recherche de la paire la plus proche — O(n log n)
# ──────────────────────────────────────────────────────────
#
# Problème : trouver les deux points les plus proches dans un plan.
# Approche naïve : O(n²)
# D&C : O(n log n)

import math

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def paire_proche_bande(bande, d):
    """Chercher dans la bande verticale de largeur 2d."""
    min_d = d
    bande.sort(key=lambda p: p[1])
    for i in range(len(bande)):
        j = i + 1
        while j < len(bande) and (bande[j][1] - bande[i][1]) < min_d:
            min_d = min(min_d, distance(bande[i], bande[j]))
            j += 1
    return min_d

def paire_proche_dc(points):
    """Paire la plus proche par D&C."""
    n = len(points)
    if n <= 3:
        return min(distance(points[i], points[j])
                   for i in range(n) for j in range(i+1, n))

    milieu = n // 2
    milieu_x = points[milieu][0]

    d_gauche = paire_proche_dc(points[:milieu])
    d_droite = paire_proche_dc(points[milieu:])
    d = min(d_gauche, d_droite)

    bande = [p for p in points if abs(p[0] - milieu_x) < d]
    return min(d, paire_proche_bande(bande, d))

import random
points = sorted([(random.randint(0, 100), random.randint(0, 100))
                 for _ in range(20)])
d_optimal = paire_proche_dc(points)
d_naif = min(distance(points[i], points[j])
             for i in range(len(points))
             for j in range(i+1, len(points)))

print(f"D&C  : {d_optimal:.4f}")
print(f"Naïf : {d_naif:.4f}")
print(f"OK   : {abs(d_optimal - d_naif) < 1e-9}")


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Calculer x^n avec x et n entiers, sans ** ni pow()
def puiss(x, n):
    if n == 0: return 1
    if n == 1: return x
    if n < 0:  return puiss(1/x, -n)
    m = puiss(x, n // 2)
    return m * m if n % 2 == 0 else m * m * x

print(puiss(2, 10))  # 1024

# Ex 2 : Trier une liste de 0, 1 et 2 (Problème du drapeau hollandais)
def drapeau_hollandais(lst):
    """Partitionner en 3 groupes en un seul passage O(n)."""
    bas, milieu, haut = 0, 0, len(lst) - 1
    while milieu <= haut:
        if lst[milieu] == 0:
            lst[bas], lst[milieu] = lst[milieu], lst[bas]
            bas += 1; milieu += 1
        elif lst[milieu] == 1:
            milieu += 1
        else:
            lst[milieu], lst[haut] = lst[haut], lst[milieu]
            haut -= 1
    return lst

print(drapeau_hollandais([2, 0, 2, 1, 1, 0]))  # [0, 0, 1, 1, 2, 2]

# Ex 3 : Inversion de tableau par D&C
def inverser_dc(lst, gauche=0, droite=None):
    if droite is None:
        droite = len(lst) - 1
    if gauche >= droite:
        return lst
    lst[gauche], lst[droite] = lst[droite], lst[gauche]
    return inverser_dc(lst, gauche + 1, droite - 1)

print(inverser_dc([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
