# 05 — Analyse Avancée — L2
> Mathématiques L2 — Suites & Séries · Fonctions de plusieurs variables · Intégrales généralisées

---

## 1. Suites et séries numériques

### 1.1 Suites — Rappels et compléments

**Suites extraites** : la suite (u_φ(n)) extraite de (uₙ) via φ strictement croissante.

> Si (uₙ) converge vers l, alors toute suite extraite converge vers l. La réciproque est vraie pour les suites monotones.

**Suite de Cauchy** : ∀ε > 0, ∃n₀, ∀p, q ≥ n₀, |uₚ − u_q| < ε.

> **Théorème** : Dans ℝ, toute suite de Cauchy converge (complétude de ℝ).

### 1.2 Séries numériques

La **série** de terme général uₙ est la suite des sommes partielles Sₙ = u₀ + u₁ + … + uₙ.

On note Σuₙ la série. Elle **converge** si (Sₙ) converge, et sa somme est S = lim Sₙ = Σ_{n=0}^{+∞} uₙ.

**Condition nécessaire de convergence** : Σuₙ converge ⟹ uₙ → 0. La réciproque est fausse (série harmonique).

### 1.3 Critères de convergence pour séries à termes positifs

| Critère | Condition | Conclusion |
|---|---|---|
| **Comparaison** | 0 ≤ uₙ ≤ vₙ | Σvₙ conv. ⟹ Σuₙ conv. ; Σuₙ div. ⟹ Σvₙ div. |
| **Règle de d'Alembert** | ρ = lim \|u_{n+1}/uₙ\| | ρ < 1 : conv. abs. ; ρ > 1 : div. ; ρ = 1 : pas de conclusion |
| **Règle de Cauchy (racine)** | ρ = lim \|uₙ\|^{1/n} | même conclusion que d'Alembert |
| **Critère intégral** | uₙ = f(n), f décr. positive | Σuₙ et ∫₁^∞ f même nature |

### 1.4 Séries alternées et convergence absolue

- **Convergence absolue** : Σ|uₙ| converge ⟹ Σuₙ converge (mais pas l'inverse).
- **Critère des séries alternées (Leibniz)** : si uₙ = (−1)ⁿ aₙ avec aₙ ≥ 0, aₙ décroissante, aₙ → 0, alors Σuₙ converge.

### 1.5 Séries de référence

| Série | Convergence | Somme |
|---|---|---|
| Géométrique Σ qⁿ | \|q\| < 1 | 1/(1−q) |
| Série harmonique Σ 1/n | Diverge | — |
| Série de Riemann Σ 1/nᵅ | α > 1 | convergente ; α ≤ 1 : divergente |
| Série exponentielle Σ xⁿ/n! | Toujours | eˣ |
| Σ (−1)ⁿ/n | Converge (non absolument) | ln(2) |

---

## 2. Séries entières

### 2.1 Définition et rayon de convergence

Une **série entière** est Σ aₙ xⁿ. Son **rayon de convergence** R est défini par :

> 1/R = lim sup |aₙ|^{1/n} (formule de Hadamard)

| |x| | Convergence |
|---|---|
| \|x\| < R | Convergence absolue |
| \|x\| > R | Divergence |
| \|x\| = R | À étudier cas par cas |

**Calcul pratique** de R : souvent via d'Alembert : R = lim |aₙ/aₙ₊₁|.

### 2.2 Propriétés

- Dérivation terme à terme sur ]−R, R[ : (Σ aₙxⁿ)' = Σ n·aₙxⁿ⁻¹ (même R)
- Intégration terme à terme sur ]−R, R[ : ∫₀ˣ Σ aₙtⁿ dt = Σ aₙxⁿ⁺¹/(n+1) (même R)

### 2.3 Développements en séries entières

| Fonction | Développement | R |
|---|---|---|
| eˣ | Σ xⁿ/n! | +∞ |
| sin(x) | Σ (−1)ⁿ x^{2n+1}/(2n+1)! | +∞ |
| cos(x) | Σ (−1)ⁿ x^{2n}/(2n)! | +∞ |
| ln(1+x) | Σ (−1)ⁿ⁺¹ xⁿ/n | 1 |
| 1/(1−x) | Σ xⁿ | 1 |
| (1+x)^α | Σ C(α,n) xⁿ | 1 |

---

## 3. Fonctions de plusieurs variables

### 3.1 Topologie dans ℝⁿ

- **Boule ouverte** : B(a, r) = {x ∈ ℝⁿ | ‖x − a‖ < r}
- **Ouvert** : A ⊆ ℝⁿ tel que tout point est centre d'une boule dans A
- **Fermé** : le complémentaire est ouvert ; équiv. : contient ses points adhérents
- **Compact** : fermé et borné dans ℝⁿ (Heine-Borel)

### 3.2 Limite et continuité

f : ℝⁿ → ℝ est **continue en a** si lim_{x→a} f(x) = f(a).

> **Attention** : en dimension > 1, il faut que la limite soit la même quelle que soit la direction/courbe d'approche. Pour montrer qu'une limite n'existe pas, chercher deux chemins donnant des limites différentes.

**Exemple** : f(x,y) = xy/(x²+y²) n'a pas de limite en (0,0) :
- Chemin y=0 → f → 0
- Chemin y=x → f → 1/2

### 3.3 Dérivées partielles

La **dérivée partielle** de f par rapport à x en (a,b) est :

> ∂f/∂x (a, b) = lim_{h→0} [f(a+h, b) − f(a, b)] / h

On dérive par rapport à x en **fixant y** comme une constante.

**Gradient** : ∇f = (∂f/∂x₁, …, ∂f/∂xₙ) — vecteur des dérivées partielles.

> **Attention** : existence des dérivées partielles ≠ différentiabilité.

### 3.4 Différentiabilité

f est **différentiable en a** s'il existe une application linéaire L telle que :

> f(a + h) = f(a) + L(h) + o(‖h‖) quand h → 0

L est la **différentielle** df(a), et L(h) = ∇f(a) · h (produit scalaire).

> **Théorème** : si toutes les dérivées partielles existent et sont continues en a, alors f est différentiable en a.

### 3.5 Dérivées d'ordre 2 et matrice Hessienne

**Dérivées partielles d'ordre 2** : ∂²f/∂x², ∂²f/∂y², ∂²f/∂x∂y, ∂²f/∂y∂x

**Théorème de Schwarz** : si ∂²f/∂x∂y et ∂²f/∂y∂x sont continues, elles sont égales.

**Matrice Hessienne** (f : ℝ² → ℝ) :

> H_f(a) = [[∂²f/∂x², ∂²f/∂x∂y], [∂²f/∂y∂x, ∂²f/∂y²]]

### 3.6 Extrema et points selles

Un **point critique** est un point où ∇f = 0.

**Classification** (f : ℝ² → ℝ, H la hessienne au point critique) :

| det(H) | ∂²f/∂x² | Nature |
|---|---|---|
| > 0 | > 0 | **Minimum local** |
| > 0 | < 0 | **Maximum local** |
| < 0 | (quelconque) | **Point selle** |
| = 0 | — | Test indécis |

### 3.7 Règle de la chaîne (composition)

Si f : ℝ² → ℝ et g : ℝ → ℝ² avec g(t) = (x(t), y(t)), alors :

> (f ∘ g)'(t) = ∂f/∂x · x'(t) + ∂f/∂y · y'(t)

**Formule générale** : d/dt [f(x(t), y(t))] = ∇f · g'(t)

---

## 4. Intégrales doubles et triples

### 4.1 Intégrale double

> ∬_D f(x, y) dx dy = « volume sous la surface z = f(x,y) au-dessus de D »

**Théorème de Fubini** : si f est continue sur le rectangle R = [a,b]×[c,d] :
> ∬_R f(x,y) dx dy = ∫ₐᵇ (∫_c^d f(x,y) dy) dx = ∫_c^d (∫ₐᵇ f(x,y) dx) dy

### 4.2 Changement de variables

**Passage en coordonnées polaires** : x = r·cos θ, y = r·sin θ
> ∬_D f(x,y) dx dy = ∬_{D'} f(r cos θ, r sin θ) · r dr dθ

Le facteur **r** est le **jacobien** du changement de variables.

**Formule générale** (changement (u,v) → (x,y)) :
> ∬ f(x,y) dx dy = ∬ f(x(u,v), y(u,v)) · |J(u,v)| du dv

où J = det([[∂x/∂u, ∂x/∂v], [∂y/∂u, ∂y/∂v]]) est le **jacobien**.

---

## 5. Intégrales généralisées (impropres)

### 5.1 Définition

L'**intégrale généralisée** ∫_a^{+∞} f(x) dx est définie par :
> ∫_a^{+∞} f(x) dx = lim_{b→+∞} ∫ₐᵇ f(x) dx (si la limite existe et est finie)

De même pour ∫_{-∞}^b f, ∫_{-∞}^{+∞} f, ou ∫_a^b f avec f non bornée en a ou b.

### 5.2 Critères de convergence

| Critère | Condition |
|---|---|
| **Comparaison** | 0 ≤ f ≤ g, ∫g conv. ⟹ ∫f conv. |
| **Équivalent** | f ~ g en +∞ ⟹ même nature |
| **Règle de Riemann** | f(x) ~ c/xᵅ en +∞ : conv. si α > 1 |
| **Intégration par parties** | Utile pour prouver convergence et calculer |

### 5.3 Intégrales de référence

| Intégrale | Convergence | Valeur |
|---|---|---|
| ∫₁^{+∞} 1/xᵅ dx | α > 1 | 1/(α−1) |
| ∫₀^1 1/xᵅ dx | α < 1 | 1/(1−α) |
| ∫₀^{+∞} e^{−x} dx | Toujours | 1 |
| ∫₀^{+∞} e^{−x²} dx | Toujours | √π/2 |
| ∫₀^{+∞} xⁿe^{−x} dx | Toujours | n! (fonction Gamma) |

---

## 6. Équations différentielles (EDO)

### 6.1 EDO du 1er ordre linéaire

**Forme** : y'(x) + a(x)·y(x) = b(x)

**Méthode** :
1. **Solution homogène** (b=0) : y_h = C·e^{−A(x)} où A'= a
2. **Solution particulière** : variation de la constante (C devient C(x))
3. **Solution générale** = y_h + y_p

**Exemple** : y' − 2y = 0 → y = Ce^{2x}

### 6.2 EDO du 2e ordre à coefficients constants

**Forme** : ay'' + by' + cy = f(x)

**Équation caractéristique** : ar² + br + c = 0

| Racines | Solution homogène |
|---|---|
| r₁ ≠ r₂ réelles | y_h = C₁e^{r₁x} + C₂e^{r₂x} |
| r₁ = r₂ = r | y_h = (C₁ + C₂x)e^{rx} |
| r = α ± iβ (complexes) | y_h = e^{αx}(C₁cos(βx) + C₂sin(βx)) |

---

## 7. Révisions

### Questions de cours
1. Quelle est la différence entre convergence simple et convergence absolue pour les séries ?
2. Trouver le rayon de convergence de Σ xⁿ/n².
3. f(x,y) = x² + y² − 2x − 4y + 5. Trouver le minimum de f.
4. Énoncer le théorème de Fubini.
5. ∫₁^{+∞} 1/x² dx converge-t-elle ? Calculer sa valeur.
6. Résoudre y'' − 5y' + 6y = 0.

### Réponses
1. **Convergence absolue** : Σ|uₙ| converge (plus forte). Elle implique la convergence simple. La **convergence conditionnelle** est la convergence de Σuₙ sans convergence absolue (ex. Σ(−1)ⁿ/n converge mais pas Σ 1/n).
2. d'Alembert : |u_{n+1}/uₙ| = |x|·n²/(n+1)² → |x|. Donc R = **1**. Aux bords : en x=1, Σ 1/n² converge (Riemann α=2>1) ; en x=−1, Σ (−1)ⁿ/n² converge absolument. L'intervalle de convergence est **[−1, 1]**.
3. ∇f = (2x−2, 2y−4) = 0 → x=1, y=2. H = [[2,0],[0,2]], det(H)=4>0, ∂²f/∂x²=2>0 → **minimum** en (1,2), f(1,2) = 1 + 4 − 2 − 8 + 5 = **0**.
4. Si f est continue sur [a,b]×[c,d], l'intégrale double se calcule en **deux intégrales simples imbriquées**, dans n'importe quel ordre : ∬f dx dy = ∫(∫f dy)dx = ∫(∫f dx)dy.
5. ∫₁^b 1/x² dx = [−1/x]₁^b = −1/b + 1 → **1** quand b→+∞. L'intégrale converge et vaut **1**.
6. Équation caractéristique : r² − 5r + 6 = 0 → (r−2)(r−3) = 0 → r₁=2, r₂=3. Solution : **y = C₁e^{2x} + C₂e^{3x}**.
