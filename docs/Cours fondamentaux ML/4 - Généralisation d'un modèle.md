# Généralisation d'un modèle de Machine Learning
Un des concepts important lors de l'entraînement d'un modèle est
sa capacité à généraliser.

Nous allons ici voir quels sont les enjeux dont on parle lorsque
l'on parle de généralisation, et comment l'évaluer.

## Le besoin de généraliser
Dans le schéma classique d'un apprentissage supervisé, vous voudrez un modèle capable
de prédire une certaine valeur `y` à partir d'un ensemble de valeurs `X`.

Pour qu'un tel modèle soit utile, il faut qu'il soit capable de donner une bonne solution (approximative)
pour des données jamais observées. En effet, à quoi bon utiliser un modèle sur des données où l'on a déjà
collecté et mesuré la valeur de `y` !

Pendant l'entraînement d'un modèle, on mesure souvent sa performance sur le jeu de données utilisé pendant l'entraînement.
Cela revient à demander à un étudiant s'il est bien capable de refaire de tête des exercices où on lui a donné
la correction auparavant.
Comment faire pour s'assurer qu'il est capable de réussir la plupart des exercices ?

*On s'entends bien ici que l'on veut que l'étudiant réussisse des exercices qui sont bien du même cours que ceux
sur lesquels il s'entraîne. Pour que l'analogie avec un modèle de ML fonctionne, il faudrait donc le soumettre à
de nouvelles données qui sont issues de la même distribution.*

## Définitions
### Overfitting
L'overfitting, ou sur-apprentissage en français, est le résultat d'un modèle qui a "trop appris". Il est parfaitement
capable de prédire la bonne solution pour un exemple utilisé pour l'entraîné, mais il devient tout d'un coup très mauvais
lorsqu'on l'évalue sur une toute nouvelle donnée.

Dans le cas de notre étudiant, à force d'entraînement sur les quelques exercices fournis, il aura fini par remarquer
certaines astuces qui permettent de court-circuiter des questions afin d'être plus performant. Mais ces astuces
peuvent se révéler n'être que des coïncidences qui fonctionnent bien sur les quelques exercices mais qui sont en fait fausses.
L'utilisation de ces fausses corrélations s'avère alors dévastateur lors de l'évaluation sur de nouveaux exercices !

On parle alors de sur-entraînement. La machine a détecté des corrélations qui semblent utiles sur le jeu d'entraînement,
mais elles sont en fait de fausses corrélations qui n'expliquent en rien la relation entre `X` et `y`.
Cela arrive très souvent, et c'est la hantise de toute personne travaillant dans le ML.

### Underfitting
### Généralisation d'un modèle

## Exemples
Exemple simple : générer des données y = x^2.

### Overfitting
Regression polynomiale avec un degré supérieur à 2.

### Underfitting
Regression linaire.

### Généralisation
Regression polynomiale de degré 2.

## Évaluer la généralisation d'un modèle
On a donc besoin d'évaluer le pouvoir de généralisation de nos modèles.
En fait on peut voir sur les exemples précédents que le meilleur moyen de détecter un mauvais comportement du modèle est de le
tester sur des données qu'il n'a jamais vues auparavant. Le plus simple est donc de diviser les données en deux groupes :

* **Données d'entraînement**
* **Données de test**

Le premier jeu de données est utilisé pour entraîner le modèle, le second pour évaluer la capacité du modèle à généraliser à de nouveaux exemples.

### Train/Test
Il est donc tout le temps obligatoire de diviser les données en ces deux catégories. En anglais, on parle de **training dataset** et **testing dataset**.
Le jeu de test doit être représentatif de la distribution des données réelle. En général, on mélange toutes nos données et on en tire au hasard 20%
qui constitueront notre jeu de test.

C'est sur le jeu de test que les performances finales du modèle peuvent être déduites. On n'utilises jamais les métriques sur le jeu d'entraînement
comme métriques finales d'un modèle.

## La recherche d'hyperparamètres

*Présentation des hyperparamètres ?*

Vous venez d'entraîner un modèle, vous l'évaluer alors sur le jeu de test et vous observez des performances décevantes. Vous pensez pouvoir
l'améliorer en modifiant quelques hyperparamètres. Ainsi, vous vous mettez à faire plusieurs aller-retours entre l'évaluation du modèle sur le jeu de test
et l'entraînement jusqu'à atteindre ce que vous pensez être les meilleures performances atteignables par le modèle.

Oui mais voilà, à force de régler vos hyperparamètres grâce au jeu de test, vous êtes en train indirectement d'optimiser le modèle sur les données de test.
Cela revient à un étudiant de remarquer petit à petit que certaines techniques fonctionnent particulièrement bien sur le jeu de test. En fait, il est
en train d'overfit sur le jeu de test.

De manière générale, **il faut éviter au maximum de faire fuiter les informations contenues par le jeu de test dans l'entraînement de nos modèles.**
Il faut le garder uniquement pour l'évaluation finale de notre modèle, une fois que l'on a fixé nos hyperparamètres.

### Train/Val/Test
Alors comment sélectionner nos hyperparamètres ? On utilise un troisième de jeu de données : le **jeu de données de validation**.
C'est avec ce **validation dataset** que vous allez régler (*fine-tune*) les hyperparamètres de votre modèle.
Ce jeu de données est tiré au hasard parmi vos données de la même façon que vous avez créer votre jeu de test.

En général, voici comment je m'occupe de mes données pour créer les datasets :

* **Données initiales** (*100%*):

    * Données de test (*20%*)
    * Données restantes (*80%*):

        * Données de validation (*20%*)
        * Données d'entraînement (*80%*)

*Diagramme avec des patates est probablement mieux*

## Détails supplémentaires
Chaque paramètre doit être entraîné uniquement à l'aide du jeu d'entraînement. Ainsi, même lors du preprocessing de vos données,
vous devez faire en sorte que tout information utilisée doit provenir du jeu d'entraînement uniquement. Par exemple, si vous
décidez de normaliser vos données selon une loi normale, vous devez utiliser la moyenne et l'écart-type du jeu d'entraînement
pour normaliser toutes vos données. Une erreur classique serait d'utiliser la moyenne et l'écart-type de chaque jeu de données pour la normalisation.

## Conclusion
Nous avons besoin de s'assurer qu'un modèle généralise bien. Il est toujours possible de trouver des corrélations statistiques
(voir `Spurious Correlations`) dans les données d'entraînement qui semblent expliquer les quelques détails qui améliorent les performances des prédictions.
Or ces petites coïcidences ne permettent pas d'expliquer la relation entre `X` et `y`.

Dans le meilleur des mondes, nous n'aurions pas besoin d'évaluer la généralisation d'un modèle si nous possédions toutes les données possibles et imaginables pour
la tâche considérée. Mais c'est malheureusement impossible (*et cela rendrait d'ailleurs le ML beaucoup moins utile*), il faut donc s'assurer l'utilité du modèle
une fois hors de l'entraînement.

Enfin, il est intéressant que nous évaluons ici la généralisation d'un modèle sur son domaine de distribution. Sachez qu'il existe
toute une branche de l'IA qui se concentre sur la capacité des modèles à généraliser sur d'autres domaines que celui utilisé pour l'entraînement.
On parle alors de *généralisation Out-of-Distribution*.

## Pour aller plus loin
L'optimisation de modèles de séries temporelles demande des précautions supplémentaires. On divise les données sur l'axe temporel, de sorte à avoir les données
de test dans le futur par rapport aux données d'entraînement et de validation.

## Sources
https://tylervigen.com/spurious-correlations
https://out-of-distribution-generalization.com/
