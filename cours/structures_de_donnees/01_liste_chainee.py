# ============================================================
# 01 — Liste chaînée (Linked List)
# Singly Linked List & Doubly Linked List
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. Liste simplement chaînée (Singly Linked List)
# ──────────────────────────────────────────────────────────

class Noeud:
    """Nœud d'une liste simplement chaînée."""
    def __init__(self, donnee):
        self.donnee = donnee
        self.suivant = None

    def __repr__(self):
        return f"Noeud({self.donnee})"


class ListeChainee:
    """
    Liste simplement chaînée.

    Opérations :
      insertion_tete  O(1)
      insertion_queue O(1) avec pointeur sur queue
      insertion_pos   O(n)
      suppression     O(n)
      recherche       O(n)
      acces indice    O(n)
    """

    def __init__(self):
        self.tete  = None
        self.queue = None
        self._taille = 0

    # ── Propriétés ──────────────────────────────────────

    def __len__(self):
        return self._taille

    def est_vide(self):
        return self.tete is None

    # ── Insertions ──────────────────────────────────────

    def inserer_tete(self, donnee):
        """Insérer en tête — O(1)."""
        nouveau = Noeud(donnee)
        nouveau.suivant = self.tete
        self.tete = nouveau
        if self.queue is None:
            self.queue = nouveau
        self._taille += 1

    def inserer_queue(self, donnee):
        """Insérer en queue — O(1)."""
        nouveau = Noeud(donnee)
        if self.est_vide():
            self.tete = self.queue = nouveau
        else:
            self.queue.suivant = nouveau
            self.queue = nouveau
        self._taille += 1

    def inserer_position(self, donnee, position):
        """Insérer à la position donnée — O(n)."""
        if position < 0 or position > self._taille:
            raise IndexError(f"Position invalide : {position}")
        if position == 0:
            self.inserer_tete(donnee)
            return
        if position == self._taille:
            self.inserer_queue(donnee)
            return
        courant = self.tete
        for _ in range(position - 1):
            courant = courant.suivant
        nouveau = Noeud(donnee)
        nouveau.suivant = courant.suivant
        courant.suivant = nouveau
        self._taille += 1

    # ── Suppressions ────────────────────────────────────

    def supprimer_tete(self):
        """Supprimer et retourner l'élément en tête — O(1)."""
        if self.est_vide():
            raise IndexError("Liste vide")
        donnee = self.tete.donnee
        self.tete = self.tete.suivant
        if self.tete is None:
            self.queue = None
        self._taille -= 1
        return donnee

    def supprimer_valeur(self, valeur):
        """Supprimer la première occurrence de valeur — O(n)."""
        if self.est_vide():
            raise ValueError(f"{valeur} non trouvé")
        if self.tete.donnee == valeur:
            return self.supprimer_tete()
        courant = self.tete
        while courant.suivant:
            if courant.suivant.donnee == valeur:
                if courant.suivant == self.queue:
                    self.queue = courant
                courant.suivant = courant.suivant.suivant
                self._taille -= 1
                return valeur
            courant = courant.suivant
        raise ValueError(f"{valeur} non trouvé")

    # ── Recherche ───────────────────────────────────────

    def contient(self, valeur):
        """Vérifier si la valeur est présente — O(n)."""
        courant = self.tete
        while courant:
            if courant.donnee == valeur:
                return True
            courant = courant.suivant
        return False

    def obtenir(self, index):
        """Obtenir l'élément à l'indice — O(n)."""
        if index < 0:
            index += self._taille
        if not (0 <= index < self._taille):
            raise IndexError(f"Indice hors limites : {index}")
        courant = self.tete
        for _ in range(index):
            courant = courant.suivant
        return courant.donnee

    # ── Utilitaires ─────────────────────────────────────

    def inverser(self):
        """Inverser la liste en place — O(n)."""
        precedent = None
        courant   = self.tete
        self.queue = self.tete
        while courant:
            suivant          = courant.suivant
            courant.suivant  = precedent
            precedent        = courant
            courant          = suivant
        self.tete = precedent

    def vers_liste(self):
        """Convertir en liste Python — O(n)."""
        result = []
        courant = self.tete
        while courant:
            result.append(courant.donnee)
            courant = courant.suivant
        return result

    def __repr__(self):
        noeuds = self.vers_liste()
        return " → ".join(str(n) for n in noeuds) + " → None"

    def detecter_cycle(self):
        """Algorithme de Floyd (lièvre et tortue) — O(n)."""
        lent = rapide = self.tete
        while rapide and rapide.suivant:
            lent   = lent.suivant
            rapide = rapide.suivant.suivant
            if lent is rapide:
                return True
        return False

    def milieu(self):
        """Trouver le nœud du milieu — O(n)."""
        lent = rapide = self.tete
        while rapide and rapide.suivant:
            lent   = lent.suivant
            rapide = rapide.suivant.suivant
        return lent.donnee if lent else None


# ── Tests ──────────────────────────────────────────────────

lc = ListeChainee()
for val in [1, 2, 3, 4, 5]:
    lc.inserer_queue(val)
print("Initiale :", lc)          # 1 → 2 → 3 → 4 → 5 → None

lc.inserer_tete(0)
print("Tête 0   :", lc)          # 0 → 1 → 2 → 3 → 4 → 5 → None

lc.inserer_position(99, 3)
print("Pos 3=99 :", lc)

lc.supprimer_valeur(99)
print("Del 99   :", lc)

lc.inverser()
print("Inversée :", lc)          # 5 → 4 → 3 → 2 → 1 → 0 → None

print("Milieu   :", lc.milieu()) # 2 (pour 6 éléments → index 3, valeur 2)
print("Len      :", len(lc))     # 6


# ──────────────────────────────────────────────────────────
# 2. Liste doublement chaînée (Doubly Linked List)
# ──────────────────────────────────────────────────────────

class NoeudDouble:
    def __init__(self, donnee):
        self.donnee   = donnee
        self.suivant  = None
        self.precedent = None

    def __repr__(self):
        return f"ND({self.donnee})"


class ListeDoublement:
    """
    Liste doublement chaînée.
    Avantage sur la liste simple : suppression en O(1) si on a le nœud.
    """

    def __init__(self):
        # Utiliser des sentinelles (gardes) pour simplifier le code
        self.tete = NoeudDouble(None)   # sentinelle tête
        self.queue = NoeudDouble(None)  # sentinelle queue
        self.tete.suivant  = self.queue
        self.queue.precedent = self.tete
        self._taille = 0

    def _inserer_entre(self, precedent, suivant, donnee):
        """Insérer un nœud entre precedent et suivant — O(1)."""
        nouveau = NoeudDouble(donnee)
        nouveau.precedent = precedent
        nouveau.suivant   = suivant
        precedent.suivant = nouveau
        suivant.precedent = nouveau
        self._taille += 1
        return nouveau

    def _supprimer_noeud(self, noeud):
        """Supprimer un nœud donné — O(1)."""
        noeud.precedent.suivant = noeud.suivant
        noeud.suivant.precedent = noeud.precedent
        self._taille -= 1
        return noeud.donnee

    def inserer_tete(self, donnee):
        return self._inserer_entre(self.tete, self.tete.suivant, donnee)

    def inserer_queue(self, donnee):
        return self._inserer_entre(self.queue.precedent, self.queue, donnee)

    def supprimer_tete(self):
        if self._taille == 0:
            raise IndexError("Liste vide")
        return self._supprimer_noeud(self.tete.suivant)

    def supprimer_queue(self):
        if self._taille == 0:
            raise IndexError("Liste vide")
        return self._supprimer_noeud(self.queue.precedent)

    def vers_liste(self):
        result = []
        courant = self.tete.suivant
        while courant is not self.queue:
            result.append(courant.donnee)
            courant = courant.suivant
        return result

    def vers_liste_inverse(self):
        result = []
        courant = self.queue.precedent
        while courant is not self.tete:
            result.append(courant.donnee)
            courant = courant.precedent
        return result

    def __len__(self):
        return self._taille

    def __repr__(self):
        return " ⟺ ".join(str(x) for x in self.vers_liste())


ld = ListeDoublement()
for val in [1, 2, 3, 4, 5]:
    ld.inserer_queue(val)
print("DLL      :", ld)
print("Inversée :", ld.vers_liste_inverse())
ld.supprimer_tete()
ld.supprimer_queue()
print("Après    :", ld)


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Fusionner deux listes chaînées triées
def fusionner_triees(l1: ListeChainee, l2: ListeChainee) -> ListeChainee:
    """Fusionner deux listes triées en une liste triée."""
    resultat = ListeChainee()
    c1, c2 = l1.tete, l2.tete
    while c1 and c2:
        if c1.donnee <= c2.donnee:
            resultat.inserer_queue(c1.donnee); c1 = c1.suivant
        else:
            resultat.inserer_queue(c2.donnee); c2 = c2.suivant
    courant = c1 or c2
    while courant:
        resultat.inserer_queue(courant.donnee)
        courant = courant.suivant
    return resultat

l1 = ListeChainee()
l2 = ListeChainee()
for v in [1, 3, 5, 7]: l1.inserer_queue(v)
for v in [2, 4, 6, 8]: l2.inserer_queue(v)
print("Fusion :", fusionner_triees(l1, l2))

# Ex 2 : Vérifier si une liste chaînée est un palindrome
def est_palindrome(lc: ListeChainee) -> bool:
    lst = lc.vers_liste()
    return lst == lst[::-1]

lc_pal = ListeChainee()
for v in [1, 2, 3, 2, 1]: lc_pal.inserer_queue(v)
print("Palindrome :", est_palindrome(lc_pal))  # True

# Ex 3 : Supprimer les doublons d'une liste non triée
def supprimer_doublons(lc: ListeChainee):
    vus = set()
    courant = lc.tete
    precedent = None
    while courant:
        if courant.donnee in vus:
            precedent.suivant = courant.suivant
            if courant == lc.queue:
                lc.queue = precedent
            lc._taille -= 1
        else:
            vus.add(courant.donnee)
            precedent = courant
        courant = courant.suivant
    return lc

lc_dup = ListeChainee()
for v in [1, 2, 3, 2, 4, 3, 5]: lc_dup.inserer_queue(v)
print("Sans doublons :", supprimer_doublons(lc_dup))
