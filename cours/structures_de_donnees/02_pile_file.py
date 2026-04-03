# ============================================================
# 02 — Pile & File
# Stack, Queue, Deque, Priority Queue
# ============================================================

from collections import deque
import heapq

# ──────────────────────────────────────────────────────────
# 1. Pile (Stack) — LIFO : Last In, First Out
# ──────────────────────────────────────────────────────────

class Pile:
    """
    Pile implémentée avec une liste Python.
    push  O(1) amorti
    pop   O(1)
    peek  O(1)
    """

    def __init__(self):
        self._donnees = []

    def empiler(self, valeur):
        """push — ajouter au sommet."""
        self._donnees.append(valeur)

    def depiler(self):
        """pop — retirer du sommet."""
        if self.est_vide():
            raise IndexError("Pile vide")
        return self._donnees.pop()

    def sommet(self):
        """peek — consulter sans retirer."""
        if self.est_vide():
            raise IndexError("Pile vide")
        return self._donnees[-1]

    def est_vide(self):
        return len(self._donnees) == 0

    def __len__(self):
        return len(self._donnees)

    def __repr__(self):
        if not self._donnees:
            return "Pile vide"
        return " | ".join(str(x) for x in self._donnees) + " ← sommet"


# Applications classiques des piles

def verifier_parentheses(expression):
    """Vérifier si les parenthèses/crochets/accolades sont équilibrés."""
    pile = Pile()
    ouvrants = "({["
    fermants = ")}]"
    correspondance = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in ouvrants:
            pile.empiler(char)
        elif char in fermants:
            if pile.est_vide() or pile.sommet() != correspondance[char]:
                return False
            pile.depiler()
    return pile.est_vide()

tests = ["(())", "({[]})", "([)]", "(()", "{}", ""]
for t in tests:
    print(f"'{t}' → {verifier_parentheses(t)}")


def evaluer_postfixe(expression):
    """Évaluer une expression en notation postfixe (polonaise inverse)."""
    # Exemple : "3 4 + 2 *" = (3+4)*2 = 14
    pile = Pile()
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    for token in expression.split():
        if token in ops:
            b = pile.depiler()
            a = pile.depiler()
            pile.empiler(ops[token](a, b))
        else:
            pile.empiler(float(token))
    return pile.depiler()

print(evaluer_postfixe("3 4 + 2 *"))   # 14.0
print(evaluer_postfixe("5 1 2 + 4 * + 3 -"))  # 14.0


def inverser_chaine(s):
    """Inverser une chaîne avec une pile."""
    pile = Pile()
    for char in s:
        pile.empiler(char)
    return "".join(pile.depiler() for _ in range(len(pile)))

print(inverser_chaine("Python"))  # nohtyP


def parcours_dfs_iteratif(graphe, depart):
    """DFS (profondeur d'abord) avec pile explicite."""
    visites = []
    pile = Pile()
    pile.empiler(depart)
    vus = {depart}
    while not pile.est_vide():
        sommet = pile.depiler()
        visites.append(sommet)
        for voisin in reversed(graphe.get(sommet, [])):
            if voisin not in vus:
                vus.add(voisin)
                pile.empiler(voisin)
    return visites

graphe = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [], "E": [], "F": []
}
print("DFS :", parcours_dfs_iteratif(graphe, "A"))  # A B D E C F


# ──────────────────────────────────────────────────────────
# 2. File (Queue) — FIFO : First In, First Out
# ──────────────────────────────────────────────────────────

class File:
    """
    File implémentée avec collections.deque.
    enfiler  O(1)
    defiler  O(1)
    front    O(1)
    """

    def __init__(self):
        self._donnees = deque()

    def enfiler(self, valeur):
        """enqueue — ajouter à la queue."""
        self._donnees.append(valeur)

    def defiler(self):
        """dequeue — retirer de la tête."""
        if self.est_vide():
            raise IndexError("File vide")
        return self._donnees.popleft()

    def devant(self):
        """Consulter le premier élément sans le retirer."""
        if self.est_vide():
            raise IndexError("File vide")
        return self._donnees[0]

    def est_vide(self):
        return len(self._donnees) == 0

    def __len__(self):
        return len(self._donnees)

    def __repr__(self):
        return "→ " + " → ".join(str(x) for x in self._donnees)


def parcours_bfs(graphe, depart):
    """BFS (largeur d'abord) avec file."""
    visites = []
    file = File()
    file.enfiler(depart)
    vus = {depart}
    while not file.est_vide():
        sommet = file.defiler()
        visites.append(sommet)
        for voisin in graphe.get(sommet, []):
            if voisin not in vus:
                vus.add(voisin)
                file.enfiler(voisin)
    return visites

print("BFS :", parcours_bfs(graphe, "A"))  # A B C D E F


# ──────────────────────────────────────────────────────────
# 3. Deque (Double-Ended Queue) — O(1) des deux côtés
# ──────────────────────────────────────────────────────────

d = deque([1, 2, 3, 4, 5], maxlen=5)
print(d)                    # deque([1, 2, 3, 4, 5], maxlen=5)

d.appendleft(0)             # ajouter à gauche (enlève le dernier si maxlen)
d.append(6)                 # ajouter à droite (enlève le premier si maxlen)
print(d)                    # deque([0, 1, 2, 3, 4], maxlen=5)... variable

d2 = deque([1, 2, 3, 4, 5])
d2.rotate(2)                # rotation : [4, 5, 1, 2, 3]
print(d2)
d2.rotate(-2)               # rotation inverse : [1, 2, 3, 4, 5]
print(d2)


def est_palindrome_deque(s):
    """Vérifier palindrome avec deque — O(n)."""
    d = deque(s.lower().replace(" ", ""))
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

for mot in ["kayak", "python", "radar", "niveau"]:
    print(f"'{mot}' palindrome ? {est_palindrome_deque(mot)}")


# ──────────────────────────────────────────────────────────
# 4. File à priorité (Priority Queue) — O(log n) insertion/extraction
# ──────────────────────────────────────────────────────────

class FilePriorite:
    """
    File à priorité basée sur un tas min (heapq).
    Insertion  : O(log n)
    Extraction : O(log n)
    Min        : O(1)
    """

    def __init__(self):
        self._tas = []
        self._compteur = 0  # tie-breaking : ordre FIFO pour priorités égales

    def inserer(self, donnee, priorite):
        """Insérer avec priorité (plus faible = plus prioritaire)."""
        heapq.heappush(self._tas, (priorite, self._compteur, donnee))
        self._compteur += 1

    def extraire_min(self):
        """Extraire l'élément de plus haute priorité (priorité min)."""
        if self.est_vide():
            raise IndexError("File vide")
        priorite, _, donnee = heapq.heappop(self._tas)
        return donnee, priorite

    def consulter_min(self):
        if self.est_vide():
            raise IndexError("File vide")
        return self._tas[0][2], self._tas[0][0]

    def est_vide(self):
        return len(self._tas) == 0

    def __len__(self):
        return len(self._tas)


fp = FilePriorite()
fp.inserer("tâche basse priorité",    3)
fp.inserer("tâche haute priorité",    1)
fp.inserer("tâche moyenne priorité",  2)
fp.inserer("urgence",                 1)  # même priorité → FIFO

while not fp.est_vide():
    tache, prio = fp.extraire_min()
    print(f"[prio={prio}] {tache}")


# File à priorité avec heapq directement
taches = []
heapq.heappush(taches, (5, "répondre emails"))
heapq.heappush(taches, (1, "corriger bug critique"))
heapq.heappush(taches, (3, "réunion"))

while taches:
    prio, tache = heapq.heappop(taches)
    print(f"{prio}: {tache}")

# n plus petits / n plus grands éléments
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(heapq.nsmallest(3, data))  # [1, 1, 2]
print(heapq.nlargest(3, data))   # [9, 6, 5]


# ──────────────────────────────────────────────────────────
# 5. File avec deux piles
# ──────────────────────────────────────────────────────────

class FileAvecPiles:
    """Implémenter une file avec deux piles — O(1) amorti."""

    def __init__(self):
        self._entree = []   # pile d'entrée (enfiler)
        self._sortie = []   # pile de sortie (défiler)

    def enfiler(self, valeur):
        self._entree.append(valeur)

    def defiler(self):
        if not self._sortie:
            # Transférer entree → sortie (inverse l'ordre)
            while self._entree:
                self._sortie.append(self._entree.pop())
        if not self._sortie:
            raise IndexError("File vide")
        return self._sortie.pop()

    def est_vide(self):
        return not self._entree and not self._sortie


f2p = FileAvecPiles()
for v in [1, 2, 3, 4, 5]:
    f2p.enfiler(v)
print(f2p.defiler())  # 1
print(f2p.defiler())  # 2
f2p.enfiler(6)
print(f2p.defiler())  # 3


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Évaluer une expression infixe (conversion → postfixe + évaluation)
def infixe_vers_postfixe(expression):
    """Algorithme shunting-yard de Dijkstra."""
    priorites = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    sortie = []
    ops = Pile()
    for token in expression.split():
        if token.lstrip("-").isdigit():
            sortie.append(token)
        elif token in priorites:
            while (not ops.est_vide() and
                   ops.sommet() in priorites and
                   priorites[ops.sommet()] >= priorites[token]):
                sortie.append(ops.depiler())
            ops.empiler(token)
        elif token == "(":
            ops.empiler(token)
        elif token == ")":
            while not ops.est_vide() and ops.sommet() != "(":
                sortie.append(ops.depiler())
            if not ops.est_vide():
                ops.depiler()  # retirer "("
    while not ops.est_vide():
        sortie.append(ops.depiler())
    return " ".join(sortie)

expr = "3 + 4 * 2"
postfixe = infixe_vers_postfixe(expr)
print(f"{expr} → {postfixe} = {evaluer_postfixe(postfixe)}")

# Ex 2 : File circulaire
class FileCirculaire:
    def __init__(self, capacite):
        self._data = [None] * capacite
        self._tete = 0
        self._taille = 0
        self._capacite = capacite

    def enfiler(self, val):
        if self._taille == self._capacite:
            raise OverflowError("File pleine")
        idx = (self._tete + self._taille) % self._capacite
        self._data[idx] = val
        self._taille += 1

    def defiler(self):
        if self._taille == 0:
            raise IndexError("File vide")
        val = self._data[self._tete]
        self._tete = (self._tete + 1) % self._capacite
        self._taille -= 1
        return val

fc = FileCirculaire(5)
for v in [1, 2, 3]:
    fc.enfiler(v)
print(fc.defiler())  # 1
fc.enfiler(4)
print(fc.defiler())  # 2

# Ex 3 : Flux glissant de taille k — maximum de chaque fenêtre
from collections import deque

def max_fenetre_glissante(lst, k):
    """Trouver le max de chaque fenêtre de taille k — O(n)."""
    resultat = []
    dq = deque()  # indices, décroissant par valeur

    for i, val in enumerate(lst):
        # Retirer les indices hors de la fenêtre
        while dq and dq[0] <= i - k:
            dq.popleft()
        # Retirer les indices avec des valeurs plus petites
        while dq and lst[dq[-1]] <= val:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            resultat.append(lst[dq[0]])
    return resultat

print(max_fenetre_glissante([1, 3, -1, -3, 5, 3, 6, 7], 3))
# [3, 3, 5, 5, 6, 7]
