# 05 — Méthodologie en Psychologie
> Méthodes de recherche, Statistiques, Éthique

---

## 1. La démarche hypothético-déductive

### Étapes
```
Observation / Théorie
        ↓
   Hypothèse (H₀ / H₁)
        ↓
  Choix de la méthode
        ↓
  Collecte des données
        ↓
  Analyse statistique
        ↓
 Accepter / Rejeter H₀
        ↓
Conclusion & Publication
        ↓
     Réplication
```

### Hypothèse nulle et alternative
- **H₀** (hypothèse nulle) : pas d'effet, pas de différence
- **H₁** (hypothèse alternative) : il existe un effet
- On cherche à **rejeter H₀** avec suffisamment de preuves

---

## 2. Les méthodes de recherche

### 2.1 Méthode expérimentale

La seule qui permette d'établir des **relations causales**.

**Éléments clés** :
- **Variable indépendante (VI)** : manipulée par le chercheur
- **Variable dépendante (VD)** : mesurée
- **Variables confondantes** : contrôlées ou randomisées
- **Groupe expérimental** : reçoit le traitement
- **Groupe contrôle** : ne reçoit pas le traitement (ou reçoit le placebo)

**Exemple** :
> VI : type de mémorisation (relecture vs rappel actif)
> VD : score à un test 48h plus tard
> H₁ : le rappel actif améliore la mémorisation

**Types de plans expérimentaux** :
| Plan | Description | Avantage |
|---|---|---|
| Inter-groupes | Différents sujets par condition | Pas d'ordre, pas de pratique |
| Intra-sujet | Mêmes sujets dans toutes les conditions | Contrôle des différences individuelles |
| Mixte | Combinaison des deux | Flexibilité |

**Validité** :
- **Validité interne** : l'expérience mesure bien ce qu'elle prétend
- **Validité externe** : les résultats se généralisent à la vie réelle
- **Validité écologique** : le laboratoire reflète la réalité

### 2.2 Méthode corrélationnelle

Mesure la **relation** entre deux variables sans manipulation.

**Coefficient de corrélation r (Pearson)** :
- r ∈ [-1, +1]
- r = +1 : corrélation parfaite positive
- r = -1 : corrélation parfaite négative
- r = 0 : aucune corrélation
- |r| > 0.7 : fort ; 0.4–0.7 : modéré ; < 0.4 : faible

⚠️ **Corrélation ≠ causalité**
> « La consommation de glaces est corrélée aux noyades » → variable confondante : la chaleur

**Diagramme de dispersion (scatterplot)** :
- Visualiser la relation entre deux variables continues

### 2.3 Méthode observationnelle

Observation sans intervention dans le milieu naturel.

| Type | Description |
|---|---|
| **Naturaliste** | Observer dans l'environnement naturel (non intrusif) |
| **Participation** | Le chercheur s'immerge dans le groupe |
| **Structurée** | En laboratoire, avec comportements codifiés |

**Avantages** : validité écologique, comportements spontanés
**Limites** : pas de causalité, biais d'observation

### 2.4 Enquête (questionnaires et entretiens)

**Types d'entretiens** :
| Type | Description |
|---|---|
| Directif | Questions fermées, standardisées |
| Semi-directif | Guide de questions, liberté de réponse |
| Non directif | Libre expression autour d'un thème |

**Échelles de mesure** :
- **Likert** : de « Pas du tout d'accord » à « Tout à fait d'accord » (5 ou 7 points)
- **Différentiel sémantique** : entre deux adjectifs opposés (chaud–froid)
- **VAS** (Visual Analogue Scale) : ligne continue à marquer

**Biais de questionnaire** :
- Biais de désirabilité sociale : répondre ce qu'on croit attendu
- Biais de réponse acquiesçante : tendre à répondre « oui »
- Biais de rappel : mauvaise mémoire des événements passés
- Effet de halo : une question influence les suivantes

### 2.5 Étude de cas

Analyse approfondie d'un individu, d'un groupe ou d'un événement.

**Avantages** : richesse qualitative, génération d'hypothèses
**Limites** : non généralisable, biais du chercheur

**Exemples célèbres** :
- **H.M.** (amnésie antérograde) → modèles de mémoire
- **Phineas Gage** (lobe frontal) → fonctions exécutives
- **Genie** (isolement) → période critique pour le langage

### 2.6 Méta-analyse

Synthèse quantitative de plusieurs études sur un même sujet.

- Calcule un **effet moyen** (effect size)
- Identifie les modérateurs
- Puissance statistique maximale
- **Limites** : biais de publication (études positives surreprésentées)

---

## 3. Statistiques en psychologie

### 3.1 Statistiques descriptives

**Mesures de tendance centrale** :
| Mesure | Définition | Usage |
|---|---|---|
| **Moyenne** (μ, x̄) | Somme / n | Distribution normale |
| **Médiane** | Valeur centrale | Distributions asymétriques |
| **Mode** | Valeur la plus fréquente | Variables nominales |

**Mesures de dispersion** :
| Mesure | Définition |
|---|---|
| **Étendue** | Max − Min |
| **Variance** (σ²) | Moyenne des carrés des écarts à la moyenne |
| **Écart-type** (σ) | √Variance |
| **Intervalle interquartile (IQR)** | Q3 − Q1 |

**Distributions** :
- **Normale (Gaussienne)** : courbe en cloche, symétrique
  - 68% des données ± 1σ
  - 95% des données ± 2σ
  - 99.7% des données ± 3σ
- **Asymétrie positive** : queue à droite (revenus)
- **Asymétrie négative** : queue à gauche (notes d'un bon étudiant)

### 3.2 Statistiques inférentielles

**Tests statistiques courants** :
| Test | Usage |
|---|---|
| **t de Student** | Comparer 2 moyennes |
| **ANOVA** | Comparer ≥ 3 moyennes |
| **Chi² (χ²)** | Variables catégorielles |
| **Corrélation de Pearson** | Relation entre 2 variables continues |
| **Régression linéaire** | Prédire une variable à partir d'une autre |
| **Mann-Whitney U** | Non paramétrique, 2 groupes |
| **Kruskal-Wallis** | Non paramétrique, ≥ 3 groupes |

### 3.3 La valeur p et le seuil de significativité

**p-value** : probabilité d'obtenir les résultats observés si H₀ est vraie.

- **p < .05** : significatif (convention historique)
- **p < .01** : très significatif
- **p < .001** : hautement significatif

⚠️ **Erreurs statistiques** :
| Erreur | Description |
|---|---|
| **Erreur de type I (α)** | Rejeter H₀ à tort (faux positif) |
| **Erreur de type II (β)** | Accepter H₀ à tort (faux négatif) |
| **Puissance (1-β)** | Probabilité de détecter un vrai effet |

### 3.4 Taille de l'effet (Effect Size)

La p-value ne dit pas **combien** l'effet est important.

| Mesure | Petite | Moyenne | Grande |
|---|---|---|---|
| **d de Cohen** | 0.2 | 0.5 | 0.8 |
| **r** | 0.1 | 0.3 | 0.5 |
| **η²** | 0.01 | 0.06 | 0.14 |

### 3.5 Crise de réplication

> De nombreuses études classiques ne se répliquent pas.

- **Open Science Collaboration (2015)** : seulement 36% des études de psychologie sociale répliquées
- Causes : p-hacking, HARKing (Hypothesizing After Results Known), faibles tailles d'effet, petits échantillons
- Solutions : préenregistrement des études, open data, open materials

---

## 4. Éthique en recherche

### 4.1 Principes fondamentaux (APA, 2017)

| Principe | Description |
|---|---|
| **Bienfaisance** | Maximiser le bien-être des participants |
| **Non-malfaisance** | Ne pas nuire |
| **Autonomie** | Respecter la liberté de choix |
| **Justice** | Équité dans la distribution des bénéfices et risques |

### 4.2 Consentement éclairé

Le participant doit :
- Être informé des objectifs et procédures
- Comprendre les risques et bénéfices potentiels
- Accepter librement (sans contrainte)
- Pouvoir se retirer à tout moment sans pénalité

**Exceptions** :
- Observation naturaliste dans des lieux publics
- Recherches impliquant une tromperie (débriefer obligatoire après)

### 4.3 Tromperie en recherche
Parfois nécessaire (ex : Milgram). Conditions :
- Aucun autre moyen d'étudier le phénomène
- Aucun préjudice grave anticipé
- **Débriefer complet** après l'étude

### 4.4 Confidentialité et anonymat
- Données anonymisées ou pseudonymisées
- Stockage sécurisé, accès limité
- RGPD (Règlement Général sur la Protection des Données)

### 4.5 Comités d'éthique
Toute recherche sur des êtres humains doit être approuvée par un **comité d'éthique institutionnel** (CPP en France, IRB aux USA).

---

## 5. Rédiger un rapport de recherche

### Structure IMRaD
| Section | Contenu |
|---|---|
| **Introduction** | Contexte, revue de littérature, hypothèses |
| **Méthode** | Participants, matériel, procédure |
| **Résultats** | Statistiques descriptives et inférentielles, figures |
| **Discussion** | Interprétation, limites, perspectives |
| **Références** | Format APA |

### Format APA (7e édition) — Références

**Article** :
> Auteur, A. A., & Auteur, B. B. (Année). Titre de l'article. *Nom de la revue*, *volume*(numéro), pages. https://doi.org/

**Livre** :
> Auteur, A. A. (Année). *Titre du livre*. Éditeur.

**Statistiques dans le texte** :
> *t*(58) = 2.43, *p* = .018, *d* = 0.62

---

## 6. Révisions

### Questions de cours
1. Quelle est la différence entre méthode expérimentale et corrélationnelle ?
2. Définissez VI et VD avec un exemple.
3. Qu'est-ce que la valeur p ? Quel est le seuil conventionnel ?
4. Expliquez les erreurs de type I et II.
5. Quelles sont les conditions du consentement éclairé ?
6. Pourquoi la taille de l'effet est-elle plus informative que la p-value ?

### Réponses clés
1. Expérimentale : manipulation de la VI → causalité. Corrélationnelle : mesure de deux variables → relation, pas causalité.
2. VI = ce que le chercheur manipule (ex : type d'étude : relecture vs rappel). VD = ce qu'on mesure (ex : score au test). Les changements de VI expliquent les variations de la VD.
3. Probabilité d'observer les résultats si H₀ est vraie. Seuil : p < .05 (5% de risque d'erreur de type I).
4. Type I (α) : rejeter H₀ à tort (faux positif). Type II (β) : ne pas rejeter H₀ alors qu'elle est fausse (faux négatif). La puissance (1-β) est la probabilité de détecter un vrai effet.
5. Information complète, compréhension, liberté (pas de contrainte), droit de retrait à tout moment.
6. La p-value indique si l'effet existe ; la taille de l'effet (Cohen's d, r) dit combien il est important. Un p < .05 avec d = 0.01 est statistiquement significatif mais sans intérêt pratique.
