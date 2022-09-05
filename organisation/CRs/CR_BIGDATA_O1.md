# CR - Réunion Team Big Data

## Réunion du 28/04/2022
Objectif : Définir l’intéret du chapitre, un plan détaillé de celui-ci et des objectifs de rédaction à court terme.

Renommer nom du chapitre (car pas en francais). Proposition : Big Data et Ingénierie des données.

Il s’agit d’un chapitre « périphérique » de IAZ  (pas au cœur de l’enseignement de l’IA) mais suffisamment important pour que les lecteurs s’y attardent, toujours dans un contexte fortement lié à l’IA (industrialisation de modèle, IA dans le Cloud, IA sur des technos distribuées, importance de la qualité des données etc …) 

## Idées générales sur le chapitre :

Première version du plan détaillée cohérente. Quelques ajustement à faire :

Aborder les sujets de manière contemporaine. Il y a un contexte à décrire, des problématiques à résoudre, des solutions à trouver. Présenter ces solutions, les limites et allez plus loin si nécessaire.
Partir sur « la donnée », l’or noir des entreprises comme base. Qu’est-ce qu’une donnée ? Pourquoi ca a de la valeur ? Comment mettre en place une gouvernance de données ? Quid de la qualité des données ?  Comment la « nettoyer » .La donnée est tout en haut de la pyramide + ramifications selon des problématiques concrètes et cas d’usage.

Se baser sur un seul langage : Python

Partir sur un cas d’usage fil rouge : Entreprise fictive, je suis Netflix. Implanté en Californie. L’infra de ma BDD a explosé car trop de données. 4 coins des Etats-Unis. Besoin de multiplier mes data centers. Outre Atlantique répliqua dans les data centers mondiaux….
- Permettra d’illustrer par l’exemple l’ensemble des notions abordées.
- Projet fil rouge à chaque thématique du chapitre (SQL, NO SQL, Algo distrib, Cloud, ML OPS)

## Idées en vrac sur le plan détaillé du chapitre :
1ère partie du chapitre très généraliste sur la définition et les enjeux/problématiques d’une « DATA » 
Qualité des données + Gouvernance des données + Pré-processing + RGPD : A aborder dans la 1ère partie du chapitre 
SQL - No SQL  - Partir sur un cas d’usage No SQL pour le fil rouge - Choix entre Cassandra, Neo4j, Mongo – La techno la plus utilisée…
Algos distribués - A quoi ca sert Spark ? ces points forts ? Cas d’usage pour le projet fil rouge sur du PySpark ?
Scala, Julia, … à citer en complément. 

Pour le Cloud : Interet ? C’est quoi ?  Low code, Azure, Amazon , Data Pipeline, Versionning
Lien avec le DevOPS & ETL : Déploiement infrastructure, Tagguer les fonctionnalités, Mise à échelle 
Lien avec le ML OPS : c’est du DEVOPS appliqué à la donné

## Plan détaillé

https://github.com/ia-z/ia-z/issues/52

## 1ère itération - A faire à court terme :
-	@Adrien : En charge de l’introduction du chapitre / la 1ère partie du Chapitre sur la définition et les caractéristiques d’une DATA
-	@CairOn : En charge des aspect BDD relationnelles  
