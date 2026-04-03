# ============================================================
# 04 — Encapsulation
# Propriétés, attributs privés, descripteurs, slots
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. Niveaux d'accès en Python
# ──────────────────────────────────────────────────────────
#
# Python n'a pas de vrais modificateurs d'accès (public/private).
# La convention est :
#
#   nom       → public   : accessible partout
#   _nom      → protégé  : "privé par convention" (accessible mais déconseillé)
#   __nom     → privé    : name mangling → _Classe__nom (vraiment difficile d'accès)

class Exemple:
    def __init__(self):
        self.public     = "public"
        self._protege   = "protégé"
        self.__prive    = "privé"

    def acceder_prive(self):
        return self.__prive  # accessible depuis la classe

e = Exemple()
print(e.public)           # public
print(e._protege)         # protégé (accessible mais déconseillé)
# print(e.__prive)        # AttributeError !
print(e._Exemple__prive)  # privé (name mangling — accès possible mais pas recommandé)
print(e.acceder_prive())  # privé


# ──────────────────────────────────────────────────────────
# 2. Propriétés (property) — encapsulation élégante
# ──────────────────────────────────────────────────────────

class CompteBancaire:
    """Compte avec solde encapsulé et validé."""

    FRAIS_RETRAIT = 0.01  # 1% de frais

    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self._solde    = 0
        self._historique = []
        # Utiliser le setter pour la validation initiale
        self.solde = solde_initial

    @property
    def solde(self):
        """Getter — accès en lecture."""
        return self._solde

    @solde.setter
    def solde(self, montant):
        """Setter — validation à l'écriture."""
        if not isinstance(montant, (int, float)):
            raise TypeError("Le solde doit être un nombre")
        if montant < 0:
            raise ValueError("Le solde ne peut pas être négatif")
        self._solde = round(float(montant), 2)

    @property
    def historique(self):
        """Retourner une copie pour protéger la liste interne."""
        return self._historique.copy()

    @property
    def solde_apres_frais(self):
        """Propriété calculée (read-only)."""
        return self._solde * (1 - self.FRAIS_RETRAIT)

    def deposer(self, montant):
        if montant <= 0:
            raise ValueError("Le dépôt doit être positif")
        self._solde += montant
        self._historique.append(f"+{montant:.2f}€")
        return self

    def retirer(self, montant):
        if montant <= 0:
            raise ValueError("Le retrait doit être positif")
        if montant > self._solde:
            raise ValueError("Solde insuffisant")
        self._solde -= montant
        self._historique.append(f"-{montant:.2f}€")
        return self

    def __repr__(self):
        return f"Compte({self.titulaire!r}, solde={self._solde:.2f}€)"


compte = CompteBancaire("Alice", 1000)
compte.deposer(500).retirer(200)
print(compte)
print("Solde :", compte.solde)
print("Historique :", compte.historique)

try:
    compte.solde = -100
except ValueError as e:
    print(f"Erreur : {e}")


# ──────────────────────────────────────────────────────────
# 3. Descripteurs
# ──────────────────────────────────────────────────────────
#
# Un descripteur est un objet qui définit __get__, __set__, __delete__.
# C'est le mécanisme qui alimente property, classmethod, staticmethod.

class PositifValidateur:
    """Descripteur : valide que la valeur est positive."""

    def __set_name__(self, owner, name):
        self.nom_public  = name
        self.nom_prive   = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self  # accès depuis la classe
        return getattr(obj, self.nom_prive, None)

    def __set__(self, obj, valeur):
        if not isinstance(valeur, (int, float)):
            raise TypeError(f"{self.nom_public} doit être un nombre")
        if valeur < 0:
            raise ValueError(f"{self.nom_public} doit être positif")
        setattr(obj, self.nom_prive, valeur)

    def __delete__(self, obj):
        delattr(obj, self.nom_prive)


class TypeValidateur:
    """Descripteur : valide le type."""

    def __init__(self, *types):
        self.types = types

    def __set_name__(self, owner, name):
        self.nom_public = name
        self.nom_prive  = "_" + name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.nom_prive, None)

    def __set__(self, obj, valeur):
        if not isinstance(valeur, self.types):
            raise TypeError(
                f"{self.nom_public} doit être {self.types}, reçu {type(valeur)}"
            )
        setattr(obj, self.nom_prive, valeur)


class Produit:
    """Utilise des descripteurs pour valider les attributs."""

    nom   = TypeValidateur(str)
    prix  = PositifValidateur()
    stock = PositifValidateur()

    def __init__(self, nom, prix, stock):
        self.nom   = nom
        self.prix  = prix
        self.stock = stock

    def __repr__(self):
        return f"Produit({self.nom!r}, prix={self.prix}€, stock={self.stock})"


p = Produit("Clavier", 49.99, 100)
print(p)

try:
    p.prix = -10
except ValueError as e:
    print(f"Erreur : {e}")

try:
    p.nom = 42
except TypeError as e:
    print(f"Erreur : {e}")


# ──────────────────────────────────────────────────────────
# 4. __slots__ — optimisation mémoire
# ──────────────────────────────────────────────────────────
#
# Par défaut, chaque instance Python a un dictionnaire __dict__.
# __slots__ remplace ce dict par un tableau fixe → moins de mémoire.
# Utile pour des classes avec des millions d'instances.

class PointAvecDict:
    """Point normal — utilise __dict__."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointAvecSlots:
    """Point avec __slots__ — plus léger en mémoire."""
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

import sys

pd = PointAvecDict(1, 2)
ps = PointAvecSlots(1, 2)

print(f"Avec dict  : {sys.getsizeof(pd.__dict__)} bytes (__dict__)")
print(f"Avec slots : pas de __dict__")
print(f"pd size    : {sys.getsizeof(pd)} bytes")
print(f"ps size    : {sys.getsizeof(ps)} bytes")

# On peut toujours ajouter des attributs à pd
pd.z = 3
# ps.z = 3  # AttributeError !

# Comparaison sur 1 000 000 d'instances
import tracemalloc

tracemalloc.start()
points_dict = [PointAvecDict(i, i) for i in range(100_000)]
mem_dict, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
points_slots = [PointAvecSlots(i, i) for i in range(100_000)]
mem_slots, _ = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Dict  : {mem_dict / 1_000_000:.2f} MB")
print(f"Slots : {mem_slots / 1_000_000:.2f} MB")
print(f"Ratio : {mem_dict / mem_slots:.1f}×")


# ──────────────────────────────────────────────────────────
# 5. Classe immuable avec __setattr__
# ──────────────────────────────────────────────────────────

class Immuable:
    """Classe dont les attributs ne peuvent pas être modifiés après init."""

    _init_fait = False

    def __init__(self, **kwargs):
        for cle, val in kwargs.items():
            object.__setattr__(self, cle, val)  # bypass notre __setattr__
        object.__setattr__(self, "_init_fait", True)

    def __setattr__(self, nom, valeur):
        if self._init_fait:
            raise AttributeError(
                f"Objet immuable — impossible de modifier '{nom}'"
            )
        object.__setattr__(self, nom, valeur)

    def __delattr__(self, nom):
        raise AttributeError("Objet immuable — impossible de supprimer un attribut")

    def __repr__(self):
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return f"{type(self).__name__}({attrs})"


point = Immuable(x=3, y=4)
print(point)  # Immuable({'x': 3, 'y': 4})

try:
    point.x = 10
except AttributeError as e:
    print(f"Erreur : {e}")

# dataclass frozen=True — alternative moderne
from dataclasses import dataclass

@dataclass(frozen=True)
class PointGele:
    x: float
    y: float

    def distance(self):
        return (self.x**2 + self.y**2) ** 0.5

pg = PointGele(3, 4)
print(pg.distance())  # 5.0
try:
    pg.x = 10
except Exception as e:
    print(f"Erreur : {e}")


# ──────────────────────────────────────────────────────────
# 6. dataclasses — encapsulation moderne
# ──────────────────────────────────────────────────────────

from dataclasses import dataclass, field
from typing import List

@dataclass
class Etudiant:
    nom:    str
    prenom: str
    age:    int
    notes:  List[float] = field(default_factory=list)

    def __post_init__(self):
        """Validation après __init__ automatique."""
        if self.age < 0 or self.age > 120:
            raise ValueError(f"Âge invalide : {self.age}")
        if not self.nom:
            raise ValueError("Le nom ne peut pas être vide")
        self.nom = self.nom.strip().upper()

    @property
    def moyenne(self):
        return sum(self.notes) / len(self.notes) if self.notes else 0.0

    def ajouter_note(self, note):
        if not 0 <= note <= 20:
            raise ValueError(f"Note invalide : {note}")
        self.notes.append(note)


e = Etudiant("dupont", "Alice", 21)
e.ajouter_note(15)
e.ajouter_note(17)
print(e)
print(f"Moyenne : {e.moyenne:.1f}")


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Descripteur de plage (RangeValidator)
class PlageValidateur:
    def __init__(self, mini, maxi):
        self.mini = mini
        self.maxi = maxi

    def __set_name__(self, owner, name):
        self.nom_public = name
        self.nom_prive  = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.nom_prive, None) if obj else self

    def __set__(self, obj, val):
        if not (self.mini <= val <= self.maxi):
            raise ValueError(
                f"{self.nom_public} doit être entre {self.mini} et {self.maxi}, reçu {val}"
            )
        setattr(obj, self.nom_prive, val)


class Angle:
    degres = PlageValidateur(0, 360)

    def __init__(self, degres):
        self.degres = degres

    def __repr__(self):
        return f"Angle({self.degres}°)"

a = Angle(90)
print(a)
try:
    a.degres = 400
except ValueError as e:
    print(e)

# Ex 2 : Observable — notifier lors des changements
class Observateur(Protocol if False else object):
    def mise_a_jour(self, nom, ancienne, nouvelle): ...

class AttributObservable:
    """Descripteur qui notifie les observateurs lors d'un changement."""

    def __set_name__(self, owner, name):
        self.nom_public = name
        self.nom_prive  = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.nom_prive, None) if obj else self

    def __set__(self, obj, val):
        ancienne = getattr(obj, self.nom_prive, None)
        setattr(obj, self.nom_prive, val)
        if ancienne != val and hasattr(obj, "_observateurs"):
            for obs in obj._observateurs:
                obs(self.nom_public, ancienne, val)


class Config:
    debug   = AttributObservable()
    timeout = AttributObservable()

    def __init__(self, debug=False, timeout=30):
        self._observateurs = []
        self.debug   = debug
        self.timeout = timeout

    def ajouter_observateur(self, fn):
        self._observateurs.append(fn)


def logger(nom, avant, apres):
    print(f"Config.{nom} : {avant!r} → {apres!r}")

cfg = Config()
cfg.ajouter_observateur(logger)
cfg.debug = True
cfg.timeout = 60
