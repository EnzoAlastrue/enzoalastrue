# ============================================================
# 04 — Tas (Heap)
# Min Heap, Max Heap, Heap Sort — O(log n)
# ============================================================

import heapq
import random

# ──────────────────────────────────────────────────────────
# 1. Concepts fondamentaux
# ──────────────────────────────────────────────────────────

# Un tas (heap) est un arbre binaire complet vérifiant la propriété de tas :
#
# Min-Heap : le parent est toujours ≤ à ses enfants
#            → la racine est le MINIMUM
#
# Max-Heap : le parent est toujours ≥ à ses enfants
#            → la racine est le MAXIMUM
#
# Représentation dans un tableau :
#   parent(i)      = (i - 1) // 2
#   enfant_gauche  = 2*i + 1
#   enfant_droit   = 2*i + 2
#
# Complexités :
#   insertion       O(log n)
#   extraction min  O(log n)
#   minimum         O(1)
#   construction    O(n)  — heapify

# ──────────────────────────────────────────────────────────
# 2. Min-Heap implémenté manuellement
# ──────────────────────────────────────────────────────────

class MinHeap:
    """
    Tas minimum.
    La racine contient toujours le plus petit élément.
    """

    def __init__(self):
        self._data = []

    # ── Accès aux indices ────────────────────────────────

    @staticmethod
    def _parent(i):
        return (i - 1) // 2

    @staticmethod
    def _gauche(i):
        return 2 * i + 1

    @staticmethod
    def _droit(i):
        return 2 * i + 2

    # ── Insertion ───────────────────────────────────────

    def inserer(self, valeur):
        """Insérer en fin, puis "percoler vers le haut" — O(log n)."""
        self._data.append(valeur)
        self._percoler_haut(len(self._data) - 1)

    def _percoler_haut(self, i):
        """Faire remonter l'élément à l'indice i vers sa position correcte."""
        while i > 0:
            p = self._parent(i)
            if self._data[i] < self._data[p]:
                self._data[i], self._data[p] = self._data[p], self._data[i]
                i = p
            else:
                break

    # ── Extraction ──────────────────────────────────────

    def extraire_min(self):
        """Retirer et retourner le minimum — O(log n)."""
        if self.est_vide():
            raise IndexError("Tas vide")
        # Échanger racine et dernier élément
        self._data[0], self._data[-1] = self._data[-1], self._data[0]
        minimum = self._data.pop()
        # Percoler vers le bas
        self._percoler_bas(0)
        return minimum

    def _percoler_bas(self, i):
        """Faire descendre l'élément à l'indice i vers sa position correcte."""
        n = len(self._data)
        while True:
            plus_petit = i
            g = self._gauche(i)
            d = self._droit(i)
            if g < n and self._data[g] < self._data[plus_petit]:
                plus_petit = g
            if d < n and self._data[d] < self._data[plus_petit]:
                plus_petit = d
            if plus_petit == i:
                break
            self._data[i], self._data[plus_petit] = self._data[plus_petit], self._data[i]
            i = plus_petit

    # ── Autres opérations ───────────────────────────────

    def minimum(self):
        """Consulter le minimum sans l'extraire — O(1)."""
        if self.est_vide():
            raise IndexError("Tas vide")
        return self._data[0]

    def construire(self, liste):
        """Construire un tas depuis une liste — O(n)."""
        self._data = liste[:]
        # Percoler vers le bas depuis le dernier nœud non-feuille
        for i in range(len(self._data) // 2 - 1, -1, -1):
            self._percoler_bas(i)

    def est_vide(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"MinHeap({self._data})"

    def est_valide(self):
        """Vérifier la propriété de tas."""
        for i in range(1, len(self._data)):
            p = self._parent(i)
            if self._data[p] > self._data[i]:
                return False
        return True


# Tests MinHeap
h = MinHeap()
for v in [5, 3, 8, 1, 9, 2, 7, 4, 6]:
    h.inserer(v)

print("Min Heap :", h)
print("Valide ? :", h.est_valide())

extraits = []
while not h.est_vide():
    extraits.append(h.extraire_min())
print("Extrait en ordre :", extraits)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Construction O(n)
h2 = MinHeap()
h2.construire([5, 3, 8, 1, 9, 2, 7, 4, 6])
print("Construit O(n) :", h2)
print("Valide ? :", h2.est_valide())


# ──────────────────────────────────────────────────────────
# 3. Max-Heap
# ──────────────────────────────────────────────────────────

class MaxHeap:
    """
    Tas maximum — implémenté en inversant les valeurs dans un min-heap.
    Astuce Python : stocker -valeur dans un min-heap.
    """

    def __init__(self):
        self._data = []  # stocke les valeurs négatives

    def inserer(self, valeur):
        heapq.heappush(self._data, -valeur)

    def extraire_max(self):
        if not self._data:
            raise IndexError("Tas vide")
        return -heapq.heappop(self._data)

    def maximum(self):
        if not self._data:
            raise IndexError("Tas vide")
        return -self._data[0]

    def est_vide(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"MaxHeap({[-x for x in self._data]})"


mh = MaxHeap()
for v in [5, 3, 8, 1, 9, 2, 7, 4, 6]:
    mh.inserer(v)
print("Max Heap :", mh)
print("Max :", mh.maximum())         # 9
print("Extrait :", mh.extraire_max())  # 9


# ──────────────────────────────────────────────────────────
# 4. Heap Sort — O(n log n)
# ──────────────────────────────────────────────────────────

def heap_sort(lst):
    """
    Tri par tas — O(n log n), en place, non stable.
    1. Construire un max-heap
    2. Extraire le max et le placer en fin de tableau
    """
    n = len(lst)

    def percoler_bas(lst, n, i):
        plus_grand = i
        g, d = 2 * i + 1, 2 * i + 2
        if g < n and lst[g] > lst[plus_grand]:
            plus_grand = g
        if d < n and lst[d] > lst[plus_grand]:
            plus_grand = d
        if plus_grand != i:
            lst[i], lst[plus_grand] = lst[plus_grand], lst[i]
            percoler_bas(lst, n, plus_grand)

    # Phase 1 : construire le max-heap O(n)
    for i in range(n // 2 - 1, -1, -1):
        percoler_bas(lst, n, i)

    # Phase 2 : extraire les éléments un par un O(n log n)
    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]  # max en fin
        percoler_bas(lst, i, 0)

    return lst

lst = [5, 3, 8, 1, 9, 2, 7, 4, 6]
print("Avant :", lst)
print("Après :", heap_sort(lst[:]))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# ──────────────────────────────────────────────────────────
# 5. Module heapq de Python
# ──────────────────────────────────────────────────────────

# heapq implémente un MIN-HEAP sur des listes Python standard

lst = [5, 3, 8, 1, 9, 2]

# heapify — convertir une liste en tas min O(n)
heapq.heapify(lst)
print("heapify :", lst)          # [1, 3, 2, 5, 9, 8] (tas valide)

# heappush — insertion O(log n)
heapq.heappush(lst, 0)
print("push(0) :", lst)

# heappop — extraction min O(log n)
print("pop :", heapq.heappop(lst))  # 0

# heappushpop — push puis pop (plus efficace que les deux séparément) O(log n)
result = heapq.heappushpop(lst, -1)
print("pushpop(-1) :", result)    # -1 (car -1 < min actuel)

# heapreplace — pop puis push O(log n)
result = heapq.heapreplace(lst, 100)
print("replace :", result)        # min extrait

# n plus petits / n plus grands
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print("3 plus petits :", heapq.nsmallest(3, data))  # [1, 1, 2]
print("3 plus grands :", heapq.nlargest(3, data))   # [9, 6, 5]

# Fusionner des iterables triés
a = [1, 4, 7]
b = [2, 5, 8]
c = [3, 6, 9]
print("merge :", list(heapq.merge(a, b, c)))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# File à priorité avec des tuples
taches = []
heapq.heappush(taches, (3, "réunion"))
heapq.heappush(taches, (1, "bug critique"))
heapq.heappush(taches, (2, "code review"))
while taches:
    prio, tache = heapq.heappop(taches)
    print(f"[{prio}] {tache}")


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Médiane glissante (running median) avec deux tas
class MedianeGlissante:
    """
    Maintenir la médiane dynamiquement.
    - max_heap : moitié inférieure (stockée négative pour simuler max-heap)
    - min_heap : moitié supérieure
    """
    def __init__(self):
        self._max_heap = []  # max-heap (valeurs négatives)
        self._min_heap = []  # min-heap

    def ajouter(self, num):
        heapq.heappush(self._max_heap, -num)
        # Équilibrer
        if (self._max_heap and self._min_heap and
                (-self._max_heap[0]) > self._min_heap[0]):
            val = -heapq.heappop(self._max_heap)
            heapq.heappush(self._min_heap, val)
        # Équilibrer les tailles
        if len(self._max_heap) > len(self._min_heap) + 1:
            val = -heapq.heappop(self._max_heap)
            heapq.heappush(self._min_heap, val)
        elif len(self._min_heap) > len(self._max_heap):
            val = heapq.heappop(self._min_heap)
            heapq.heappush(self._max_heap, -val)

    def mediane(self):
        if len(self._max_heap) == len(self._min_heap):
            return (-self._max_heap[0] + self._min_heap[0]) / 2
        return float(-self._max_heap[0])

mg = MedianeGlissante()
for num in [5, 15, 1, 3, 8, 7, 9, 11]:
    mg.ajouter(num)
    print(f"Ajout de {num:2} → médiane = {mg.mediane()}")

# Ex 2 : K éléments les plus fréquents
from collections import Counter

def top_k_frequent(lst, k):
    """K éléments les plus fréquents — O(n log k)."""
    compteur = Counter(lst)
    return heapq.nlargest(k, compteur, key=compteur.get)

print(top_k_frequent([1,1,1,2,2,3], 2))  # [1, 2]

# Ex 3 : Fusionner k listes triées
def fusionner_k_listes(listes):
    """Fusionner k listes triées — O(N log k) où N = total éléments."""
    tas = []
    for i, lst in enumerate(listes):
        if lst:
            heapq.heappush(tas, (lst[0], i, 0))
    resultat = []
    while tas:
        val, i, j = heapq.heappop(tas)
        resultat.append(val)
        if j + 1 < len(listes[i]):
            heapq.heappush(tas, (listes[i][j + 1], i, j + 1))
    return resultat

listes = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print(fusionner_k_listes(listes))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
