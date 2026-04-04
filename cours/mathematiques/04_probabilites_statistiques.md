# 04 — Probabilités & Statistiques
> Mathématiques L1-L2 — Probabilités · Variables aléatoires · Statistiques

---

## 1. Calcul des probabilités

### 1.1 Espace probabilisé

Un **espace probabilisé** est un triplet (Ω, A, P) :
- **Ω** : espace d'états (univers, ensemble des issues possibles)
- **A** : tribu (famille de sous-ensembles — les *événements*)
- **P** : probabilité (application A → [0, 1] respectant les axiomes)

**Axiomes de Kolmogorov** :
1. ∀A ∈ A, P(A) ≥ 0
2. P(Ω) = 1
3. Si A₁, A₂, … sont **deux à deux disjoints**, P(∪Aᵢ) = ΣP(Aᵢ)

### 1.2 Propriétés fondamentales

| Propriété | Formule |
|---|---|
| Complémentaire | P(Aᶜ) = 1 − P(A) |
| Événement impossible | P(∅) = 0 |
| Union | P(A ∪ B) = P(A) + P(B) − P(A ∩ B) |
| Inclusion | A ⊆ B ⟹ P(A) ≤ P(B) |
| Formule de Boole | P(A ∪ B ∪ C) = ΣP(Aᵢ) − ΣP(Aᵢ∩Aⱼ) + P(A∩B∩C) |

### 1.3 Probabilité conditionnelle

> P(A | B) = P(A ∩ B) / P(B) (avec P(B) > 0)

« Probabilité de A sachant B » : on restreint l'espace Ω à B.

**Formule des probabilités composées** :
> P(A ∩ B) = P(A|B) · P(B) = P(B|A) · P(A)

**Formule des probabilités totales** :
Si B₁, …, Bₙ forment une **partition** de Ω (disjoints, de réunion Ω, P(Bᵢ) > 0) :
> P(A) = Σᵢ P(A | Bᵢ) · P(Bᵢ)

**Formule de Bayes** :
> P(Bᵢ | A) = P(A | Bᵢ) · P(Bᵢ) / P(A)

### 1.4 Indépendance

A et B sont **indépendants** si P(A ∩ B) = P(A) · P(B).

> Attention : indépendance ≠ incompatibilité (événements disjoints avec P > 0 sont **dépendants**).

---

## 2. Dénombrement

### 2.1 Arrangements et permutations

| Concept | Formule | Description |
|---|---|---|
| Permutations de n | n! | Ranger n objets distincts dans un ordre |
| p-arrangements de n | n!/(n−p)! | Choisir p objets parmi n en tenant compte de l'ordre |
| Combinaisons C(n,p) | n!/[p!(n−p)!] | Choisir p objets parmi n sans tenir compte de l'ordre |

**Notation** : C(n, p) = Cₙᵖ = \binom{n}{p}

### 2.2 Formules importantes

- **Formule de Pascal** : Cₙᵖ = Cₙ₋₁ᵖ⁻¹ + Cₙ₋₁ᵖ
- **Formule du binôme de Newton** : (a + b)ⁿ = Σₖ Cₙᵏ · aᵏ · bⁿ⁻ᵏ
- **Symétrie** : Cₙᵖ = Cₙⁿ⁻ᵖ
- Σₖ Cₙᵏ = 2ⁿ (nombre de sous-ensembles de {1,…,n})

---

## 3. Variables aléatoires discrètes

### 3.1 Définition

Une **variable aléatoire (va) discrète** X est une application X : Ω → ℝ prenant un nombre fini ou dénombrable de valeurs x₁, x₂, …

**Loi de X** : P(X = xᵢ) = pᵢ ≥ 0, avec Σpᵢ = 1.

### 3.2 Espérance, variance, écart-type

| Grandeur | Formule | Interprétation |
|---|---|---|
| **Espérance** E[X] | Σᵢ xᵢ · P(X=xᵢ) | Valeur moyenne |
| **Variance** V[X] | E[X²] − (E[X])² | Dispersion autour de la moyenne |
| **Écart-type** σ | √V[X] | Même unité que X |

**Propriétés** :
- E[aX + b] = aE[X] + b
- V[aX + b] = a²V[X]
- Si X et Y **indépendantes** : E[XY] = E[X]·E[Y] et V[X+Y] = V[X]+V[Y]

### 3.3 Lois discrètes usuelles

| Loi | Notation | P(X=k) | E[X] | V[X] |
|---|---|---|---|---|
| Bernoulli | B(p) | p si k=1, 1−p si k=0 | p | p(1−p) |
| Binomiale | B(n,p) | Cₙᵏ pᵏ(1−p)ⁿ⁻ᵏ | np | np(1−p) |
| Géométrique | G(p) | (1−p)ᵏ⁻¹ p, k≥1 | 1/p | (1−p)/p² |
| Poisson | P(λ) | e⁻λ λᵏ/k! | λ | λ |
| Uniforme discrète | U({1,…,n}) | 1/n | (n+1)/2 | (n²−1)/12 |

> **Approximation de Poisson** : si n grand, p petit, np = λ constant, alors B(n,p) ≈ P(λ).

---

## 4. Variables aléatoires continues

### 4.1 Densité de probabilité

Une va continue X admet une **densité** f : ℝ → ℝ⁺ si :
- f(x) ≥ 0 pour tout x
- ∫₋∞^{+∞} f(x) dx = 1
- P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx

**Fonction de répartition** : F(x) = P(X ≤ x) = ∫₋∞^x f(t) dt

### 4.2 Espérance, variance pour les va continues

| Grandeur | Formule |
|---|---|
| E[X] | ∫₋∞^{+∞} x·f(x) dx |
| E[g(X)] | ∫₋∞^{+∞} g(x)·f(x) dx |
| V[X] | E[X²] − (E[X])² |

### 4.3 Lois continues usuelles

| Loi | Notation | Densité | E[X] | V[X] |
|---|---|---|---|---|
| Uniforme | U([a,b]) | 1/(b−a) sur [a,b] | (a+b)/2 | (b−a)²/12 |
| Exponentielle | Exp(λ) | λe^{−λx} sur ℝ⁺ | 1/λ | 1/λ² |
| Normale | N(μ,σ²) | voir ci-dessous | μ | σ² |
| Gamma | Γ(α,β) | x^{α−1}e^{−x/β}/[β^α Γ(α)] | αβ | αβ² |
| Chi-deux | χ²(n) | cas particulier de Gamma | n | 2n |

**Densité de la loi normale N(μ, σ²)** :
> f(x) = 1/(σ√(2π)) · exp(−(x−μ)²/(2σ²))

**Loi normale standard** N(0,1) : μ=0, σ=1, notée Z.

> **Standardisation** : si X ~ N(μ, σ²), alors Z = (X−μ)/σ ~ N(0,1)

### 4.4 Propriétés de la loi normale

- Symétrie par rapport à μ : f(μ+t) = f(μ−t)
- La somme de va normales indépendantes est normale
- **Règle 68-95-99.7** : P(|X−μ| ≤ σ) ≈ 68%, P(|X−μ| ≤ 2σ) ≈ 95%, P(|X−μ| ≤ 3σ) ≈ 99.7%

---

## 5. Statistique descriptive

### 5.1 Paramètres de position

Soit x₁, …, xₙ un échantillon de taille n.

| Paramètre | Formule | Description |
|---|---|---|
| **Moyenne** x̄ | (1/n) Σxᵢ | Centre de gravité |
| **Médiane** Me | valeur séparant les 50% inf. et sup. | Milieu ordinal |
| **Mode** Mo | valeur la plus fréquente | Pic de la distribution |

### 5.2 Paramètres de dispersion

| Paramètre | Formule | Description |
|---|---|---|
| **Étendue** | max − min | Amplitude totale |
| **Variance** s² | (1/n) Σ(xᵢ − x̄)² | Dispersion quadratique |
| **Écart-type** s | √s² | Même unité que les données |
| **Coefficient de variation** | s/x̄ | Dispersion relative |
| **Quartiles** Q1, Q3 | 25e et 75e percentiles | Positions intermédiaires |
| **IQR** | Q3 − Q1 | Écart interquartile |

### 5.3 Représentations graphiques

| Type | Usage |
|---|---|
| Histogramme | Distribution d'une variable quantitative continue |
| Boîte à moustaches (boxplot) | Résumé 5-chiffres : min, Q1, médiane, Q3, max |
| Diagramme en barres | Variable qualitative ou discrète |
| Diagramme circulaire | Proportions/parts |
| Nuage de points | Relation entre deux variables quantitatives |

---

## 6. Statistique inférentielle (L2)

### 6.1 Estimation ponctuelle

**But** : estimer un paramètre θ de la population à partir d'un échantillon.

- **Estimateur** T(X₁,…,Xₙ) : statistique calculée sur l'échantillon
- **Estimateur sans biais** : E[T] = θ
- **Estimateur convergent** : T → θ quand n → ∞ (en probabilité)

**Estimateurs usuels** :

| Paramètre | Estimateur | Sans biais ? |
|---|---|---|
| Moyenne μ | x̄ = (1/n)Σxᵢ | Oui |
| Variance σ² | s² = 1/(n−1) Σ(xᵢ−x̄)² | Oui (avec n−1) |

### 6.2 Intervalles de confiance

**IC à 95% pour la moyenne** (population normale, σ connue) :
> IC = [x̄ − 1.96·σ/√n , x̄ + 1.96·σ/√n]

**Si σ inconnue** : on remplace σ par s et le seuil 1.96 par le quantile de la **loi de Student t(n−1)**.

> **Interprétation** : si on répétait l'expérience un grand nombre de fois, 95% des intervalles construits contiendraient le vrai paramètre.

### 6.3 Tests d'hypothèses

| Étape | Description |
|---|---|
| **H₀** | Hypothèse nulle (à tester) |
| **H₁** | Hypothèse alternative (ce qu'on cherche à montrer) |
| **Statistique de test** | Valeur calculée sur l'échantillon |
| **p-valeur** | Probabilité d'obtenir un résultat aussi extrême sous H₀ |
| **Décision** | Si p-valeur < α (seuil), on rejette H₀ |

**Tests courants** :

| Test | Hypothèse testée | Statistique |
|---|---|---|
| Test z | H₀ : μ = μ₀ (σ connue) | Z = (x̄ − μ₀)/(σ/√n) ~ N(0,1) |
| Test t de Student | H₀ : μ = μ₀ (σ inconnue) | T = (x̄ − μ₀)/(s/√n) ~ t(n−1) |
| Test du χ² | Indépendance ou adéquation | Σ(Obs−Att)²/Att ~ χ²(ddl) |

---

## 7. Théorèmes asymptotiques (L2)

### 7.1 Loi des grands nombres (LGN)

**LGN faible** : si X₁, X₂, … sont iid d'espérance μ, alors :
> x̄ₙ = (X₁+…+Xₙ)/n → μ en probabilité

**LGN forte** : la convergence a lieu **presque sûrement** (avec probabilité 1).

### 7.2 Théorème central limite (TCL)

Si X₁, X₂, … sont iid d'espérance μ et variance σ² finie, alors :
> √n · (x̄ₙ − μ)/σ → N(0, 1) en loi (quand n → ∞)

> **Usage pratique** : pour n ≥ 30, on peut approximer la distribution de x̄ₙ par une loi normale, quelle que soit la distribution d'origine.

---

## 8. Révisions

### Questions de cours
1. Énoncer la formule de Bayes et donner un exemple d'application.
2. X suit une loi binomiale B(10, 0.3). Calculer E[X] et V[X].
3. Quelle est la différence entre moyenne, médiane et mode ?
4. Énoncer le Théorème Central Limite.
5. Qu'est-ce qu'un intervalle de confiance à 95% ?
6. Lancer un dé équilibré. Calculer P(résultat > 4 | résultat pair).

### Réponses
1. **P(Bᵢ|A) = P(A|Bᵢ)·P(Bᵢ) / ΣP(A|Bⱼ)·P(Bⱼ)**. Ex. : test médical — probabilité d'être malade sachant que le test est positif, en tenant compte de la prévalence de la maladie.
2. E[X] = np = 10×0.3 = **3**. V[X] = np(1−p) = 10×0.3×0.7 = **2.1**.
3. **Moyenne** : somme/n (sensible aux valeurs extrêmes). **Médiane** : valeur centrale (robuste). **Mode** : valeur la plus fréquente. Sur une distribution symétrique, elles coïncident.
4. Si X₁,…,Xₙ sont iid d'espérance μ et variance σ², alors **√n(x̄ₙ−μ)/σ → N(0,1)** en loi. Permet d'approcher la distribution de la moyenne par une normale pour n grand.
5. Intervalle aléatoire construit à partir de l'échantillon tel que, **si on répétait l'expérience**, 95% des intervalles obtenus contiendraient le vrai paramètre θ. Ce n'est PAS « il y a 95% de chances que θ soit dans cet intervalle ».
6. Ω_pair = {2, 4, 6}. Parmi ces 3 valeurs, une seule est > 4 : {6}. Donc P(>4 | pair) = **1/3**.
