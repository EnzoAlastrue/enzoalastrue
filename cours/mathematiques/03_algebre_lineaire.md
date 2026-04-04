# 03 — Algèbre Linéaire
> Mathématiques L1-L2 — Matrices · Systèmes · Espaces vectoriels · Diagonalisation

---

## 1. Matrices

### 1.1 Définition

Une **matrice** A de taille m × n est un tableau rectangulaire de m lignes et n colonnes de nombres réels (ou complexes).

On note A = (aᵢⱼ) où aᵢⱼ est le coefficient ligne i, colonne j.

**Notations spéciales** :
- Mₘₙ(ℝ) : ensemble des matrices m×n à coefficients réels
- Mₙ(ℝ) : matrices carrées n×n
- Iₙ : matrice identité n×n (1 sur la diagonale, 0 ailleurs)
- 0 : matrice nulle

### 1.2 Opérations sur les matrices

| Opération | Condition | Formule |
|---|---|---|
| Addition | Même taille | (A + B)ᵢⱼ = aᵢⱼ + bᵢⱼ |
| Multiplication scalaire | — | (λA)ᵢⱼ = λ·aᵢⱼ |
| Produit | A : m×n, B : n×p | (AB)ᵢⱼ = Σₖ aᵢₖ·bₖⱼ |
| Transposée | A : m×n | (Aᵀ)ᵢⱼ = aⱼᵢ (taille n×m) |

> **Attention** : le produit matriciel **n'est pas commutatif** en général (AB ≠ BA).

### 1.3 Types de matrices

| Nom | Propriété |
|---|---|
| Symétrique | Aᵀ = A |
| Antisymétrique | Aᵀ = −A |
| Orthogonale | AᵀA = AAᵀ = Iₙ (équiv. : A⁻¹ = Aᵀ) |
| Triangulaire sup. | aᵢⱼ = 0 si i > j |
| Triangulaire inf. | aᵢⱼ = 0 si i < j |
| Diagonale | aᵢⱼ = 0 si i ≠ j |

---

## 2. Déterminant

### 2.1 Définition et calcul

Le **déterminant** det(A) est un scalaire associé à toute matrice carrée.

**Ordre 2** : det([a b; c d]) = ad − bc

**Ordre 3** (règle de Sarrus) :
```
det([a b c; d e f; g h i]) = aei + bfg + cdh − ceg − afh − bdi
```

**Développement par rapport à la ligne i** (cofacteurs) :
> det(A) = Σⱼ (−1)^(i+j) · aᵢⱼ · Mᵢⱼ

où Mᵢⱼ est le **mineur** (déterminant de la matrice obtenue en supprimant la ligne i et la colonne j).

### 2.2 Propriétés du déterminant

| Propriété | Énoncé |
|---|---|
| Produit | det(AB) = det(A)·det(B) |
| Transposée | det(Aᵀ) = det(A) |
| Matrice singulière | det(A) = 0 ⟺ A n'est pas inversible |
| Échange de lignes | Échange de 2 lignes → change le signe |
| Ligne multipliée par λ | det multiplié par λ |
| Ligne combinaison linéaire | det = 0 (lignes liées) |
| Triangulaire | det = produit des termes diagonaux |

### 2.3 Matrice inverse

A ∈ Mₙ(ℝ) est **inversible** si ∃B ∈ Mₙ(ℝ) tel que AB = BA = Iₙ. On note B = A⁻¹.

**Condition** : A inversible ⟺ det(A) ≠ 0

**Formule pour une matrice 2×2** :
> Si A = [a b; c d], alors A⁻¹ = 1/(ad−bc) · [d −b; −c a]

**Méthode générale** : pivot de Gauss sur [A | Iₙ] → [Iₙ | A⁻¹]

---

## 3. Systèmes linéaires

### 3.1 Représentation matricielle

Un système de m équations à n inconnues s'écrit AX = B, où :
- A ∈ Mₘₙ(ℝ) : **matrice des coefficients**
- X ∈ Mₙ₁(ℝ) : **vecteur des inconnues**
- B ∈ Mₘ₁(ℝ) : **vecteur du second membre**

### 3.2 Méthode du pivot de Gauss

**Opérations élémentaires autorisées** (ne changent pas l'ensemble solution) :
1. Échanger deux lignes : Lᵢ ↔ Lⱼ
2. Multiplier une ligne par un scalaire non nul : Lᵢ ← λ·Lᵢ
3. Ajouter à une ligne un multiple d'une autre : Lᵢ ← Lᵢ + λ·Lⱼ

**Objectif** : réduire la matrice augmentée [A|B] en forme **échelonnée** (triangulaire sup.), puis résoudre par **substitution arrière**.

### 3.3 Discussion selon le rang

Soit r = rang(A), r' = rang([A|B]) (matrice augmentée), n = nombre d'inconnues.

| Condition | Interprétation | Solutions |
|---|---|---|
| r' > r | Système **incompatible** | Aucune |
| r' = r = n | Système de Cramer | Unique |
| r' = r < n | Infinité de solutions | n − r **degrés de liberté** |

> **Théorème de Rouché-Fontené** : le système AX = B est compatible ⟺ rang(A) = rang([A\|B]).

---

## 4. Espaces vectoriels

### 4.1 Définition

Un **espace vectoriel** (ev) sur ℝ est un ensemble E muni de deux lois :
- Addition : (u, v) ↦ u + v
- Multiplication par scalaire : (λ, u) ↦ λu

vérifiant 8 axiomes (associativité, commutativité, neutre, opposé, distributivités, compatibilité).

**Exemples fondamentaux** :
- ℝⁿ (n-uplets de réels)
- Mₘₙ(ℝ) (matrices)
- ℝ[X] (polynômes)
- C⁰([a,b]) (fonctions continues sur [a,b])

### 4.2 Sous-espace vectoriel (sev)

F ⊆ E est un **sev** si :
1. F est non vide (0_E ∈ F)
2. ∀u, v ∈ F, u + v ∈ F
3. ∀λ ∈ ℝ, ∀u ∈ F, λu ∈ F

> **Équivalent compact** : F est un sev ⟺ ∀u, v ∈ F, ∀λ, μ ∈ ℝ, λu + μv ∈ F.

### 4.3 Famille libre, génératrice, base

| Concept | Définition |
|---|---|
| **Famille libre** | λ₁v₁ + … + λₖvₖ = 0 ⟹ tous les λᵢ = 0 (pas de relation non triviale) |
| **Famille génératrice** | tout vecteur de E s'écrit comme combinaison linéaire des vᵢ |
| **Base** | famille libre **et** génératrice |

**Dimension** d'un ev : nombre d'éléments d'une base (toutes les bases ont le même cardinal).

| Espace | Dimension | Base canonique |
|---|---|---|
| ℝⁿ | n | e₁ = (1,0,…,0), …, eₙ = (0,…,0,1) |
| Mₘₙ(ℝ) | m·n | Matrices Eᵢⱼ (1 en position (i,j), 0 ailleurs) |
| ℝₙ[X] | n+1 | 1, X, X², …, Xⁿ |

### 4.4 Rang d'une matrice

Le **rang** de A ∈ Mₘₙ(ℝ) est la dimension de l'espace engendré par ses colonnes (ou ses lignes — même valeur).

> rang(A) ≤ min(m, n)  
> A inversible ⟺ rang(A) = n

---

## 5. Applications linéaires

### 5.1 Définition

f : E → F est **linéaire** si :
- ∀u, v ∈ E : f(u + v) = f(u) + f(v)
- ∀λ ∈ ℝ, ∀u ∈ E : f(λu) = λf(u)

> Équivalent : f(λu + μv) = λf(u) + μf(v) pour tous λ, μ, u, v.

**Conséquence immédiate** : f(0) = 0 et f(−u) = −f(u).

### 5.2 Noyau et image

| Objet | Définition | Type |
|---|---|---|
| **Noyau** Ker(f) | {x ∈ E \| f(x) = 0_F} | Sev de E |
| **Image** Im(f) | {f(x) \| x ∈ E} | Sev de F |

**Théorème du rang** (dimension) :
> dim(E) = dim(Ker f) + dim(Im f) = dim(Ker f) + rang(f)

### 5.3 Injectivité, surjectivité, bijectivité

| Propriété | Équivalent pour f linéaire |
|---|---|
| Injective | Ker(f) = {0} |
| Surjective | Im(f) = F |
| Bijective (isomorphisme) | Ker(f) = {0} et Im(f) = F |

> Si dim(E) = dim(F), alors injective ⟺ surjective ⟺ bijective.

### 5.4 Matrice d'une application linéaire

Si B_E = (e₁,…,eₙ) et B_F = (f₁,…,fₘ) sont des bases, la **matrice de f dans ces bases** est la matrice A ∈ Mₘₙ(ℝ) dont la j-ème colonne contient les coordonnées de f(eⱼ) dans B_F.

**Changement de base** : si P est la matrice de passage de B à B', alors :
> A' = P⁻¹AP

---

## 6. Valeurs propres et diagonalisation (L2)

### 6.1 Valeurs propres et vecteurs propres

Soit A ∈ Mₙ(ℝ). λ est une **valeur propre** de A s'il existe v ≠ 0 tel que **Av = λv**.

- v est un **vecteur propre** associé à λ
- **Espace propre** : Eλ = Ker(A − λIₙ)

**Calcul** :
1. Résoudre l'**équation caractéristique** : det(A − λI) = 0
2. Pour chaque λ trouvé, résoudre (A − λI)v = 0 pour trouver les vecteurs propres

**Polynôme caractéristique** : χ_A(λ) = det(A − λI) est un polynôme de degré n.

### 6.2 Diagonalisation

A est **diagonalisable** s'il existe P inversible et D diagonale tels que A = PDP⁻¹.

| Condition | Diagonalisable |
|---|---|
| n valeurs propres distinctes | OUI (toujours) |
| Pour chaque vp λ : dim(Eλ) = multiplicité de λ | OUI (CNS) |
| Matrice symétrique réelle | OUI (théorème spectral) |

**Méthode** :
1. Calculer χ_A et trouver les valeurs propres λ₁, …, λₖ
2. Pour chaque λᵢ, calculer une base de Eλᵢ
3. Si les vecteurs propres forment une base de ℝⁿ → A est diagonalisable
4. P = matrice dont les colonnes sont les vecteurs propres, D = diag(λ₁, …, λₙ)

### 6.3 Applications de la diagonalisation

- **Puissance de matrice** : Aⁿ = PDⁿP⁻¹ (facile car Dⁿ = diag(λ₁ⁿ, …, λₙⁿ))
- **Suites récurrentes linéaires** : exprimer Uₙ = AⁿU₀
- **Exponentielle matricielle** : e^A = Pe^D P⁻¹

---

## 7. Produit scalaire (L2)

### 7.1 Définition

Un **produit scalaire** sur E est une application ⟨·,·⟩ : E×E → ℝ bilinéaire, symétrique et **définie positive** :
- ⟨u, u⟩ ≥ 0 et ⟨u, u⟩ = 0 ⟺ u = 0

**Norme** associée : ‖u‖ = √⟨u, u⟩

**Inégalité de Cauchy-Schwarz** : |⟨u, v⟩| ≤ ‖u‖·‖v‖

### 7.2 Orthogonalité

- u ⊥ v si ⟨u, v⟩ = 0
- **Base orthonormée** (BON) : base où ⟨eᵢ, eⱼ⟩ = δᵢⱼ (0 si i≠j, 1 si i=j)
- **Procédé de Gram-Schmidt** : orthonormaliser n'importe quelle base

### 7.3 Projection orthogonale

Si F est un sev de dimension finie et u ∈ E, la **projection orthogonale** de u sur F est l'unique p ∈ F tel que u − p ⊥ F (minimise la distance de u à F).

---

## 8. Révisions

### Questions de cours
1. Calculer le déterminant de A = [[2,1],[3,4]] et l'inverse de A.
2. Énoncer le théorème du rang.
3. Un système AX = B avec A de taille 3×4 et rang(A) = 2 : combien de degrés de liberté dans l'ensemble des solutions ?
4. Qu'est-ce qu'un vecteur propre ? Comment trouve-t-on les valeurs propres ?
5. La matrice A = [[3,1],[0,3]] est-elle diagonalisable ? Pourquoi ?
6. Énoncer l'inégalité de Cauchy-Schwarz.

### Réponses
1. det(A) = 2×4 − 1×3 = **5**. A⁻¹ = (1/5)[[4,−1],[−3,2]] = [[4/5, −1/5],[−3/5, 2/5]].
2. Pour f : E → F linéaire : **dim(E) = dim(Ker f) + dim(Im f)**. Autrement dit, dimension du noyau + rang = dimension du départ.
3. rang(A) = 2, n = 4, donc n − rang(A) = **2 degrés de liberté** (si le système est compatible).
4. v ≠ 0 est vecteur propre pour la valeur propre λ si Av = λv. On trouve les vp en résolvant **det(A − λI) = 0**.
5. Le polynôme caractéristique est (3−λ)² = 0, donc λ = 3 est une vp double. L'espace propre E₃ = Ker(A−3I) = Ker([[0,1],[0,0]]) a dimension 1 < 2 = multiplicité. **A n'est pas diagonalisable** (elle est conjuguée à une matrice de Jordan [[3,1],[0,3]]).
6. Pour tout u, v ∈ E : **|⟨u, v⟩| ≤ ‖u‖·‖v‖**. Égalité ⟺ u et v sont colinéaires.
