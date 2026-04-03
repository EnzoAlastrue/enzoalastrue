# ============================================================
# 02 — Héritage
# Héritage simple, multiple, MRO, super()
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. Héritage simple
# ──────────────────────────────────────────────────────────

class Animal:
    """Classe de base (parent)."""

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def se_nourrir(self):
        return f"{self.nom} mange."

    def dormir(self):
        return f"{self.nom} dort."

    def se_presenter(self):
        return f"Je suis {self.nom}, j'ai {self.age} an(s)."

    def __str__(self):
        return f"{type(self).__name__}({self.nom}, {self.age} ans)"

    def __repr__(self):
        return self.__str__()


class Chien(Animal):
    """Classe dérivée (enfant)."""

    def __init__(self, nom, age, race):
        super().__init__(nom, age)   # appel du constructeur parent
        self.race = race

    def aboyer(self):
        return f"{self.nom} aboie : Wouaf !"

    def se_presenter(self):          # surcharge (override)
        base = super().se_presenter()  # réutiliser la méthode parent
        return f"{base} Je suis un {self.race}."

    def __str__(self):
        return f"Chien({self.nom}, {self.race})"


class Chat(Animal):
    def __init__(self, nom, age, couleur="noir"):
        super().__init__(nom, age)
        self.couleur = couleur

    def ronronner(self):
        return f"{self.nom} ronronne..."

    def se_presenter(self):
        return f"{super().se_presenter()} Je suis un chat {self.couleur}."


# Tests
chien = Chien("Rex", 3, "Labrador")
chat  = Chat("Whiskers", 5, "roux")

print(chien.se_presenter())       # Méthode surchargée
print(chien.se_nourrir())         # Méthode héritée
print(chien.aboyer())             # Méthode propre

print(chat.se_presenter())
print(chat.ronronner())

# isinstance / issubclass
print(isinstance(chien, Chien))   # True
print(isinstance(chien, Animal))  # True (héritage)
print(isinstance(chien, Chat))    # False

print(issubclass(Chien, Animal))  # True
print(issubclass(Chat, Animal))   # True
print(issubclass(Animal, object)) # True — tout hérite d'object


# ──────────────────────────────────────────────────────────
# 2. Polymorphisme via l'héritage
# ──────────────────────────────────────────────────────────

class Forme:
    """Classe abstraite de base."""
    def aire(self):
        raise NotImplementedError("Doit être implémentée par la sous-classe")

    def perimetre(self):
        raise NotImplementedError

    def description(self):
        return (f"{type(self).__name__} : aire={self.aire():.2f}, "
                f"périmètre={self.perimetre():.2f}")


import math

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)


class Triangle(Forme):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def aire(self):
        s = self.perimetre() / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))

    def perimetre(self):
        return self.a + self.b + self.c


# Polymorphisme : même interface, comportements différents
formes = [Cercle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for forme in formes:
    print(forme.description())

# Aire totale — même code, peu importe le type
total = sum(f.aire() for f in formes)
print(f"Aire totale : {total:.2f}")


# ──────────────────────────────────────────────────────────
# 3. Héritage multiple
# ──────────────────────────────────────────────────────────

class Volant:
    def voler(self):
        return f"{self.__class__.__name__} vole."

    def altitude(self):
        return "altitude : 1000m"


class Nageur:
    def nager(self):
        return f"{self.__class__.__name__} nage."

    def profondeur(self):
        return "profondeur : 10m"


class Canard(Animal, Volant, Nageur):
    """Un canard vole ET nage — héritage multiple."""

    def __init__(self, nom, age):
        Animal.__init__(self, nom, age)  # ou super().__init__(nom, age)

    def coin_coin(self):
        return f"{self.nom} : Coin coin !"


donald = Canard("Donald", 2)
print(donald.se_presenter())
print(donald.voler())
print(donald.nager())
print(donald.coin_coin())


# ──────────────────────────────────────────────────────────
# 4. MRO — Method Resolution Order
# ──────────────────────────────────────────────────────────
#
# Python utilise l'algorithme C3 Linearization pour résoudre
# l'ordre de résolution des méthodes en cas d'héritage multiple.

print(Canard.__mro__)
# (Canard, Animal, Volant, Nageur, object)

# MRO lisible
for cls in Canard.__mro__:
    print(cls.__name__)

# Exemple classique du diamant
class A:
    def methode(self):
        print("A.methode")

class B(A):
    def methode(self):
        print("B.methode")
        super().methode()  # important : super() suit le MRO

class C(A):
    def methode(self):
        print("C.methode")
        super().methode()

class D(B, C):
    def methode(self):
        print("D.methode")
        super().methode()

# MRO : D → B → C → A
print(D.__mro__)
d = D()
d.methode()
# D.methode → B.methode → C.methode → A.methode
# (chaque classe appelle super() → C3 garantit qu'A n'est appelé qu'une fois)


# ──────────────────────────────────────────────────────────
# 5. Mixins — pattern de composition via héritage
# ──────────────────────────────────────────────────────────
#
# Un Mixin est une classe qui fournit des fonctionnalités
# sans être une classe de base autonome.

class JsonMixin:
    """Ajouter la sérialisation JSON à n'importe quelle classe."""
    import json as _json

    def vers_json(self):
        import json
        return json.dumps(self.__dict__, default=str, ensure_ascii=False)

    @classmethod
    def depuis_json(cls, json_str):
        import json
        data = json.loads(json_str)
        obj = cls.__new__(cls)
        obj.__dict__.update(data)
        return obj


class LogMixin:
    """Ajouter du logging à n'importe quelle classe."""

    def log(self, message):
        print(f"[{type(self).__name__}] {message}")


class ValidateurMixin:
    """Validation des attributs."""

    def valider(self):
        for attr, valeur in self.__dict__.items():
            if valeur is None:
                raise ValueError(f"Attribut manquant : {attr}")
        return True


class Produit(JsonMixin, LogMixin, ValidateurMixin):
    def __init__(self, nom, prix, stock):
        self.nom   = nom
        self.prix  = prix
        self.stock = stock

    def acheter(self, quantite):
        self.log(f"Achat de {quantite} × {self.nom}")
        if quantite > self.stock:
            raise ValueError("Stock insuffisant")
        self.stock -= quantite


p = Produit("Clavier", 49.99, 100)
print(p.vers_json())
p.acheter(5)
print(p.valider())


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Hiérarchie de comptes bancaires
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self._solde = solde
        self._historique = []

    @property
    def solde(self):
        return self._solde

    def deposer(self, montant):
        self._solde += montant
        self._historique.append(f"+{montant}")
        return self

    def retirer(self, montant):
        if montant > self._solde:
            raise ValueError("Solde insuffisant")
        self._solde -= montant
        self._historique.append(f"-{montant}")
        return self

    def __str__(self):
        return f"{self.titulaire} : {self._solde}€"


class CompteEpargne(CompteBancaire):
    TAUX_INTERET = 0.02

    def __init__(self, titulaire, solde=0):
        super().__init__(titulaire, solde)

    def appliquer_interets(self):
        interets = self._solde * self.TAUX_INTERET
        self.deposer(interets)
        return interets

    def retirer(self, montant):
        if montant > self._solde * 0.8:  # max 80% du solde
            raise ValueError("Retraits limités à 80% du solde")
        return super().retirer(montant)


class CompteCredit(CompteBancaire):
    def __init__(self, titulaire, limite=1000):
        super().__init__(titulaire, 0)
        self.limite = limite

    def retirer(self, montant):
        if self._solde - montant < -self.limite:
            raise ValueError(f"Limite de crédit atteinte : {self.limite}€")
        self._solde -= montant
        self._historique.append(f"-{montant}")
        return self


cb = CompteBancaire("Alice", 1000)
ce = CompteEpargne("Bob", 5000)
cc = CompteCredit("Charlie", 2000)

cb.deposer(500).retirer(200)
ce.appliquer_interets()
cc.retirer(1500)

comptes = [cb, ce, cc]
for c in comptes:
    print(c)
