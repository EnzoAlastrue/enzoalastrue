# ============================================================
# 01 — Classes & Objets
# Attributs, méthodes, méthodes spéciales, propriétés
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. Définir une classe
# ──────────────────────────────────────────────────────────

class Etudiant:
    """Représente un étudiant."""

    # Attribut de classe (partagé par toutes les instances)
    etablissement = "Université Paris"
    _nb_etudiants = 0  # compteur privé de classe

    def __init__(self, nom, prenom, age):
        """Constructeur — appelé à la création de l'objet."""
        # Attributs d'instance (propres à chaque objet)
        self.nom    = nom
        self.prenom = prenom
        self.age    = age
        self._notes = []  # attribut "privé" par convention

        Etudiant._nb_etudiants += 1

    # ── Méthodes d'instance ────────────────────────────

    def ajouter_note(self, note):
        """Ajouter une note (entre 0 et 20)."""
        if not 0 <= note <= 20:
            raise ValueError(f"Note invalide : {note}")
        self._notes.append(note)

    def moyenne(self):
        """Calculer la moyenne des notes."""
        if not self._notes:
            return 0.0
        return sum(self._notes) / len(self._notes)

    def mention(self):
        moy = self.moyenne()
        if moy >= 16:   return "Très bien"
        if moy >= 14:   return "Bien"
        if moy >= 12:   return "Assez bien"
        if moy >= 10:   return "Passable"
        return "Insuffisant"

    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

    # ── Méthodes de classe ─────────────────────────────

    @classmethod
    def nb_etudiants(cls):
        """Accéder/modifier des attributs de classe."""
        return cls._nb_etudiants

    @classmethod
    def depuis_chaine(cls, chaine):
        """Factory method : Etudiant.depuis_chaine('Dupont,Alice,21')."""
        parts = chaine.split(",")
        return cls(parts[0], parts[1], int(parts[2]))

    # ── Méthodes statiques ─────────────────────────────

    @staticmethod
    def valider_note(note):
        """Pas besoin de self ni de cls."""
        return isinstance(note, (int, float)) and 0 <= note <= 20

    # ── Méthodes spéciales (Dunder) ────────────────────

    def __str__(self):
        """str(obj) et print(obj) — représentation lisible."""
        return f"{self.nom_complet()} ({self.age} ans) — moy: {self.moyenne():.1f}"

    def __repr__(self):
        """repr(obj) — représentation non ambiguë pour les développeurs."""
        return f"Etudiant({self.nom!r}, {self.prenom!r}, {self.age})"

    def __len__(self):
        """len(obj) — nombre de notes."""
        return len(self._notes)

    def __bool__(self):
        """bool(obj) — True si au moins une note."""
        return len(self._notes) > 0

    def __eq__(self, autre):
        """obj1 == obj2."""
        if not isinstance(autre, Etudiant):
            return NotImplemented
        return self.nom == autre.nom and self.prenom == autre.prenom

    def __lt__(self, autre):
        """obj1 < obj2 — pour le tri."""
        return self.moyenne() < autre.moyenne()

    def __hash__(self):
        """Nécessaire si __eq__ est défini (pour dict/set)."""
        return hash((self.nom, self.prenom))

    def __contains__(self, note):
        """note in obj."""
        return note in self._notes

    def __iter__(self):
        """Rendre l'objet itérable."""
        return iter(self._notes)

    def __getitem__(self, index):
        """obj[index]."""
        return self._notes[index]


# Tests
e1 = Etudiant("Dupont", "Alice", 21)
e2 = Etudiant.depuis_chaine("Martin,Bob,22")

e1.ajouter_note(15)
e1.ajouter_note(17)
e1.ajouter_note(13)

print(e1)            # Alice Dupont (21 ans) — moy: 15.0
print(repr(e1))      # Etudiant('Dupont', 'Alice', 21)
print(len(e1))       # 3
print(bool(e1))      # True
print(e1.mention())  # Bien

print("Nombre d'étudiants :", Etudiant.nb_etudiants())  # 2
print("Établissement :", Etudiant.etablissement)

# Itération
for note in e1:
    print(note, end=" ")
print()

# Tri
e2.ajouter_note(10)
e2.ajouter_note(8)
etudiants = [e1, e2]
etudiants.sort(reverse=True)
print([str(e) for e in etudiants])


# ──────────────────────────────────────────────────────────
# 2. Propriétés (properties)
# ──────────────────────────────────────────────────────────

class Temperature:
    """Démo des propriétés getter/setter/deleter."""

    def __init__(self, celsius=0):
        self._celsius = celsius  # stockage interne

    @property
    def celsius(self):
        """Getter."""
        return self._celsius

    @celsius.setter
    def celsius(self, valeur):
        """Setter avec validation."""
        if valeur < -273.15:
            raise ValueError("En dessous du zéro absolu !")
        self._celsius = valeur

    @celsius.deleter
    def celsius(self):
        """Deleter."""
        del self._celsius

    @property
    def fahrenheit(self):
        """Propriété calculée (pas de setter)."""
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, valeur):
        self.celsius = (valeur - 32) * 5 / 9

    @property
    def kelvin(self):
        return self._celsius + 273.15

    def __repr__(self):
        return f"{self._celsius}°C"


t = Temperature(100)
print(t.celsius)     # 100
print(t.fahrenheit)  # 212.0
print(t.kelvin)      # 373.15

t.fahrenheit = 32
print(t.celsius)     # 0.0

try:
    t.celsius = -300
except ValueError as e:
    print(e)


# ──────────────────────────────────────────────────────────
# 3. Méthodes spéciales arithmétiques
# ──────────────────────────────────────────────────────────

class Vecteur:
    """Vecteur 2D avec opérateurs surchargés."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, autre):       # self + autre
        return Vecteur(self.x + autre.x, self.y + autre.y)

    def __sub__(self, autre):       # self - autre
        return Vecteur(self.x - autre.x, self.y - autre.y)

    def __mul__(self, scalaire):    # self * n
        return Vecteur(self.x * scalaire, self.y * scalaire)

    def __rmul__(self, scalaire):   # n * self
        return self.__mul__(scalaire)

    def __neg__(self):              # -self
        return Vecteur(-self.x, -self.y)

    def __abs__(self):              # abs(self)
        return (self.x**2 + self.y**2) ** 0.5

    def __iadd__(self, autre):      # self += autre
        self.x += autre.x
        self.y += autre.y
        return self

    def __repr__(self):
        return f"Vecteur({self.x}, {self.y})"

    def __eq__(self, autre):
        return self.x == autre.x and self.y == autre.y


v1 = Vecteur(1, 2)
v2 = Vecteur(3, 4)

print(v1 + v2)     # Vecteur(4, 6)
print(v1 - v2)     # Vecteur(-2, -2)
print(v1 * 3)      # Vecteur(3, 6)
print(3 * v1)      # Vecteur(3, 6)
print(-v1)         # Vecteur(-1, -2)
print(abs(v2))     # 5.0


# ──────────────────────────────────────────────────────────
# 4. Gestionnaires de contexte
# ──────────────────────────────────────────────────────────

class ConnexionDB:
    """Simuler une connexion à une base de données."""

    def __init__(self, url):
        self.url = url
        self._connecte = False

    def __enter__(self):
        """Appelé lors de l'entrée dans le bloc with."""
        print(f"Connexion à {self.url}")
        self._connecte = True
        return self  # valeur accessible via 'as'

    def __exit__(self, type_exc, val_exc, tb):
        """Appelé lors de la sortie du bloc with (même si exception)."""
        print("Fermeture de la connexion")
        self._connecte = False
        return False  # ne pas supprimer l'exception

    def executer(self, requete):
        if not self._connecte:
            raise RuntimeError("Non connecté")
        print(f"  SQL: {requete}")

with ConnexionDB("localhost:5432/madb") as db:
    db.executer("SELECT * FROM etudiants")
    db.executer("INSERT INTO etudiants VALUES (...)")


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Classe Fraction avec opérateurs
from math import gcd

class Fraction:
    def __init__(self, num, den=1):
        if den == 0:
            raise ZeroDivisionError("Dénominateur nul")
        if den < 0:
            num, den = -num, -den
        pgcd = gcd(abs(num), den)
        self.num = num // pgcd
        self.den = den // pgcd

    def __add__(self, autre):
        return Fraction(self.num * autre.den + autre.num * self.den,
                        self.den * autre.den)

    def __mul__(self, autre):
        return Fraction(self.num * autre.num, self.den * autre.den)

    def __eq__(self, autre):
        return self.num == autre.num and self.den == autre.den

    def __repr__(self):
        return f"{self.num}/{self.den}" if self.den != 1 else str(self.num)

    def __float__(self):
        return self.num / self.den

a = Fraction(1, 2)
b = Fraction(1, 3)
print(a + b)     # 5/6
print(a * b)     # 1/6
print(float(a))  # 0.5

# Ex 2 : Classe Pile avec méthodes spéciales
class PileSpeciale:
    def __init__(self):
        self._data = []

    def __len__(self):       return len(self._data)
    def __bool__(self):      return bool(self._data)
    def __iter__(self):      return iter(reversed(self._data))
    def __contains__(self, v): return v in self._data
    def __repr__(self):      return f"Pile({self._data})"

    def push(self, v):       self._data.append(v)
    def pop(self):           return self._data.pop()
    def peek(self):          return self._data[-1]

p = PileSpeciale()
p.push(1); p.push(2); p.push(3)
print(list(p))   # [3, 2, 1]
print(2 in p)    # True
print(len(p))    # 3
