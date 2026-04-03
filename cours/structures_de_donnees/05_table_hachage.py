# ============================================================
# 05 — Table de hachage (Hash Table)
# Chaining (chaînage) & Open Addressing (adressage ouvert)
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. Concepts fondamentaux
# ──────────────────────────────────────────────────────────

# Une table de hachage mappe des clés à des valeurs via une fonction de hachage.
#
# Complexités (cas moyen avec un bon facteur de charge) :
#   insertion   O(1) amorti
#   recherche   O(1) amorti
#   suppression O(1) amorti
#   Pire cas    O(n) si toutes les clés collisionnent
#
# Facteur de charge : α = n / m  (n = éléments, m = taille du tableau)
# Idéal : α ≤ 0.75 (Java) ou ≤ 0.66 (Python)


# ──────────────────────────────────────────────────────────
# 2. Fonctions de hachage
# ──────────────────────────────────────────────────────────

def hash_simple(cle, taille):
    """Hachage simple par modulo."""
    return hash(cle) % taille

def hash_polynomial(chaine, taille, base=31):
    """Hachage polynomial pour les chaînes."""
    h = 0
    for char in chaine:
        h = (h * base + ord(char)) % taille
    return h

def hash_double(cle, taille, i):
    """Double hachage pour l'adressage ouvert."""
    h1 = hash(cle) % taille
    h2 = 1 + (hash(cle) % (taille - 1))
    return (h1 + i * h2) % taille

# Python utilise SipHash-1-3 pour les str (protection contre les DoS)
print(hash("Python"))
print(hash(42))
print(hash(3.14))
print(hash((1, 2, 3)))   # tuple hashable
# print(hash([1, 2]))    # TypeError : liste non hashable


# ──────────────────────────────────────────────────────────
# 3. Table de hachage avec chaînage (Separate Chaining)
# ──────────────────────────────────────────────────────────

class NoeudChaine:
    def __init__(self, cle, valeur):
        self.cle = cle
        self.valeur = valeur
        self.suivant = None

class TableHachageChainage:
    """
    Résolution des collisions par chaînage.
    Chaque case du tableau contient une liste chaînée.
    Facteur de charge : redimensionnement si > 0.75
    """

    CAPACITE_INITIALE = 8
    SEUIL_MAX = 0.75   # redimensionner si α > seuil
    SEUIL_MIN = 0.25   # réduire si α < seuil (optionnel)

    def __init__(self):
        self._capacite  = self.CAPACITE_INITIALE
        self._tableau   = [None] * self._capacite
        self._taille    = 0

    def _indice(self, cle):
        return hash(cle) % self._capacite

    def _facteur_charge(self):
        return self._taille / self._capacite

    # ── Insertion ───────────────────────────────────────

    def inserer(self, cle, valeur):
        if self._facteur_charge() >= self.SEUIL_MAX:
            self._redimensionner(self._capacite * 2)
        idx = self._indice(cle)
        noeud = self._tableau[idx]
        # Chercher si la clé existe déjà
        while noeud:
            if noeud.cle == cle:
                noeud.valeur = valeur
                return
            noeud = noeud.suivant
        # Ajouter en tête de la chaîne
        nouveau = NoeudChaine(cle, valeur)
        nouveau.suivant = self._tableau[idx]
        self._tableau[idx] = nouveau
        self._taille += 1

    # ── Recherche ───────────────────────────────────────

    def obtenir(self, cle, defaut=None):
        idx = self._indice(cle)
        noeud = self._tableau[idx]
        while noeud:
            if noeud.cle == cle:
                return noeud.valeur
            noeud = noeud.suivant
        return defaut

    def contient(self, cle):
        return self.obtenir(cle) is not None

    # ── Suppression ─────────────────────────────────────

    def supprimer(self, cle):
        idx = self._indice(cle)
        noeud = self._tableau[idx]
        precedent = None
        while noeud:
            if noeud.cle == cle:
                if precedent:
                    precedent.suivant = noeud.suivant
                else:
                    self._tableau[idx] = noeud.suivant
                self._taille -= 1
                return noeud.valeur
            precedent = noeud
            noeud = noeud.suivant
        raise KeyError(cle)

    # ── Redimensionnement ───────────────────────────────

    def _redimensionner(self, nouvelle_capacite):
        ancienne = self._tableau
        self._capacite = nouvelle_capacite
        self._tableau  = [None] * self._capacite
        self._taille   = 0
        for noeud in ancienne:
            while noeud:
                self.inserer(noeud.cle, noeud.valeur)
                noeud = noeud.suivant

    # ── Interface dict-like ─────────────────────────────

    def __setitem__(self, cle, valeur):
        self.inserer(cle, valeur)

    def __getitem__(self, cle):
        val = self.obtenir(cle)
        if val is None and not self.contient(cle):
            raise KeyError(cle)
        return val

    def __delitem__(self, cle):
        self.supprimer(cle)

    def __contains__(self, cle):
        return self.contient(cle)

    def __len__(self):
        return self._taille

    def items(self):
        for noeud in self._tableau:
            while noeud:
                yield noeud.cle, noeud.valeur
                noeud = noeud.suivant

    def keys(self):
        return [k for k, _ in self.items()]

    def values(self):
        return [v for _, v in self.items()]

    def __repr__(self):
        paires = ", ".join(f"{k!r}: {v!r}" for k, v in self.items())
        return "{" + paires + "}"


# Tests
th = TableHachageChainage()
th["nom"] = "Enzo"
th["age"] = 21
th["ville"] = "Paris"
th["langage"] = "Python"

print("Table :", th)
print("nom   :", th["nom"])
print("len   :", len(th))
print("α     :", th._facteur_charge())

del th["ville"]
print("Après del :", th)

for k, v in th.items():
    print(f"  {k} → {v}")


# ──────────────────────────────────────────────────────────
# 4. Table de hachage avec adressage ouvert (Open Addressing)
# ──────────────────────────────────────────────────────────

class TableHachageOuverte:
    """
    Résolution des collisions par sondage linéaire.
    Toutes les entrées dans le même tableau (pas de listes).
    """

    _VIDE    = object()  # sentinelle : case jamais utilisée
    _SUPPRIME = object() # sentinelle : case supprimée ("tombstone")

    def __init__(self, capacite=8):
        self._capacite = capacite
        self._cles    = [self._VIDE] * capacite
        self._valeurs = [None] * capacite
        self._taille  = 0

    def _sonder(self, cle):
        """Sondage linéaire : chercher la position de la clé."""
        h = hash(cle) % self._capacite
        for i in range(self._capacite):
            idx = (h + i) % self._capacite
            if self._cles[idx] is self._VIDE:
                return idx, False          # case vide → clé absente
            if self._cles[idx] is not self._SUPPRIME and self._cles[idx] == cle:
                return idx, True           # clé trouvée
        return -1, False                   # tableau plein

    def inserer(self, cle, valeur):
        if self._taille / self._capacite >= 0.6:
            self._redimensionner(self._capacite * 2)
        h = hash(cle) % self._capacite
        premiere_tombe = None
        for i in range(self._capacite):
            idx = (h + i) % self._capacite
            if self._cles[idx] is self._VIDE:
                pos = premiere_tombe if premiere_tombe is not None else idx
                self._cles[pos] = cle
                self._valeurs[pos] = valeur
                self._taille += 1
                return
            if self._cles[idx] is self._SUPPRIME:
                if premiere_tombe is None:
                    premiere_tombe = idx
            elif self._cles[idx] == cle:
                self._valeurs[idx] = valeur
                return

    def obtenir(self, cle, defaut=None):
        h = hash(cle) % self._capacite
        for i in range(self._capacite):
            idx = (h + i) % self._capacite
            if self._cles[idx] is self._VIDE:
                return defaut
            if self._cles[idx] is not self._SUPPRIME and self._cles[idx] == cle:
                return self._valeurs[idx]
        return defaut

    def supprimer(self, cle):
        h = hash(cle) % self._capacite
        for i in range(self._capacite):
            idx = (h + i) % self._capacite
            if self._cles[idx] is self._VIDE:
                raise KeyError(cle)
            if self._cles[idx] is not self._SUPPRIME and self._cles[idx] == cle:
                val = self._valeurs[idx]
                self._cles[idx] = self._SUPPRIME
                self._valeurs[idx] = None
                self._taille -= 1
                return val
        raise KeyError(cle)

    def _redimensionner(self, nouvelle_capacite):
        anciens_cles    = self._cles
        anciens_valeurs = self._valeurs
        self._capacite  = nouvelle_capacite
        self._cles      = [self._VIDE] * nouvelle_capacite
        self._valeurs   = [None] * nouvelle_capacite
        self._taille    = 0
        for cle, val in zip(anciens_cles, anciens_valeurs):
            if cle is not self._VIDE and cle is not self._SUPPRIME:
                self.inserer(cle, val)

    def __setitem__(self, cle, valeur): self.inserer(cle, valeur)
    def __getitem__(self, cle):
        v = self.obtenir(cle)
        if v is None and self.obtenir(cle, "...") == "...":
            raise KeyError(cle)
        return v
    def __len__(self): return self._taille

tho = TableHachageOuverte()
tho["a"] = 1
tho["b"] = 2
tho["c"] = 3
print("Ouvert :", [(k, v) for k, v in zip(tho._cles, tho._valeurs)
                   if k is not tho._VIDE and k is not tho._SUPPRIME])


# ──────────────────────────────────────────────────────────
# 5. dict Python — implémentation interne
# ──────────────────────────────────────────────────────────

# Python utilise Open Addressing avec :
# - Sondage pseudo-aléatoire (pas linéaire)
# - Redimensionnement à 2/3 de facteur de charge
# - Compact en mémoire depuis Python 3.6
# - Ordonnées par ordre d'insertion depuis Python 3.7

d = {}
d["x"] = 10
print(d.get("y", 0))    # 0 (défaut)
print("x" in d)         # True

# setdefault — insérer si absent, retourner la valeur
d.setdefault("y", 42)
print(d["y"])            # 42

# defaultdict
from collections import defaultdict
graphe = defaultdict(list)
graphe["A"].append("B")
graphe["A"].append("C")
print(dict(graphe))      # {'A': ['B', 'C']}

# Counter
from collections import Counter
mots = "le chat est sur le tapis et le chat dort".split()
c = Counter(mots)
print(c.most_common(3))  # [('le', 3), ('chat', 2), ...]

# OrderedDict (utile pour LRU cache)
from collections import OrderedDict

class CacheLRU:
    """Cache LRU (Least Recently Used) avec OrderedDict."""
    def __init__(self, capacite):
        self._cache = OrderedDict()
        self._capacite = capacite

    def obtenir(self, cle):
        if cle not in self._cache:
            return -1
        self._cache.move_to_end(cle)  # marquer comme récemment utilisé
        return self._cache[cle]

    def inserer(self, cle, valeur):
        if cle in self._cache:
            self._cache.move_to_end(cle)
        self._cache[cle] = valeur
        if len(self._cache) > self._capacite:
            self._cache.popitem(last=False)  # supprimer le moins récent


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Anagrammes groupées
def grouper_anagrammes(mots):
    groupes = defaultdict(list)
    for mot in mots:
        cle = "".join(sorted(mot))
        groupes[cle].append(mot)
    return list(groupes.values())

print(grouper_anagrammes(["eat","tea","tan","ate","nat","bat"]))

# Ex 2 : Sous-tableau de somme nulle
def sous_tableau_somme_nulle(lst):
    """Trouver un sous-tableau de somme 0 — O(n)."""
    somme_prefixe = {0: -1}
    somme = 0
    for i, val in enumerate(lst):
        somme += val
        if somme in somme_prefixe:
            return somme_prefixe[somme] + 1, i
        somme_prefixe[somme] = i
    return None

print(sous_tableau_somme_nulle([3, 4, -7, 1, 3, 3, 1, -4]))  # (0, 2)

# Ex 3 : Plus longue sous-chaîne sans caractère répété
def plus_longue_sans_repetition(s):
    """Fenêtre glissante avec table de hachage — O(n)."""
    debut = longueur_max = 0
    derniere_pos = {}
    for fin, char in enumerate(s):
        if char in derniere_pos and derniere_pos[char] >= debut:
            debut = derniere_pos[char] + 1
        derniere_pos[char] = fin
        longueur_max = max(longueur_max, fin - debut + 1)
    return longueur_max

print(plus_longue_sans_repetition("abcabcbb"))  # 3
print(plus_longue_sans_repetition("pwwkew"))    # 3
print(plus_longue_sans_repetition("abcdef"))    # 6
