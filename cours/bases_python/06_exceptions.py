# ============================================================
# 06 — Exceptions
# try/except, finally, raise, exceptions personnalisées
# ============================================================

# ──────────────────────────────────────────────────────────
# 1. Hiérarchie des exceptions Python
# ──────────────────────────────────────────────────────────

# BaseException
#  ├── SystemExit
#  ├── KeyboardInterrupt
#  └── Exception
#       ├── ArithmeticError
#       │    ├── ZeroDivisionError
#       │    └── OverflowError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── ValueError
#       ├── TypeError
#       ├── AttributeError
#       ├── NameError
#       ├── IOError / OSError
#       │    └── FileNotFoundError
#       ├── RuntimeError
#       │    └── RecursionError
#       └── StopIteration


# ──────────────────────────────────────────────────────────
# 2. try / except / else / finally
# ──────────────────────────────────────────────────────────

def diviser(a, b):
    try:
        resultat = a / b          # peut lever ZeroDivisionError
    except ZeroDivisionError:
        print("Erreur : division par zéro !")
        return None
    else:
        # exécuté uniquement si aucune exception
        print(f"{a} / {b} = {resultat}")
        return resultat
    finally:
        # toujours exécuté, même si return ou exception
        print("Calcul terminé.")

diviser(10, 2)
diviser(10, 0)

# Capturer plusieurs types d'exceptions
def convertir(valeur):
    try:
        return int(valeur)
    except (ValueError, TypeError) as e:
        print(f"Conversion impossible : {e}")
        return None

# Capturer toutes les exceptions (à éviter si possible)
try:
    x = int("abc")
except Exception as e:
    print(f"Exception : {type(e).__name__}: {e}")

# Accéder à l'objet exception
try:
    liste = [1, 2, 3]
    print(liste[10])
except IndexError as e:
    print(f"IndexError : {e}")
    print(f"args : {e.args}")

# Gérer plusieurs blocs except
def lire_entier(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Veuillez entrer un entier valide.")
        except EOFError:
            print("Fin de saisie inattendue.")
            return 0


# ──────────────────────────────────────────────────────────
# 3. raise — lever une exception
# ──────────────────────────────────────────────────────────

def racine_carree(n):
    if n < 0:
        raise ValueError(f"Impossible de calculer √{n} (valeur négative)")
    return n ** 0.5

try:
    print(racine_carree(16))   # 4.0
    print(racine_carree(-4))   # lève ValueError
except ValueError as e:
    print(e)

# Re-lever (re-raise)
def traiter(donnees):
    try:
        return 100 / donnees["valeur"]
    except ZeroDivisionError:
        print("Log : division par zéro détectée")
        raise           # re-lève l'exception originale
    except KeyError as e:
        raise ValueError(f"Clé manquante : {e}") from e  # chaînage d'exceptions

# assert — vérification d'invariants (désactivé avec python -O)
def factorielle(n):
    assert n >= 0, f"n doit être positif, reçu {n}"
    if n == 0:
        return 1
    return n * factorielle(n - 1)


# ──────────────────────────────────────────────────────────
# 4. Exceptions personnalisées
# ──────────────────────────────────────────────────────────

# Convention : hériter de Exception, nommer en PascalCase + "Error"

class ErreurAge(ValueError):
    """Levée quand un âge est hors des limites acceptables."""
    def __init__(self, age, minimum=0, maximum=150):
        self.age = age
        self.minimum = minimum
        self.maximum = maximum
        super().__init__(
            f"Âge invalide : {age} (attendu entre {minimum} et {maximum})"
        )

class ErreurSoldeInsuffisant(Exception):
    """Levée lors d'un retrait supérieur au solde."""
    def __init__(self, solde, montant):
        self.solde = solde
        self.montant = montant
        self.manque = montant - solde
        super().__init__(
            f"Solde insuffisant : {solde}€ disponible, {montant}€ demandé "
            f"(manque {self.manque}€)"
        )

# Hiérarchie d'exceptions métier
class ErreurApplication(Exception):
    """Classe de base pour les erreurs de l'application."""

class ErreurValidation(ErreurApplication):
    """Erreur de validation des données."""

class ErreurBase(ErreurApplication):
    """Erreur d'accès à la base de données."""

class ErreurConnexion(ErreurBase):
    """Erreur de connexion à la base."""


# Utilisation
class CompteBancaire:
    def __init__(self, titulaire, solde_initial=0):
        self.titulaire = titulaire
        self._solde = solde_initial

    @property
    def solde(self):
        return self._solde

    def deposer(self, montant):
        if montant <= 0:
            raise ErreurValidation(f"Montant invalide : {montant}")
        self._solde += montant
        return self._solde

    def retirer(self, montant):
        if montant <= 0:
            raise ErreurValidation(f"Montant invalide : {montant}")
        if montant > self._solde:
            raise ErreurSoldeInsuffisant(self._solde, montant)
        self._solde -= montant
        return self._solde

compte = CompteBancaire("Enzo", 100)
try:
    compte.deposer(50)
    compte.retirer(200)
except ErreurSoldeInsuffisant as e:
    print(e)
    print(f"Il manque {e.manque}€")
except ErreurValidation as e:
    print(f"Validation : {e}")


# ──────────────────────────────────────────────────────────
# 5. Gestionnaires de contexte (context managers)
# ──────────────────────────────────────────────────────────

# with garantit que __exit__ est appelé même en cas d'exception
class GestionnaireFichier:
    def __init__(self, nom, mode="r"):
        self.nom = nom
        self.mode = mode
        self.fichier = None

    def __enter__(self):
        self.fichier = open(self.nom, self.mode, encoding="utf-8")
        print(f"Ouverture de {self.nom}")
        return self.fichier

    def __exit__(self, type_exc, valeur_exc, traceback):
        self.fichier.close()
        print(f"Fermeture de {self.nom}")
        # retourner True supprime l'exception, False la propage
        return False

# Avec contextlib
from contextlib import contextmanager

@contextmanager
def chrono(label="Opération"):
    import time
    debut = time.perf_counter()
    try:
        yield
    finally:
        fin = time.perf_counter()
        print(f"{label} : {fin - debut:.4f}s")

with chrono("Calcul"):
    total = sum(range(1_000_000))
print(total)

@contextmanager
def transaction(base):
    """Simule une transaction : commit si succès, rollback sinon."""
    print("BEGIN TRANSACTION")
    try:
        yield base
        print("COMMIT")
    except Exception as e:
        print(f"ROLLBACK (cause : {e})")
        raise


# ──────────────────────────────────────────────────────────
# 6. Bonnes pratiques
# ──────────────────────────────────────────────────────────

# ✅ Capturer le type d'exception le plus précis possible
# ✅ Ne pas capturer Exception silencieusement sans log
# ✅ Utiliser finally pour libérer les ressources
# ✅ Créer des exceptions métier explicites
# ❌ Éviter except: (sans type) — capture même KeyboardInterrupt
# ❌ Éviter de passer silencieusement sur une exception

# Mauvais :
try:
    x = 1 / 0
except:       # trop large
    pass      # silencieux — perte d'information

# Bon :
try:
    x = 1 / 0
except ZeroDivisionError:
    x = float("inf")
    print("Division par zéro, résultat mis à l'infini")


# ──────────────────────────────────────────────────────────
# Exercices
# ──────────────────────────────────────────────────────────

# Ex 1 : Saisie sécurisée d'un entier dans un intervalle
def saisir_entier(min_val, max_val, prompt="Entrer un entier : "):
    while True:
        try:
            n = int(input(prompt))
            if not (min_val <= n <= max_val):
                raise ValueError(f"Doit être entre {min_val} et {max_val}")
            return n
        except ValueError as e:
            print(f"Invalide : {e}")

# Ex 2 : Calculatrice sécurisée
def calculer(a, op, b):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    if op not in operations:
        raise ValueError(f"Opération inconnue : '{op}'")
    if op == "/" and b == 0:
        raise ZeroDivisionError("Division par zéro")
    return operations[op](a, b)

for test in [(10, "+", 5), (10, "/", 0), (10, "^", 2)]:
    try:
        print(f"{test[0]} {test[1]} {test[2]} = {calculer(*test)}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Erreur : {e}")

# Ex 3 : Décorateur de gestion d'erreurs avec retry
import time

def retry(max_tentatives=3, delai=1, exceptions=(Exception,)):
    def decorateur(fonction):
        def wrapper(*args, **kwargs):
            for tentative in range(1, max_tentatives + 1):
                try:
                    return fonction(*args, **kwargs)
                except exceptions as e:
                    print(f"Tentative {tentative}/{max_tentatives} échouée : {e}")
                    if tentative < max_tentatives:
                        time.sleep(delai)
            raise RuntimeError(f"Échec après {max_tentatives} tentatives")
        return wrapper
    return decorateur

@retry(max_tentatives=3, delai=0.1, exceptions=(ValueError,))
def operation_fragile(x):
    import random
    if random.random() < 0.7:
        raise ValueError("Erreur aléatoire")
    return x * 2
