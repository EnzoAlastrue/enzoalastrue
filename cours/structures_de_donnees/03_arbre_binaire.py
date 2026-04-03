# ============================================================
# 03 — Arbre Binaire de Recherche (BST)
# Binary Search Tree — O(log n) moyen, O(n) pire cas
# ============================================================

from collections import deque

# ──────────────────────────────────────────────────────────
# 1. Nœud de l'arbre
# ──────────────────────────────────────────────────────────

class Noeud:
    def __init__(self, cle, valeur=None):
        self.cle      = cle
        self.valeur   = valeur if valeur is not None else cle
        self.gauche   = None
        self.droite   = None
        self.hauteur  = 1      # utilisé pour AVL

    def __repr__(self):
        return f"Noeud({self.cle})"


# ──────────────────────────────────────────────────────────
# 2. Arbre Binaire de Recherche (BST)
# ──────────────────────────────────────────────────────────

class ArbreBST:
    """
    Propriété BST : pour tout nœud n,
      tous les nœuds du sous-arbre gauche ont une clé < n.cle
      tous les nœuds du sous-arbre droit  ont une clé > n.cle

    Complexité (arbre équilibré) :
      recherche  O(log n)
      insertion  O(log n)
      suppression O(log n)
      Pire cas (dégénéré) : O(n)
    """

    def __init__(self):
        self.racine = None
        self._taille = 0

    # ── Insertion ───────────────────────────────────────

    def inserer(self, cle, valeur=None):
        self.racine = self._inserer(self.racine, cle, valeur)
        self._taille += 1

    def _inserer(self, noeud, cle, valeur):
        if noeud is None:
            return Noeud(cle, valeur)
        if cle < noeud.cle:
            noeud.gauche = self._inserer(noeud.gauche, cle, valeur)
        elif cle > noeud.cle:
            noeud.droite = self._inserer(noeud.droite, cle, valeur)
        else:
            noeud.valeur = valeur or cle  # mise à jour
            self._taille -= 1             # pas de nouveau nœud
        return noeud

    # ── Recherche ───────────────────────────────────────

    def chercher(self, cle):
        noeud = self._chercher(self.racine, cle)
        return noeud.valeur if noeud else None

    def _chercher(self, noeud, cle):
        if noeud is None or noeud.cle == cle:
            return noeud
        if cle < noeud.cle:
            return self._chercher(noeud.gauche, cle)
        return self._chercher(noeud.droite, cle)

    def contient(self, cle):
        return self._chercher(self.racine, cle) is not None

    # ── Suppression ─────────────────────────────────────

    def supprimer(self, cle):
        self.racine, supprime = self._supprimer(self.racine, cle)
        if supprime:
            self._taille -= 1

    def _supprimer(self, noeud, cle):
        if noeud is None:
            return noeud, False
        supprime = False
        if cle < noeud.cle:
            noeud.gauche, supprime = self._supprimer(noeud.gauche, cle)
        elif cle > noeud.cle:
            noeud.droite, supprime = self._supprimer(noeud.droite, cle)
        else:
            supprime = True
            # Cas 1 : feuille ou nœud avec un seul enfant
            if noeud.gauche is None:
                return noeud.droite, supprime
            if noeud.droite is None:
                return noeud.gauche, supprime
            # Cas 2 : deux enfants → remplacer par le successeur (min du droite)
            successeur = self._min_noeud(noeud.droite)
            noeud.cle    = successeur.cle
            noeud.valeur = successeur.valeur
            noeud.droite, _ = self._supprimer(noeud.droite, successeur.cle)
        return noeud, supprime

    def _min_noeud(self, noeud):
        while noeud.gauche:
            noeud = noeud.gauche
        return noeud

    def _max_noeud(self, noeud):
        while noeud.droite:
            noeud = noeud.droite
        return noeud

    # ── Parcours ────────────────────────────────────────

    def infixe(self):
        """Gauche → Racine → Droite : donne les éléments triés."""
        resultat = []
        self._infixe(self.racine, resultat)
        return resultat

    def _infixe(self, noeud, resultat):
        if noeud:
            self._infixe(noeud.gauche, resultat)
            resultat.append(noeud.cle)
            self._infixe(noeud.droite, resultat)

    def prefixe(self):
        """Racine → Gauche → Droite : utile pour copier/sérialiser."""
        resultat = []
        self._prefixe(self.racine, resultat)
        return resultat

    def _prefixe(self, noeud, resultat):
        if noeud:
            resultat.append(noeud.cle)
            self._prefixe(noeud.gauche, resultat)
            self._prefixe(noeud.droite, resultat)

    def postfixe(self):
        """Gauche → Droite → Racine : utile pour supprimer/évaluer."""
        resultat = []
        self._postfixe(self.racine, resultat)
        return resultat

    def _postfixe(self, noeud, resultat):
        if noeud:
            self._postfixe(noeud.gauche, resultat)
            self._postfixe(noeud.droite, resultat)
            resultat.append(noeud.cle)

    def par_niveau(self):
        """Parcours en largeur (BFS) — niveau par niveau."""
        if not self.racine:
            return []
        resultat = []
        file = deque([self.racine])
        while file:
            noeud = file.popleft()
            resultat.append(noeud.cle)
            if noeud.gauche:
                file.append(noeud.gauche)
            if noeud.droite:
                file.append(noeud.droite)
        return resultat

    # ── Propriétés ──────────────────────────────────────

    def hauteur(self):
        return self._hauteur(self.racine)

    def _hauteur(self, noeud):
        if noeud is None:
            return 0
        return 1 + max(self._hauteur(noeud.gauche),
                       self._hauteur(noeud.droite))

    def est_bst(self):
        """Vérifier si l'arbre respecte la propriété BST."""
        return self._est_bst(self.racine, float("-inf"), float("inf"))

    def _est_bst(self, noeud, mini, maxi):
        if noeud is None:
            return True
        if not (mini < noeud.cle < maxi):
            return False
        return (self._est_bst(noeud.gauche, mini, noeud.cle) and
                self._est_bst(noeud.droite, noeud.cle, maxi))

    def est_equilibre(self):
        """Vérifier si l'arbre est équilibré."""
        return self._est_equilibre(self.racine) != -1

    def _est_equilibre(self, noeud):
        if noeud is None:
            return 0
        h_g = self._est_equilibre(noeud.gauche)
        h_d = self._est_equilibre(noeud.droite)
        if h_g == -1 or h_d == -1 or abs(h_g - h_d) > 1:
            return -1
        return 1 + max(h_g, h_d)

    def min_val(self):
        if not self.racine:
            return None
        return self._min_noeud(self.racine).cle

    def max_val(self):
        if not self.racine:
            return None
        return self._max_noeud(self.racine).cle

    def predecesseur(self, cle):
        """Prédécesseur infixe (plus grand élément < cle)."""
        pred = None
        noeud = self.racine
        while noeud:
            if cle <= noeud.cle:
                noeud = noeud.gauche
            else:
                pred = noeud.cle
                noeud = noeud.droite
        return pred

    def successeur(self, cle):
        """Successeur infixe (plus petit élément > cle)."""
        succ = None
        noeud = self.racine
        while noeud:
            if cle >= noeud.cle:
                noeud = noeud.droite
            else:
                succ = noeud.cle
                noeud = noeud.gauche
        return succ

    def __len__(self):
        return self._taille

    def afficher(self, noeud=None, niveau=0, prefixe="Racine: "):
        """Affichage arborescent."""
        if noeud is None and niveau == 0:
            noeud = self.racine
        if noeud:
            print(" " * (niveau * 4) + prefixe + str(noeud.cle))
            if noeud.gauche or noeud.droite:
                if noeud.gauche:
                    self.afficher(noeud.gauche, niveau + 1, "G: ")
                else:
                    print(" " * ((niveau + 1) * 4) + "G: None")
                if noeud.droite:
                    self.afficher(noeud.droite, niveau + 1, "D: ")
                else:
                    print(" " * ((niveau + 1) * 4) + "D: None")


# ── Tests ──────────────────────────────────────────────────

bst = ArbreBST()
valeurs = [5, 3, 7, 1, 4, 6, 8, 2]
for v in valeurs:
    bst.inserer(v)

print("Infixe  :", bst.infixe())   # [1, 2, 3, 4, 5, 6, 7, 8]
print("Préfixe :", bst.prefixe())  # [5, 3, 1, 2, 4, 7, 6, 8]
print("Postfixe:", bst.postfixe()) # [2, 1, 4, 3, 6, 8, 7, 5]
print("Niveaux :", bst.par_niveau()) # [5, 3, 7, 1, 4, 6, 8, 2]
print("Hauteur :", bst.hauteur())   # 4
print("Min     :", bst.min_val())   # 1
print("Max     :", bst.max_val())   # 8
print("BST ?   :", bst.est_bst())   # True
print("Équil.? :", bst.est_equilibre())  # True
print("Pred(5) :", bst.predecesseur(5))  # 4
print("Succ(5) :", bst.successeur(5))    # 6

bst.afficher()

bst.supprimer(3)
print("\nAprès suppression de 3 :")
print("Infixe :", bst.infixe())    # [1, 2, 4, 5, 6, 7, 8]


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Construire un BST équilibré depuis une liste triée
def bst_depuis_triee(lst):
    """Construire un BST équilibré depuis une liste triée."""
    if not lst:
        return None
    milieu = len(lst) // 2
    noeud = Noeud(lst[milieu])
    noeud.gauche = bst_depuis_triee(lst[:milieu])
    noeud.droite = bst_depuis_triee(lst[milieu + 1:])
    return noeud

def afficher_arbre(racine, niveau=0):
    if racine:
        afficher_arbre(racine.droite, niveau + 1)
        print("  " * niveau + str(racine.cle))
        afficher_arbre(racine.gauche, niveau + 1)

racine = bst_depuis_triee([1, 2, 3, 4, 5, 6, 7])
afficher_arbre(racine)

# Ex 2 : LCA — Plus Bas Ancêtre Commun (Lowest Common Ancestor)
def lca(racine, n1, n2):
    """LCA dans un BST — O(log n) pour arbre équilibré."""
    if racine is None:
        return None
    if n1 < racine.cle and n2 < racine.cle:
        return lca(racine.gauche, n1, n2)
    if n1 > racine.cle and n2 > racine.cle:
        return lca(racine.droite, n1, n2)
    return racine.cle

bst2 = ArbreBST()
for v in [6, 2, 8, 0, 4, 7, 9, 3, 5]:
    bst2.inserer(v)

print("LCA(2,8) =", lca(bst2.racine, 2, 8))  # 6
print("LCA(2,4) =", lca(bst2.racine, 2, 4))  # 2
print("LCA(3,5) =", lca(bst2.racine, 3, 5))  # 4

# Ex 3 : k-ième plus petit élément
def kieme_plus_petit(racine, k):
    """Trouver le k-ième plus petit élément — O(n)."""
    pile = []
    courant = racine
    compteur = 0
    while courant or pile:
        while courant:
            pile.append(courant)
            courant = courant.gauche
        courant = pile.pop()
        compteur += 1
        if compteur == k:
            return courant.cle
        courant = courant.droite
    return None

print("3e plus petit :", kieme_plus_petit(bst2.racine, 3))  # 3
