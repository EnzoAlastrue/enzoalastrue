# 02 — Analyse Réelle — L1
> Mathématiques L1 — Limites · Continuité · Dérivation · Intégration

---

## 1. Nombres réels — Rappels essentiels

### 1.1 Ensembles de nombres

| Ensemble | Notation | Description |
|---|---|---|
| Entiers naturels | ℕ = {0, 1, 2, 3, …} | Positifs ou nuls |
| Entiers relatifs | ℤ = {…, −2, −1, 0, 1, 2, …} | Positifs et négatifs |
| Rationnels | ℚ = {p/q \| p ∈ ℤ, q ∈ ℤ*} | Fractions |
| Réels | ℝ | La droite réelle complète |
| Complexes | ℂ | Extension de ℝ |

> ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ ⊂ ℂ

### 1.2 Valeur absolue

- **Définition** : |x| = x si x ≥ 0, −x si x < 0
- **Inégalité triangulaire** : |x + y| ≤ |x| + |y|
- |x − y| représente la **distance** entre x et y sur la droite réelle

### 1.3 Borne supérieure et inférieure

- **Majorant** de A ⊆ ℝ : M tel que ∀x ∈ A, x ≤ M
- **Supremum** (borne sup) : le plus petit des majorants → sup(A)
- **Infimum** (borne inf) : le plus grand des minorants → inf(A)

> **Axiome de la borne supérieure** : Tout sous-ensemble de ℝ non vide et majoré admet un supremum dans ℝ. (Cet axiome distingue ℝ de ℚ.)

---

## 2. Suites numériques

### 2.1 Définitions

- **Suite** : application de ℕ dans ℝ, notée (uₙ)ₙ∈ℕ
- **Suite arithmétique** : uₙ = u₀ + n·r → Sₙ = (n+1)(u₀ + uₙ)/2
- **Suite géométrique** : uₙ = u₀ · qⁿ → Sₙ = u₀ · (1 − qⁿ⁺¹)/(1 − q) si q ≠ 1

### 2.2 Convergence

> Une suite (uₙ) **converge vers l** si : ∀ε > 0, ∃n₀ ∈ ℕ, ∀n ≥ n₀, |uₙ − l| < ε

On note alors lim(n→∞) uₙ = l.

| Type | Définition | Exemple |
|---|---|---|
| Convergente | Tend vers une limite finie l | uₙ = 1/n → 0 |
| Divergente vers +∞ | ∀M > 0, ∃n₀, ∀n ≥ n₀, uₙ > M | uₙ = n² |
| Divergente (oscillante) | Pas de limite | uₙ = (−1)ⁿ |

### 2.3 Théorèmes sur les limites

- **Unicité** : si (uₙ) converge, sa limite est unique
- **Opérations** : si uₙ → l et vₙ → l', alors uₙ + vₙ → l + l', uₙ · vₙ → l · l'
- **Théorème des gendarmes** : si uₙ ≤ wₙ ≤ vₙ et uₙ → l, vₙ → l, alors wₙ → l
- **Suite monotone et bornée** → convergente (théorème fondamental)

### 2.4 Suites usuelles

| Suite | Limite |
|---|---|
| 1/n | 0 |
| qⁿ (\|q\| < 1) | 0 |
| qⁿ (q > 1) | +∞ |
| n^α/eⁿ | 0 (l'exponentielle l'emporte) |
| ln(n)/n^α (α > 0) | 0 (le log perd contre toute puissance) |
| (1 + 1/n)ⁿ | e |

---

## 3. Limites de fonctions

### 3.1 Définition (limite en un point)

> f(x) tend vers l quand x tend vers a si : ∀ε > 0, ∃δ > 0, 0 < |x − a| < δ ⟹ |f(x) − l| < ε

On note lim(x→a) f(x) = l.

### 3.2 Limites usuelles et formes indéterminées

| Forme indéterminée | Exemples de techniques de levée |
|---|---|
| ∞/∞ | Diviser par le terme dominant |
| 0/0 | Factoriser, DL, règle de L'Hôpital |
| 0 × ∞ | Réécrire comme ∞/∞ ou 0/0 |
| 1^∞, ∞⁰, 0⁰ | Passer au logarithme |
| ∞ − ∞ | Factoriser ou conjugué |

### 3.3 Limites classiques à connaître

| Limite | Valeur |
|---|---|
| lim(x→0) sin(x)/x | 1 |
| lim(x→0) (eˣ − 1)/x | 1 |
| lim(x→0) ln(1 + x)/x | 1 |
| lim(x→0) (1 − cos x)/x² | 1/2 |
| lim(x→+∞) xⁿ/eˣ | 0 |
| lim(x→+∞) ln(x)/xᵅ (α > 0) | 0 |

---

## 4. Continuité

### 4.1 Définition

> f est **continue en a** si lim(x→a) f(x) = f(a)

Autrement dit : f est définie en a, sa limite existe en a, et elles sont égales.

f est **continue sur I** si elle est continue en tout point de I.

### 4.2 Théorèmes fondamentaux

- **Théorème des valeurs intermédiaires (TVI)** :
  Si f est continue sur [a, b] et k est entre f(a) et f(b), alors ∃c ∈ [a, b] tel que f(c) = k.
  
  > Corollaire : f continue sur [a, b], f(a) et f(b) de signes opposés ⟹ ∃c ∈ ]a, b[ tel que f(c) = 0.

- **Théorème des bornes atteintes** :
  Si f est continue sur [a, b] (fermé borné), alors f est bornée et atteint ses bornes (∃min et ∃max).

### 4.3 Types de discontinuités

| Type | Description | Exemple |
|---|---|---|
| Discontinuité de saut | limites gauche et droite existent mais ≠ | ⌊x⌋ (partie entière) en x = n |
| Discontinuité effaçable | la limite existe mais ≠ f(a) | sin(x)/x en 0 (si on pose f(0) = 0, elle devient continue) |
| Discontinuité essentielle | la limite n'existe pas | sin(1/x) en 0 |

---

## 5. Dérivation

### 5.1 Définition

> f est **dérivable en a** si la limite suivante existe et est finie :
> f'(a) = lim(h→0) [f(a+h) − f(a)] / h

Géométriquement : f'(a) est la **pente de la tangente** à la courbe en (a, f(a)).

### 5.2 Dérivées usuelles

| Fonction | Dérivée | Condition |
|---|---|---|
| xⁿ | n·xⁿ⁻¹ | n ∈ ℤ |
| √x | 1/(2√x) | x > 0 |
| eˣ | eˣ | ℝ |
| ln(x) | 1/x | x > 0 |
| sin(x) | cos(x) | ℝ |
| cos(x) | −sin(x) | ℝ |
| tan(x) | 1/cos²(x) = 1 + tan²(x) | x ≠ π/2 + kπ |
| arcsin(x) | 1/√(1−x²) | x ∈ ]−1, 1[ |
| arctan(x) | 1/(1+x²) | ℝ |

### 5.3 Règles de dérivation

| Règle | Formule |
|---|---|
| Linéarité | (αf + βg)' = αf' + βg' |
| Produit | (fg)' = f'g + fg' |
| Quotient | (f/g)' = (f'g − fg')/g² |
| Composition (règle chaîne) | (f∘g)'(x) = f'(g(x))·g'(x) |
| Réciproque | (f⁻¹)'(y) = 1/f'(f⁻¹(y)) |

### 5.4 Théorèmes importants

- **Théorème de Rolle** : f continue sur [a,b], dérivable sur ]a,b[, f(a) = f(b) ⟹ ∃c ∈ ]a,b[ tel que f'(c) = 0.
- **Théorème des accroissements finis (TAF)** : f continue sur [a,b], dérivable sur ]a,b[ ⟹ ∃c ∈ ]a,b[ tel que f(b)−f(a) = f'(c)·(b−a).
- **Corollaire** : f' > 0 sur I ⟹ f strictement croissante sur I.

### 5.5 Développements limités (DL)

Un DL de f en 0 à l'ordre n est une approximation polynomiale :

> f(x) = a₀ + a₁x + a₂x² + … + aₙxⁿ + o(xⁿ)

| Fonction | DL en 0 à l'ordre n |
|---|---|
| eˣ | 1 + x + x²/2! + x³/3! + … + xⁿ/n! + o(xⁿ) |
| sin(x) | x − x³/6 + x⁵/120 − … + o(x²ⁿ) |
| cos(x) | 1 − x²/2 + x⁴/24 − … + o(x²ⁿ⁺¹) |
| ln(1+x) | x − x²/2 + x³/3 − … + (−1)ⁿ⁺¹xⁿ/n + o(xⁿ) |
| (1+x)^α | 1 + αx + α(α−1)x²/2! + … |
| 1/(1−x) | 1 + x + x² + … + xⁿ + o(xⁿ) |

> **Usage** : lever des formes indéterminées, calculer des limites, comparer des fonctions.

---

## 6. Intégration

### 6.1 Intégrale de Riemann

> L'intégrale ∫[a,b] f(x)dx représente l'**aire algébrique** entre la courbe de f et l'axe des abscisses.

- f ≥ 0 : aire positive
- f ≤ 0 : aire négative (comptée négativement)

### 6.2 Primitives usuelles

| Fonction f(x) | Primitive F(x) | Condition |
|---|---|---|
| xⁿ (n ≠ −1) | xⁿ⁺¹/(n+1) | |
| 1/x | ln\|x\| | x ≠ 0 |
| eˣ | eˣ | |
| sin(x) | −cos(x) | |
| cos(x) | sin(x) | |
| 1/cos²(x) | tan(x) | |
| 1/√(1−x²) | arcsin(x) | x ∈ ]−1,1[ |
| 1/(1+x²) | arctan(x) | |

### 6.3 Propriétés de l'intégrale

| Propriété | Formule |
|---|---|
| Linéarité | ∫(αf + βg) = α∫f + β∫g |
| Relation de Chasles | ∫[a,c] f = ∫[a,b] f + ∫[b,c] f |
| Inversion des bornes | ∫[a,b] f = −∫[b,a] f |
| Positivité | f ≥ 0 sur [a,b] ⟹ ∫[a,b] f ≥ 0 |
| Inégalité triangulaire | \|∫[a,b] f\| ≤ ∫[a,b] \|f\| |

### 6.4 Techniques de calcul

**Intégration par parties (IPP)** :
> ∫[a,b] u·v' = [u·v]^b_a − ∫[a,b] u'·v

*Mnémotechnique : choisir u = LIATE (Logarithme, Inverse trig., Algébrique, Trig., Exponentielle)*

**Changement de variable** :
> ∫[a,b] f(g(t))·g'(t) dt = ∫[g(a),g(b)] f(x) dx

### 6.5 Théorème fondamental de l'analyse

Si f est continue sur [a, b], alors la fonction F définie par F(x) = ∫[a,x] f(t)dt est dérivable sur [a,b] et F'(x) = f(x).

> **Conséquence** : ∫[a,b] f(x)dx = F(b) − F(a) où F est une primitive quelconque de f.

---

## 7. Étude de fonctions

### Plan d'étude standard

1. **Domaine de définition** Df
2. **Parité** (paire si f(−x) = f(x), impaire si f(−x) = −f(x))
3. **Périodicité**
4. **Limites aux bornes** (y compris asymptotes)
5. **Dérivée** f' et tableau de signe
6. **Variations** et extrema
7. **Convexité** (signe de f'')
8. **Tableau de variations**
9. **Représentation graphique**

### Asymptotes

| Type | Condition | Équation |
|---|---|---|
| Verticale en a | lim(x→a) f(x) = ±∞ | x = a |
| Horizontale en ±∞ | lim(x→±∞) f(x) = l | y = l |
| Oblique en ±∞ | lim(x→±∞) [f(x) − (ax+b)] = 0 | y = ax + b |

---

## 8. Révisions

### Questions de cours
1. Énoncer le Théorème des Valeurs Intermédiaires et donner une application.
2. Calculer la dérivée de f(x) = x²·eˣ et de g(x) = ln(sin(x)).
3. Quelle est la limite de (eˣ − 1 − x)/x² quand x → 0 ?
4. Énoncer le Théorème des Accroissements Finis.
5. Calculer ∫₀¹ x·eˣ dx par intégration par parties.
6. Donner le DL de cos(x) à l'ordre 4 en 0.

### Réponses
1. **TVI** : si f est continue sur [a,b] et k est compris entre f(a) et f(b), il existe c ∈ [a,b] tel que f(c) = k. **Application** : montrer qu'un polynôme de degré impair a au moins une racine réelle.
2. **f'(x)** = 2x·eˣ + x²·eˣ = eˣ(x² + 2x) = xeˣ(x+2). **g'(x)** = cos(x)/sin(x) = cotan(x).
3. DL de eˣ : eˣ = 1 + x + x²/2 + o(x²), donc eˣ − 1 − x = x²/2 + o(x²), et (eˣ − 1 − x)/x² → **1/2**.
4. **TAF** : si f est continue sur [a,b] et dérivable sur ]a,b[, alors ∃c ∈ ]a,b[ tel que f(b) − f(a) = f'(c)·(b−a).
5. **IPP** avec u = x, v' = eˣ : ∫₀¹ xeˣ dx = [xeˣ]₀¹ − ∫₀¹ eˣ dx = e − [eˣ]₀¹ = e − (e−1) = **1**.
6. cos(x) = **1 − x²/2 + x⁴/24** + o(x⁴).
