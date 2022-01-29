# Feature Engineering
1. [Introduction](#introduction)
2. [Methodologie](#methodologie)
3. [Terminologie](#terminologie)
4. [Nettoyage des données](#nettoyage)
    1. [Valeurs manquantes](#subparagraph1)
    2. [Valeurs aberrantes](#subparagraph2)
    3. [Valeurs rares](#subparagraph3)
    4. [Haute cardinalité](#subparagraph4)
5. [Feature Scaling](#featurescaling)
6. [Feature encoding](#featureencoding)


## Introduction <a name="introduction"></a>

Le feature engineering représente l’art de convertir les données de la meilleure façon possible, ce qui implique une combinaison d'expertise du domaine, d'intuitions et de procédés mathématiques. Ce cours a pour objectif d’être une référence concise pour les débutants avec la plupart des techniques simples mais largement utilisées pour cette approche.

Le feature engineering est la partie la plus essentielle de la construction d'un projet de machine learning. Des centaines d'algorithmes à l’état de l’art apparaissent aujourd'hui à travers différentes thématiques, comme le transfer learning ou le Deep Leaning. Au bout du compte, certains projets réussissent et d'autres échouent. Qu'est-ce qui fait la différence entre ces approches ? Le facteur le plus important est sans aucun doute la qualité des données et les features utilisées.

## Methodologie <a name="methodologie"></a>

Voici une pipeline typique d’un projet de Machine Learning 

![pipeline](map_feat_eng.png)

Supposons que vous êtes Data Scientists pour une entreprise data-centric. Votre manager vous demande d’atteindre une performance précise pour un modèle donné. Après avoir minutieusement étudier les données à votre disposition en ayant effectuer une EDA digne de ce nom, vous décidez de vous lancer dans cette étape de préparation des données puis d'utiliser votre modèle favori. Néannmoins vous constater que les performances de votre modèle sont bien plus basses que prévues et vous craignez de perdre votre poste ! Pas de panique ! Pour résoudre ce problème, on réitère l’étape n°6 tant que les objectifs de performances du modèle donnés par votre N+1 ne sont pas atteints.

La qualité des données et des features ont le plus d'impact sur un projet de Machine Learning et fixent la limite de ce que vous pouvez faire. La qualité de vos prédictions et le bien fondé de votre approche repose essentiellement sur ces aspects. 

Avant toutes choses, attardons-nous quelques instants sur les notions importantes à avoir en tête tout au long de cet article.

## Terminologie <a name="terminologie"></a>

*Feature* : également appelée attribut/variable indépendante/variable d'entrée. Il s'agit d'une propriété/caractéristique individuelle mesurable d'un phénomène observé. Par exemple, la taille d’une personne, son âge.

*Target* : également connue sous le nom de variable dépendante/ variable de réponse/ variable de sortie. C'est la variable à prédire dans l'apprentissage supervisé.

*Algorithme* : la procédure spécifique utilisée pour mettre en œuvre une technique de Machine Learning particulière que vous retrouverez dans les autres parties du cours.

*Modèle* : l'algorithme appliqué à un ensemble de données, avec ses paramètres. L’objectif est d’obtenir le modèle qui capture le mieux la relation entre les features et la target.

## Nettoyage des données<a name="nettoyage"></a>

L’étape préalable au feature engineering consiste au nettoyage des données. Celle-ci repose sur différents aspects importants que nous aborderons dans cette partie.

## Valeurs manquantes <a name="subparagraph1"></a>

Définition : Aucune valeur n'est enregistrée dans une certaine observation pour une variable donnée.

*Pourquoi les données manquantes sont-elles importantes ?*

Certains algorithmes ne peuvent pas fonctionner en présence de valeurs manquantes
même pour les algorithmes qui traitent les données manquantes, sans traitement, le modèle peut conduire à des prédictions inexactes.

Une étude sur l'impact des données manquantes sur différents algorithmes Machine Learning peut être trouvée ici [link](https://core.ecu.edu/krosj/IMDSDataMining2003.pdf).

## Valeurs aberrantes <a name="subparagraph2"></a>

Définition : Une observation aberrante est une observation qui s'écarte tellement des autres observations que l'on peut soupçonner qu'elle a été générée par un mécanisme différent.

Les observations aberrantes, selon le contexte, méritent une attention particulière ou doivent être complètement ignorées. Par exemple, une transaction inhabituelle sur une carte de crédit est généralement le signe d'une activité frauduleuse, tandis qu'une taille de 1600 cm d'une personne est très probablement due à une erreur de mesure et doit être filtrée ou imputée par autre chose.

*Pourquoi la valeur aberrante est-elle importante ?*

La présence de valeurs aberrantes peut :

- Empêcher l'algorithme de fonctionner correctement
- Introduire des bruits dans l'ensemble de données
- Rendre les échantillons moins représentatifs

Certains algorithmes sont très sensibles aux valeurs aberrantes. 
Par exemple, Adaboost peut traiter les valeurs aberrantes comme des cas "difficiles" et leur accorder un poids considérable, ce qui produit un modèle à mauvaise généralisation. 
Tous les algorithmes qui reposent sur les moyennes/variances sont sensibles aux valeurs aberrantes, car ces statistiques sont fortement influencées par les valeurs extrêmes.

D'autre part, certains algorithmes sont plus robustes aux valeurs aberrantes. Par exemple, les arbres de décision ont tendance à ignorer la présence de valeurs aberrantes lorsqu'ils créent les branches de leurs arbres. En général, les arbres effectuent des séparations en demandant si la variable x >= la valeur c, et donc la valeur aberrante tombera de chaque côté de la branche, mais elle sera traitée de la même manière que les autres valeurs, quelle que soit son ampleur.

## Valeurs rares <a name="subparagraph3"></a>

Définition : Variable catégorielle dont certaines valeurs n'apparaissent que rarement.

Dans certaines situations, les valeurs rares, comme les valeurs aberrantes, peuvent contenir des informations précieuses sur l'ensemble de données et nécessitent donc une attention particulière. Par exemple, une valeur rare dans une transaction peut indiquer une fraude.

*Pourquoi les valeurs rares sont-elles importantes ?*

Les valeurs rares dans les variables catégorielles ont tendance à provoquer un surajustement.
Un grand nombre de labels peu fréquents ajoute du bruit, avec peu d'informations, ce qui entraîne un ajustement excessif aux données.
Les labels rares peuvent être présents dans l'ensemble d'apprentissage, mais pas dans l'ensemble de test, ce qui entraîne un ajustement excessif de l'ensemble d'apprentissage.

Les labels rares peuvent apparaître dans l'ensemble de test, mais pas dans l'ensemble d'entraînement. Ainsi, le modèle ne saura pas comment l'évaluer.

## Haute cardinalité <a name="subparagraph4"></a>

Définition : Le nombre de labels au sein d'une variable catégorielle est appelé cardinalité. Un nombre élevé de labels au sein d'une variable est connu comme une cardinalité élevée.

*Pourquoi une cardinalité élevée est-elle importante ?*

Les variables comportant trop de labels ont tendance à dominer celles qui n'en comportent que quelques-unes, en particulier dans les algorithmes basés sur des arbres.
Un grand nombre de labels dans une variable peut introduire du bruit avec peu ou pas d'informations, ce qui rend les modèles d'apprentissage automatique susceptibles d'être surajustés.

Certains labels peuvent n'être présentes que dans l'ensemble de données d'apprentissage, mais pas dans l'ensemble de test, ce qui entraîne une suradaptation des algorithmes à l'ensemble d'apprentissage.

À l'inverse, de nouveaux labels peuvent apparaître dans l'ensemble de test alors qu'elles n'étaient pas présentes dans l'ensemble d'apprentissage, ce qui empêche l'algorithme d'effectuer un calcul sur la nouvelle observation.

## Feature Scaling <a name="featurescaling"></a>

Définition : Le feature scaling est une méthode utilisée pour normaliser des variables indépendantes ou des features. Dans le traitement des données, elle est également connue sous le nom de normalisation des données et est effectuée durant l'étape de prétraitement des données.

*Pourquoi le Feature Scaling est-elle importante ?*

- Si la taille des entrées varie, dans certains algorithmes, vous pouvez obtenir des résultats incohérents

- La descente de gradient converge beaucoup plus rapidement lorsque la normalisation à l'échelle des features est effectuée. La descente de gradient est un algorithme d'optimisation communément utilisé dans la régression logistique, les SVM, les réseaux neuronaux, etc. qui a été introduite précédemment. 

*Comment gérer le Feature Scaling ?*

- La normalisation (mise à l'échelle du score Z) supprime la moyenne et met les données à l'échelle de la variance unitaire.
$z = (X - X_{mean}) / std$

    La feature est remise à l'échelle pour avoir une distribution normale standard centrée autour de 0 avec un écart type de 1. 

    Si la variable est asymétrique ou comporte des valeurs aberrantes, cela comprime les observations dans une plage étroite, ce qui nuit au pouvoir prédictif.

- Scaling Min-Max transforme les features en mettant à l'échelle chaque feature dans une plage donnée. 

    La valeur par défaut est $[0,1]$.

    $X_{scaled} = (X - X_{min}/(X_{max} - X_{min})$  compresse les observations dans la plage étroite si la variable est asymétrique ou comporte des valeurs aberrantes.

Comme nous pouvons le voir, la normalisation - standardisation et la méthode Min-Max comprimeront la plupart des données dans une plage étroite. 

La suppression/imputation des valeurs aberrantes est un autre sujet du nettoyage des données qui doit être effectuée au préalable de cette étape.

## Feature encoding <a name="featureencoding"></a>

*Pourquoi le Feature encoding est-il important ?*

Nous devons transformer les strings ou les variables catégorielles en nombres pour que les algorithmes puissent traiter ces valeurs. Même si vous voyez qu'un algorithme peut prendre en charge des entrées catégorielles, il est très probable que l'algorithme intègre ce processus de feature encoding.

**One-hot Encoding** : Remplace la variable catégorielle par différentes variables booléennes (0/1) pour indiquer si un certain label est vrai ou faux pour une observation donnée. 

Cette méthode permet de conserver toutes les informations de cette variable. 

Néanmoins, elle présente deux défauts : 

- elle élargir considérablement l'espace des features si trop de labels sont présents au sein de cette variable.

- n'ajoute pas de valeur supplémentaire pour rendre la variable plus prédictive.


**Count/frequency encoding** : Remplace chaque label de la variable catégorielle par le nombre/fréquence dans cette catégorie 

Cette méthode présent un défaut : 

- permet d'attribuer le même encodage pour deux labels différentes (si elles apparaissent en même temps, avec le même nombre d'occurences) et perd des informations précieuses.
