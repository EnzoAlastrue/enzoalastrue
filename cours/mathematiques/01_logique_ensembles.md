# 01 — Logique & Théorie des Ensembles
> Mathématiques L1 — Cours complet

---

## 1. Logique propositionnelle

Une **proposition** est un énoncé qui est soit vrai (V), soit faux (F) — jamais les deux.

> Exemples : « 2 + 2 = 4 » (V), « 7 est pair » (F), « il fait beau » (pas une proposition mathématique car subjective)

### 1.1 Connecteurs logiques

| Symbole | Nom | Lecture | Vrai quand... |
|---|---|---|---|
| ¬P | Négation | « non P » | P est faux |
| P ∧ Q | Conjonction | « P et Q » | P et Q sont tous les deux vrais |
| P ∨ Q | Disjonction | « P ou Q » | au moins l'un est vrai |
| P ⟹ Q | Implication | « si P alors Q » | P faux **ou** Q vrai |
| P ⟺ Q | Équivalence | « P si et seulement si Q » | P et Q ont la même valeur de vérité |

### 1.2 Tables de vérité

| P | Q | ¬P | P ∧ Q | P ∨ Q | P ⟹ Q | P ⟺ Q |
|---|---|---|---|---|---|---|
| V | V | F | V | V | V | V |
| V | F | F | F | V | F | F |
| F | V | V | F | V | V | F |
| F | F | V | F | F | V | V |

> **Attention** : P ⟹ Q est **faux** uniquement si P est vrai et Q est faux (« ex vero sequitur quodlibet »).

### 1.3 Tautologies et contradictions

- **Tautologie** : toujours vraie, quelle que soit la valeur des variables
  - Ex : P ∨ ¬P (tiers exclu)
- **Contradiction** : toujours fausse
  - Ex : P ∧ ¬P
- **Contingence** : ni tautologie ni contradiction

### 1.4 Lois logiques fondamentales

| Loi | Formule |
|---|---|
| Double négation | ¬(¬P) ⟺ P |
| De Morgan (ET) | ¬(P ∧ Q) ⟺ ¬P ∨ ¬Q |
| De Morgan (OU) | ¬(P ∨ Q) ⟺ ¬P ∧ ¬Q |
| Contraposée | (P ⟹ Q) ⟺ (¬Q ⟹ ¬P) |
| Absorption | P ∧ (P ∨ Q) ⟺ P |
| Distributivité | P ∧ (Q ∨ R) ⟺ (P ∧ Q) ∨ (P ∧ R) |

---

## 2. Quantificateurs

### 2.1 Quantificateur universel ∀

> ∀x ∈ E, P(x) : « Pour tout x appartenant à E, P(x) est vrai »

- **Nier** ∀x ∈ E, P(x) → ∃x ∈ E, ¬P(x)

### 2.2 Quantificateur existentiel ∃

> ∃x ∈ E, P(x) : « Il existe au moins un x dans E tel que P(x) est vrai »

- **Nier** ∃x ∈ E, P(x) → ∀x ∈ E, ¬P(x)

### 2.3 Exemples de négations

| Proposition | Négation |
|---|---|
| ∀n ∈ ℕ, n² ≥ 0 | ∃n ∈ ℕ, n² < 0 |
| ∃x ∈ ℝ, x² = 2 | ∀x ∈ ℝ, x² ≠ 2 |
| ∀ε > 0, ∃n₀ ∈ ℕ, \|aₙ − l\| < ε | ∃ε > 0, ∀n₀ ∈ ℕ, ∃n ≥ n₀, \|aₙ − l\| ≥ ε |

### 2.4 Raisonnements usuels

- **Raisonnement direct** : on suppose P et on en déduit Q pour prouver P ⟹ Q
- **Contraposée** : pour prouver P ⟹ Q, on prouve ¬Q ⟹ ¬P
- **Par l'absurde** : on suppose P ∧ ¬Q et on arrive à une contradiction
- **Par récurrence** : pour prouver ∀n ∈ ℕ, P(n) :
  1. **Initialisation** : vérifier P(0) (ou P(n₀))
  2. **Hérédité** : supposer P(n) vrai et montrer P(n+1)

---

## 3. Théorie des ensembles

### 3.1 Notions de base

- **Ensemble** : collection d'objets appelés *éléments*
- x ∈ A : « x appartient à A »
- x ∉ A : « x n'appartient pas à A »
- **Ensemble vide** ∅ : l'ensemble sans élément

### 3.2 Inclusions

| Notation | Signification |
|---|---|
| A ⊆ B | A est inclus dans B (tout élément de A est dans B) |
| A ⊊ B | A est strictement inclus dans B (A ⊆ B et A ≠ B) |
| A = B | A ⊆ B et B ⊆ A |

> **Méthode** : pour montrer A ⊆ B, on prend x ∈ A quelconque et on montre x ∈ B.

### 3.3 Opérations sur les ensembles

Soient A et B deux sous-ensembles d'un ensemble universel E.

| Opération | Notation | Définition |
|---|---|---|
| Réunion | A ∪ B | {x ∈ E \| x ∈ A **ou** x ∈ B} |
| Intersection | A ∩ B | {x ∈ E \| x ∈ A **et** x ∈ B} |
| Complémentaire | Aᶜ (ou Ā) | {x ∈ E \| x ∉ A} |
| Différence | A \ B | {x ∈ E \| x ∈ A **et** x ∉ B} |
| Différence symétrique | A △ B | (A \ B) ∪ (B \ A) |
| Produit cartésien | A × B | {(a, b) \| a ∈ A, b ∈ B} |

### 3.4 Propriétés des opérations

| Propriété | Formule |
|---|---|
| Commutativité | A ∪ B = B ∪ A ; A ∩ B = B ∩ A |
| Associativité | (A ∪ B) ∪ C = A ∪ (B ∪ C) |
| Distributivité | A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C) |
| De Morgan | (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ ; (A ∩ B)᷃ = Aᶜ ∪ Bᶜ |
| Absorption | A ∪ (A ∩ B) = A |
| Complémentaire | A ∪ Aᶜ = E ; A ∩ Aᶜ = ∅ |

### 3.5 Parties d'un ensemble — P(E)

L'ensemble de tous les sous-ensembles de E est noté **P(E)** (ou 2^E).

> Si E a n éléments, alors P(E) a **2ⁿ** éléments.

**Exemple** : E = {1, 2, 3} → P(E) = {∅, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}} → 2³ = 8 sous-ensembles.

---

## 4. Applications (Fonctions)

### 4.1 Définition

Une **application** f : E → F associe à chaque élément x ∈ E **exactement un** élément f(x) ∈ F.

- **E** : ensemble de départ (domaine)
- **F** : ensemble d'arrivée (codomaine)
- **f(x)** : image de x
- **Antécédent** de y : tout x tel que f(x) = y

### 4.2 Image et préimage

- **Image directe** : f(A) = {f(x) | x ∈ A} ⊆ F
- **Image réciproque** : f⁻¹(B) = {x ∈ E | f(x) ∈ B} ⊆ E
- **Image de f** : Im(f) = f(E) ⊆ F

### 4.3 Types d'applications

| Type | Définition | Condition |
|---|---|---|
| **Injective** (1-1) | x ≠ y ⟹ f(x) ≠ f(y) | ou : f(x) = f(y) ⟹ x = y |
| **Surjective** (sur) | ∀y ∈ F, ∃x ∈ E, f(x) = y | Im(f) = F |
| **Bijective** | injective **et** surjective | chaque y a exactement un antécédent |

> **Astuce** : Si E et F sont finis avec n et m éléments :
> - Injection possible ⟹ n ≤ m
> - Surjection possible ⟹ n ≥ m
> - Bijection possible ⟹ n = m

### 4.4 Composition et réciproque

- **Composition** : si f : E → F et g : F → G, alors g ∘ f : E → G, x ↦ g(f(x))
- **Application réciproque** : si f est bijective, f⁻¹ : F → E est l'unique application vérifiant f⁻¹ ∘ f = Id_E et f ∘ f⁻¹ = Id_F

---

## 5. Cardinalité

### 5.1 Ensembles finis

Si E est fini, |E| (ou Card(E)) désigne le nombre d'éléments.

| Formule | Signification |
|---|---|
| \|A ∪ B\| = \|A\| + \|B\| − \|A ∩ B\| | Principe d'inclusion-exclusion |
| \|A × B\| = \|A\| × \|B\| | Produit cartésien |
| \|P(A)\| = 2^{\|A\|} | Ensemble des parties |

### 5.2 Dénombrabilité

| Ensemble | Cardinal | Type |
|---|---|---|
| ℕ, ℤ, ℚ | ℵ₀ (aleph zéro) | Dénombrable infini |
| ℝ, [0,1], ℂ | 𝔠 (continu) | Non dénombrable |
| P(ℕ) | 𝔠 | Non dénombrable |

> **Théorème de Cantor** : Pour tout ensemble E, |E| < |P(E)|. Il n'existe pas de « plus grand » ensemble.

---

## 6. Relations

### 6.1 Relation binaire

Une **relation binaire** R sur E est un sous-ensemble de E × E.  
On note xRy pour (x, y) ∈ R.

### 6.2 Propriétés

| Propriété | Définition |
|---|---|
| **Réflexivité** | ∀x ∈ E, xRx |
| **Symétrie** | xRy ⟹ yRx |
| **Antisymétrie** | xRy et yRx ⟹ x = y |
| **Transitivité** | xRy et yRz ⟹ xRz |

### 6.3 Types de relations

- **Relation d'équivalence** : réflexive + symétrique + transitive
  - Crée des **classes d'équivalence** qui partitionnent E
  - Ex : congruence modulo n sur ℤ (a ≡ b [n] ⟺ n | (a − b))
  
- **Relation d'ordre** : réflexive + antisymétrique + transitive
  - **Ordre total** si de plus : ∀x, y, xRy ou yRx
  - Ex : ≤ sur ℝ (ordre total), ⊆ sur P(E) (ordre partiel)

---

## 7. Révisions

### Questions de cours
1. Quelle est la table de vérité de P ⟹ Q ? Quand est-elle fausse ?
2. Énoncer les lois de De Morgan pour les connecteurs logiques et pour les ensembles.
3. Quelle est la différence entre une application injective et surjective ?
4. Combien de sous-ensembles a un ensemble à 4 éléments ?
5. Qu'est-ce qu'une relation d'équivalence ? Donner un exemple.
6. Comment nie-t-on « ∀x ∈ ℝ, ∃n ∈ ℕ, n > x » ?

### Réponses
1. P ⟹ Q est **fausse uniquement** si P est vrai et Q est faux. Dans tous les autres cas (P faux, ou Q vrai), l'implication est vraie.
2. **Logique** : ¬(P ∧ Q) ⟺ ¬P ∨ ¬Q et ¬(P ∨ Q) ⟺ ¬P ∧ ¬Q. **Ensembles** : (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ et (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ.
3. **Injective** : deux éléments distincts ont des images distinctes (pas de "collision"). **Surjective** : tout élément de F a au moins un antécédent (l'image couvre tout F). Une bijection est les deux à la fois.
4. 2⁴ = **16** sous-ensembles (en comptant ∅ et l'ensemble lui-même).
5. Relation réflexive, symétrique et transitive. Ex : la congruence modulo 2 sur ℤ partitionne ℤ en pairs et impairs.
6. La négation est : **∃x ∈ ℝ, ∀n ∈ ℕ, n ≤ x** (il existe un réel qui majore tous les entiers, ce qui est faux car ℕ est non majoré).
