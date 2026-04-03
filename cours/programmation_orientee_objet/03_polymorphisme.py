# ============================================================
# 03 — Polymorphisme
# Classes abstraites, duck typing, protocoles
# ============================================================

from abc import ABC, abstractmethod
import math

# ──────────────────────────────────────────────────────────
# 1. Classes abstraites (ABC)
# ──────────────────────────────────────────────────────────
#
# Une classe abstraite ne peut pas être instanciée directement.
# Elle définit un contrat que les sous-classes doivent respecter.

class Forme(ABC):
    """Classe abstraite — définit le contrat des formes géométriques."""

    @abstractmethod
    def aire(self) -> float:
        """Calculer l'aire de la forme."""

    @abstractmethod
    def perimetre(self) -> float:
        """Calculer le périmètre de la forme."""

    # Méthode concrète — partagée par toutes les sous-classes
    def description(self) -> str:
        return (f"{type(self).__name__} : "
                f"aire={self.aire():.2f}, périmètre={self.perimetre():.2f}")

    # Propriété abstraite
    @property
    @abstractmethod
    def couleur(self) -> str:
        pass


class Cercle(Forme):
    def __init__(self, rayon, couleur="rouge"):
        self.rayon = rayon
        self._couleur = couleur

    def aire(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon

    @property
    def couleur(self):
        return self._couleur


class Rectangle(Forme):
    def __init__(self, l, h, couleur="bleu"):
        self.l = l
        self.h = h
        self._couleur = couleur

    def aire(self):
        return self.l * self.h

    def perimetre(self):
        return 2 * (self.l + self.h)

    @property
    def couleur(self):
        return self._couleur


class Triangle(Forme):
    def __init__(self, a, b, c, couleur="vert"):
        self.a, self.b, self.c = a, b, c
        self._couleur = couleur

    def aire(self):
        s = self.perimetre() / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def perimetre(self):
        return self.a + self.b + self.c

    @property
    def couleur(self):
        return self._couleur


# Essai d'instanciation d'une classe abstraite
try:
    f = Forme()
except TypeError as e:
    print(f"Erreur attendue : {e}")

# Polymorphisme en action
formes = [Cercle(5), Rectangle(4, 6), Triangle(3, 4, 5)]

for forme in formes:
    print(forme.description())

# Tri par aire — même interface, comportements différents
formes.sort(key=lambda f: f.aire())
for f in formes:
    print(f"  {type(f).__name__} : {f.aire():.2f}")

# Vérification d'instance abstraite
print(isinstance(Cercle(3), Forme))  # True


# ──────────────────────────────────────────────────────────
# 2. Duck Typing
# ──────────────────────────────────────────────────────────
#
# "If it walks like a duck and quacks like a duck, it's a duck."
# Python ne vérifie pas le type, seulement les méthodes disponibles.

class Canard:
    def parler(self):
        return "Coin coin !"

    def marcher(self):
        return "*marche comme un canard*"


class Personne:
    def parler(self):
        return "Bonjour !"

    def marcher(self):
        return "*marche normalement*"


class Robot:
    def parler(self):
        return "Bip boop."

    def marcher(self):
        return "*roule*"


def faire_faire(entite):
    """Peu importe le type — on appelle juste les méthodes."""
    print(entite.parler())
    print(entite.marcher())

for entite in [Canard(), Personne(), Robot()]:
    print(f"--- {type(entite).__name__} ---")
    faire_faire(entite)


# ──────────────────────────────────────────────────────────
# 3. Protocoles (typing.Protocol) — typage structurel
# ──────────────────────────────────────────────────────────
#
# Introduit en Python 3.8, Protocol permet le duck typing statique.
# Pas besoin d'héritage explicite — si la classe a les bonnes méthodes,
# elle satisfait le protocole.

from typing import Protocol, runtime_checkable

@runtime_checkable
class Dessinable(Protocol):
    """Tout objet qui implémente draw() est Dessinable."""
    def draw(self) -> str: ...

@runtime_checkable
class Redimensionnable(Protocol):
    """Tout objet qui implémente resize() est Redimensionnable."""
    def resize(self, facteur: float) -> None: ...


class FormeUI:
    def draw(self) -> str:
        return f"Dessin de {type(self).__name__}"

    def resize(self, facteur: float) -> None:
        print(f"Redimensionnement × {facteur}")


class Icone:
    """N'hérite de rien mais satisfait les protocoles."""
    def draw(self) -> str:
        return "Icône dessinée"

    def resize(self, facteur: float) -> None:
        print(f"Icône redimensionnée × {facteur}")


def afficher(elem: Dessinable):
    print(elem.draw())

afficher(FormeUI())
afficher(Icone())  # fonctionne sans héritage !

# Vérification runtime
print(isinstance(Icone(), Dessinable))       # True
print(isinstance(Icone(), Redimensionnable)) # True
print(isinstance("texte", Dessinable))       # False


# ──────────────────────────────────────────────────────────
# 4. Polymorphisme paramétrique avec génériques
# ──────────────────────────────────────────────────────────

from typing import TypeVar, Generic, List

T = TypeVar("T")

class Pile(Generic[T]):
    """Pile générique — fonctionne avec n'importe quel type."""

    def __init__(self):
        self._data: List[T] = []

    def empiler(self, item: T) -> None:
        self._data.append(item)

    def depiler(self) -> T:
        if not self._data:
            raise IndexError("Pile vide")
        return self._data.pop()

    def sommet(self) -> T:
        return self._data[-1]

    def __len__(self) -> int:
        return len(self._data)


# Pile d'entiers
pile_int: Pile[int] = Pile()
pile_int.empiler(1)
pile_int.empiler(2)
print(pile_int.depiler())  # 2

# Pile de chaînes
pile_str: Pile[str] = Pile()
pile_str.empiler("a")
pile_str.empiler("b")
print(pile_str.depiler())  # b


# ──────────────────────────────────────────────────────────
# 5. Polymorphisme ad-hoc : surcharge d'opérateurs
# ──────────────────────────────────────────────────────────

class Matrice:
    """Matrice 2×2 avec opérateurs surchargés."""

    def __init__(self, a, b, c, d):
        self._m = [[a, b], [c, d]]

    def __add__(self, autre):
        return Matrice(
            self._m[0][0] + autre._m[0][0],
            self._m[0][1] + autre._m[0][1],
            self._m[1][0] + autre._m[1][0],
            self._m[1][1] + autre._m[1][1],
        )

    def __mul__(self, autre):
        if isinstance(autre, (int, float)):
            return Matrice(
                self._m[0][0] * autre, self._m[0][1] * autre,
                self._m[1][0] * autre, self._m[1][1] * autre,
            )
        # Produit matriciel
        a = self._m; b = autre._m
        return Matrice(
            a[0][0]*b[0][0] + a[0][1]*b[1][0],
            a[0][0]*b[0][1] + a[0][1]*b[1][1],
            a[1][0]*b[0][0] + a[1][1]*b[1][0],
            a[1][0]*b[0][1] + a[1][1]*b[1][1],
        )

    def __eq__(self, autre):
        return self._m == autre._m

    def __repr__(self):
        return (f"[{self._m[0][0]}, {self._m[0][1]}]\n"
                f"[{self._m[1][0]}, {self._m[1][1]}]")


M1 = Matrice(1, 2, 3, 4)
M2 = Matrice(5, 6, 7, 8)
print("M1 + M2 =\n", M1 + M2)
print("M1 × 2 =\n", M1 * 2)
print("M1 × M2 =\n", M1 * M2)


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Système de paiement polymorphe
class ModePaiement(ABC):
    @abstractmethod
    def payer(self, montant: float) -> str: ...

    @abstractmethod
    def valider(self) -> bool: ...


class CarteBancaire(ModePaiement):
    def __init__(self, numero, cvv):
        self.numero = numero
        self.cvv = cvv

    def payer(self, montant):
        return f"Paiement de {montant}€ par carte {self.numero[-4:]}"

    def valider(self):
        return len(self.numero) == 16 and len(str(self.cvv)) == 3


class PayPal(ModePaiement):
    def __init__(self, email):
        self.email = email

    def payer(self, montant):
        return f"Paiement de {montant}€ via PayPal ({self.email})"

    def valider(self):
        return "@" in self.email


class Crypto(ModePaiement):
    def __init__(self, adresse, devise="BTC"):
        self.adresse = adresse
        self.devise = devise

    def payer(self, montant):
        return f"Paiement de {montant}€ en {self.devise}"

    def valider(self):
        return len(self.adresse) >= 26


def traiter_paiement(mode: ModePaiement, montant: float):
    if not mode.valider():
        print(f"Mode de paiement invalide : {type(mode).__name__}")
        return
    print(mode.payer(montant))


modes = [
    CarteBancaire("1234567890123456", 123),
    PayPal("user@example.com"),
    Crypto("1A2B3C4D5E6F7G8H9I0J1K2L3M4N5O"),
]

for mode in modes:
    traiter_paiement(mode, 99.99)

# Ex 2 : Itérateur polymorphe
class CompteurAscendant:
    def __init__(self, debut, fin):
        self.courant = debut
        self.fin = fin

    def __iter__(self): return self
    def __next__(self):
        if self.courant > self.fin:
            raise StopIteration
        val = self.courant
        self.courant += 1
        return val

class CompteurDescendant:
    def __init__(self, debut, fin):
        self.courant = debut
        self.fin = fin

    def __iter__(self): return self
    def __next__(self):
        if self.courant < self.fin:
            raise StopIteration
        val = self.courant
        self.courant -= 1
        return val

for compteur in [CompteurAscendant(1, 5), CompteurDescendant(5, 1)]:
    print(list(compteur))
