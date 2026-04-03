# ============================================================
# 05 — Patrons de conception (Design Patterns)
# Singleton, Factory, Observer, Strategy
# ============================================================

# Les design patterns sont des solutions réutilisables à des
# problèmes récurrents de conception logicielle.
#
# Catégories :
#   - Créationnels : comment créer des objets
#   - Structurels  : comment organiser les classes
#   - Comportementaux : comment les objets communiquent

# ──────────────────────────────────────────────────────────
# 1. SINGLETON — un seul et unique exemplaire
# ──────────────────────────────────────────────────────────
#
# Garantit qu'une classe n'a qu'une seule instance.
# Utile pour : configuration, connexion DB, logger.

class Singleton:
    """Singleton via __new__."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, valeur=None):
        # Ne pas réinitialiser si déjà créé
        if not hasattr(self, "_initialise"):
            self.valeur = valeur
            self._initialise = True


# Vérification
s1 = Singleton(42)
s2 = Singleton(99)
print(s1 is s2)        # True
print(s1.valeur)       # 42 (pas 99 — s2 pointe vers s1)

# Singleton thread-safe avec metaclass
import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=SingletonMeta):
    """Configuration globale de l'application."""

    def __init__(self):
        self.debug   = False
        self.timeout = 30
        self.db_url  = "localhost:5432"

    def __repr__(self):
        return f"Config(debug={self.debug}, timeout={self.timeout})"


c1 = Config()
c2 = Config()
c1.debug = True
print(c2.debug)   # True — même instance
print(c1 is c2)   # True


# ──────────────────────────────────────────────────────────
# 2. FACTORY — déléguer la création d'objets
# ──────────────────────────────────────────────────────────
#
# Factory Method  : sous-classe décide quelle classe instancier
# Abstract Factory: famille de factories liées
# Simple Factory  : méthode statique qui crée des objets

# Simple Factory
class Animal:
    def __init__(self, nom): self.nom = nom
    def parler(self): raise NotImplementedError

class Chien(Animal):
    def parler(self): return f"{self.nom} : Wouaf !"

class Chat(Animal):
    def parler(self): return f"{self.nom} : Miaou !"

class Oiseau(Animal):
    def parler(self): return f"{self.nom} : Cui cui !"

class AnimalFactory:
    """Simple Factory."""
    _registry = {
        "chien":  Chien,
        "chat":   Chat,
        "oiseau": Oiseau,
    }

    @classmethod
    def creer(cls, espece: str, nom: str) -> Animal:
        classe = cls._registry.get(espece.lower())
        if not classe:
            raise ValueError(f"Espèce inconnue : {espece}")
        return classe(nom)

    @classmethod
    def enregistrer(cls, espece: str, classe):
        """Permettre d'ajouter de nouvelles espèces."""
        cls._registry[espece] = classe


for espece, nom in [("chien", "Rex"), ("chat", "Felix"), ("oiseau", "Tweety")]:
    animal = AnimalFactory.creer(espece, nom)
    print(animal.parler())

# Factory Method via héritage
from abc import ABC, abstractmethod

class Serialiseur(ABC):
    """Factory Method : sous-classe décide du format."""

    def sauvegarder(self, donnees, chemin):
        serialise = self.serialiser(donnees)
        with open(chemin, "w", encoding="utf-8") as f:
            f.write(serialise)
        return chemin

    @abstractmethod
    def serialiser(self, donnees) -> str:
        """Factory Method."""

class SerialiseurJSON(Serialiseur):
    def serialiser(self, donnees):
        import json
        return json.dumps(donnees, indent=2, ensure_ascii=False)

class SerialiseurCSV(Serialiseur):
    def serialiser(self, donnees):
        import csv, io
        if not donnees or not isinstance(donnees[0], dict):
            return ""
        output = io.StringIO()
        writer = csv.DictWriter(output, fieldnames=donnees[0].keys())
        writer.writeheader()
        writer.writerows(donnees)
        return output.getvalue()


# ──────────────────────────────────────────────────────────
# 3. OBSERVER — notifier les abonnés des changements
# ──────────────────────────────────────────────────────────
#
# Découple le sujet (émetteur) de ses observateurs (receveurs).
# Utile pour : événements UI, systèmes de notification, MVC.

class Evenement:
    """Gestionnaire d'événements simple (publish-subscribe)."""

    def __init__(self):
        self._abonnes = []

    def abonner(self, callback):
        self._abonnes.append(callback)
        return lambda: self._abonnes.remove(callback)  # désabonnement

    def emettre(self, *args, **kwargs):
        for abonne in self._abonnes:
            abonne(*args, **kwargs)


class StockProduit:
    """Sujet observable — notifie quand le stock change."""

    def __init__(self, nom, quantite):
        self.nom = nom
        self._quantite = quantite
        # Événements
        self.sur_rupture  = Evenement()
        self.sur_reappro  = Evenement()
        self.sur_modif    = Evenement()

    @property
    def quantite(self):
        return self._quantite

    @quantite.setter
    def quantite(self, val):
        ancienne = self._quantite
        self._quantite = val
        self.sur_modif.emettre(self.nom, ancienne, val)
        if val == 0:
            self.sur_rupture.emettre(self.nom)
        if ancienne == 0 and val > 0:
            self.sur_reappro.emettre(self.nom, val)

    def __repr__(self):
        return f"Produit({self.nom}, stock={self._quantite})"


def logger_stock(nom, avant, apres):
    print(f"[LOG] {nom} : {avant} → {apres}")

def alerter_rupture(nom):
    print(f"[ALERTE] Rupture de stock : {nom} !")

def alerter_reappro(nom, quantite):
    print(f"[INFO] Réapprovisionnement : {nom} (+{quantite})")


clavier = StockProduit("Clavier", 10)
clavier.sur_modif.abonner(logger_stock)
clavier.sur_rupture.abonner(alerter_rupture)
clavier.sur_reappro.abonner(alerter_reappro)

clavier.quantite = 5
clavier.quantite = 0
clavier.quantite = 20


# Observer classique avec ABC
class Observateur(ABC):
    @abstractmethod
    def mise_a_jour(self, sujet, **donnees): ...

class Sujet:
    def __init__(self):
        self._observateurs = []

    def attacher(self, obs: Observateur):
        self._observateurs.append(obs)

    def detacher(self, obs: Observateur):
        self._observateurs.remove(obs)

    def notifier(self, **donnees):
        for obs in self._observateurs:
            obs.mise_a_jour(self, **donnees)


class Meteo(Sujet):
    def __init__(self):
        super().__init__()
        self._temperature = 0
        self._humidite = 0

    def mesurer(self, temp, humidite):
        self._temperature = temp
        self._humidite = humidite
        self.notifier(temperature=temp, humidite=humidite)


class AffichageActuel(Observateur):
    def mise_a_jour(self, sujet, **d):
        print(f"[Affichage] T={d['temperature']}°C, H={d['humidite']}%")

class AlerteChaleur(Observateur):
    def mise_a_jour(self, sujet, **d):
        if d['temperature'] > 35:
            print(f"[ALERTE CHALEUR] {d['temperature']}°C !")

meteo = Meteo()
meteo.attacher(AffichageActuel())
meteo.attacher(AlerteChaleur())
meteo.mesurer(22, 65)
meteo.mesurer(38, 80)


# ──────────────────────────────────────────────────────────
# 4. STRATEGY — changer l'algorithme à la volée
# ──────────────────────────────────────────────────────────
#
# Encapsule une famille d'algorithmes interchangeables.
# Utile pour : tris, paiements, compressions, calcul de taxes.

class StrategieTri(ABC):
    @abstractmethod
    def trier(self, lst: list) -> list: ...

class TriRapide(StrategieTri):
    def trier(self, lst):
        import random
        if len(lst) <= 1: return lst
        pivot = random.choice(lst)
        return (self.trier([x for x in lst if x < pivot]) +
                [x for x in lst if x == pivot] +
                self.trier([x for x in lst if x > pivot]))

class TriFusion(StrategieTri):
    def trier(self, lst):
        if len(lst) <= 1: return lst
        m = len(lst) // 2
        g, d = self.trier(lst[:m]), self.trier(lst[m:])
        return self._fusionner(g, d)

    def _fusionner(self, g, d):
        r, i, j = [], 0, 0
        while i < len(g) and j < len(d):
            if g[i] <= d[j]: r.append(g[i]); i += 1
            else:             r.append(d[j]); j += 1
        return r + g[i:] + d[j:]

class TriPython(StrategieTri):
    def trier(self, lst):
        return sorted(lst)


class Trieur:
    """Contexte — utilise une stratégie de tri."""

    def __init__(self, strategie: StrategieTri = None):
        self._strategie = strategie or TriPython()

    def changer_strategie(self, strategie: StrategieTri):
        self._strategie = strategie

    def trier(self, lst):
        return self._strategie.trier(lst)


trieur = Trieur()
data = [5, 3, 8, 1, 9, 2, 7, 4, 6]

for strat in [TriPython(), TriRapide(), TriFusion()]:
    trieur.changer_strategie(strat)
    print(f"{type(strat).__name__:15}: {trieur.trier(data)}")

# Strategy avec lambda (version fonctionnelle)
def trier_avec(lst, strategie):
    return strategie(lst)

print(trier_avec(data, sorted))
print(trier_avec(data, lambda l: sorted(l, reverse=True)))


# ──────────────────────────────────────────────────────────
# 5. DECORATOR pattern (à ne pas confondre avec @decorator)
# ──────────────────────────────────────────────────────────
#
# Ajouter dynamiquement des comportements à un objet.

class Boisson(ABC):
    @abstractmethod
    def description(self) -> str: ...

    @abstractmethod
    def prix(self) -> float: ...

class Cafe(Boisson):
    def description(self): return "Café"
    def prix(self): return 1.50

class The(Boisson):
    def description(self): return "Thé"
    def prix(self): return 1.20

class DecorBoisson(Boisson):
    """Décorateur de base."""
    def __init__(self, boisson: Boisson):
        self._boisson = boisson

    def description(self): return self._boisson.description()
    def prix(self):        return self._boisson.prix()

class Lait(DecorBoisson):
    def description(self): return self._boisson.description() + " + Lait"
    def prix(self):        return self._boisson.prix() + 0.30

class Sucre(DecorBoisson):
    def description(self): return self._boisson.description() + " + Sucre"
    def prix(self):        return self._boisson.prix() + 0.10

class Vanille(DecorBoisson):
    def description(self): return self._boisson.description() + " + Vanille"
    def prix(self):        return self._boisson.prix() + 0.50

# Composer les décorateurs
boisson = Vanille(Lait(Sucre(Cafe())))
print(f"{boisson.description()} : {boisson.prix():.2f}€")
# Café + Sucre + Lait + Vanille : 2.40€


# ──────────────────────────────────────────────────────────
# 6. COMMAND — encapsuler une action
# ──────────────────────────────────────────────────────────

class Commande(ABC):
    @abstractmethod
    def executer(self): ...

    @abstractmethod
    def annuler(self): ...


class CommandeDeposer(Commande):
    def __init__(self, compte, montant):
        self.compte = compte
        self.montant = montant

    def executer(self):
        self.compte._solde += self.montant
        print(f"Dépôt de {self.montant}€")

    def annuler(self):
        self.compte._solde -= self.montant
        print(f"Annulation dépôt de {self.montant}€")


class GestionnaireCommandes:
    """Invoke — exécute et mémorise les commandes pour undo/redo."""

    def __init__(self):
        self._historique = []
        self._annulees   = []

    def executer(self, commande: Commande):
        commande.executer()
        self._historique.append(commande)
        self._annulees.clear()

    def annuler(self):
        if not self._historique:
            print("Rien à annuler")
            return
        cmd = self._historique.pop()
        cmd.annuler()
        self._annulees.append(cmd)

    def refaire(self):
        if not self._annulees:
            print("Rien à refaire")
            return
        cmd = self._annulees.pop()
        cmd.executer()
        self._historique.append(cmd)


class Compte:
    def __init__(self, solde=0):
        self._solde = solde
    def __repr__(self):
        return f"Compte(solde={self._solde}€)"

c = Compte(100)
gc = GestionnaireCommandes()

gc.executer(CommandeDeposer(c, 50))
gc.executer(CommandeDeposer(c, 30))
print(c)         # 180€
gc.annuler()
print(c)         # 150€
gc.refaire()
print(c)         # 180€


# ──────────────────────────────────────────────────────────
# Résumé des patterns
# ──────────────────────────────────────────────────────────
#
# Créationnels :
#   Singleton    — une seule instance
#   Factory      — déléguer la création
#   Builder      — construire étape par étape
#   Prototype    — cloner un objet
#
# Structurels :
#   Decorator    — ajouter des comportements dynamiquement
#   Adapter      — adapter une interface incompatible
#   Facade       — simplifier une interface complexe
#   Composite    — traiter objets et groupes uniformément
#
# Comportementaux :
#   Observer     — notifier les abonnés
#   Strategy     — algorithmes interchangeables
#   Command      — encapsuler une action (undo/redo)
#   Template     — squelette d'algorithme avec étapes variables
#   Iterator     — parcourir sans exposer la structure interne
