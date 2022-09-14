# Éléments de définition
À l’intersection des statistiques et de l’informatique, le machine learning se préoccupe de la modélisation des données.
Les grands principes de ce domaine ont émergé des statistiques fréquentistes et bayésiennes, de l’intelligence artificielle ou encore du traitement du signal.
Le machine learning est la science de l’apprentissage automatique d’une fonction prédictive à partir d’un jeu d’observations de données étiquetées ou non.

Ce chapitre se veut une **introduction aux concepts et aux premières définitions qui fondent le machine learning**, et en propose plusieurs approches, décrites et illustrées.

## Donnée, jeu de données et caractéristiques
Une `donnée` est une quantité ou une observation mesurable.
Cela peut être la taille d'un individu, une image, du texte... À peu près n'importe quoi !

On peut récolter plusieurs données et les regrouper dans un jeu de données afin d'en étudier le fonctionnement d'un phénomène que l'on souhaiterai caractériser.
Par exemple, on pourrait mesurer la taille des adultes en France et regrouper ces mesures dans un `jeu de données` (*dataset* en anglais).
On dit alors que les données sont des `exemples` du dataset (ou *sample* en anglais).

Traditionnellement, on visualise un dataset à l'aide d'un tableau où les lignes sont les différents exemples et les colonnes sont les différentes mesures récupérées sur chaque exemple.

| Individu ID 	| Taille 	| Couleur des cheveux 	| Couleur des yeux 	|
|-------------	|--------	|---------------------	|------------------	|
| 1           	| 1.75   	| Brun                	| Marron           	|
| 2           	| 1.92   	| Blond               	| Bleu             	|
| ...         	|        	|                     	|                  	|

Comme vous le voyez, il est possible de récolter plusieurs données pour un même individu.
Lorsqu'un exemple a plusieurs données attribuées, on parle alors de ses données comme de ses `caractéristiques` (*features* en anglais).
On dit que les exemples sont de dimension 3 dans notre cas, car ils ont 3 caractéristiques.
Dans le cas d'une image de 64x64 pixels, cette image peut être considéré comme un exemple avec 4096 caractéristiques !

## Le jeu de données : la source de connaissances
En machine learning, tout part d'un jeu de données.
Les données sont la clef de la connaissance, elles sont une image du fonctionnement du monde au moment où elles ont été récoltées.
Voici quelques petits exemples pour illustrer l'utilité des données :
* Mesurer la trajectoire d'un lancer de balle dans l'espace permet de mieux comprendre le fonctionnement de la gravité.
* Lire l'ensemble des livres du XVIIe siècle permet de mieux comprendre comment s'exprimaient les populations de cette époque.
* Comparer les achats de tous les clients d'un site marchand permet de mieux sélectionner les items à recommander aux futurs clients.

A travers les données, on peut déceler des comportements statistiques intéressants et en tirer de l'information.
**L'objectif du machine learning est d'extraire les connaissances contenues dans un jeu de données et de les synthétiser au sein d'un modèle.**

Cependant, attention à ne pas tirer de conclusions hatives à partir d'un jeu de données.
Les données ne sont pas neutres par essence.
La façon dont elles ont été récoltées, le contexte, et des données manquantes externes peuvent totalement altérer l'information que vous avez extrait d'un jeu de données.
Ainsi, des biais statistiques peuvent être insérés et pointer vers des conclusions dramatiquement fausses.
Par exemple, on pourrait se dire que le chocolat rend plus intelligent car la plupart des personnes ayant reçu un prix nobel en [consomment](https://www.youtube.com/watch?v=z_cACapt3Hc).
Cependant, c'est oublié le facteur important ici : les pays les plus riches sont à la fois ceux qui investissent le plus dans la recherche et aussi ceux qui ont le plus accès au chocolat.

## Le modèle : la synthèse des connaissances
Une fois les données récoltées, on souhaite généralement traduire les informations qui nous intéressent en un `modèle`.
**Le modèle synthétise les connaissances contenues dans le jeu de données.**
Il exprime mathématiquement les relations du dataset, sous forme de fonction.
Pour revenir sur les exemples précédents, un modèle :
* Caractérise l'évolution de la position d'une balle après son lancer.
* Capture la distribution de probabilité que suivent les mots de la langue française du XVIIe.
* Regroupe les items d'un site marchand qui sont achetés par les mêmes catégories de personnes.

Le modèle permet d'expliquer les données.
Il n'a pas à être parfait *(et il ne l'est jamais en pratique)*, mais on espère qu'il sera suffisamment bon pour mieux comprendre les relations qu'il caractérise ou simplement pour nous être utile pour la tâche souhaitée.

## Tâches classiques résolues avec le ML
Nous pouvons maintenant nous intéresser aux différentes tâches classiques résolues à l'aide du ML.
On va uniquement regarder les grandes familles de problèmes et donner quelques exemples pour chacune d'entre elles.

### Classification
Le but d'une tâche de classification est de **déterminer la classe** des exemples d'un dataset.
Par exemple, on souhaite faire un modèle qui est capable de prédire si un mail est frauduleux ou pas.
Dans ce cas, nous aurons besoin d'un ensemble de mails avec des informations sur le contenu du mail ainsi que sur son envoyeur et la classe du mail (« frauduleux » ou « non frauduleux »).
Dans ce type d'exemples, on parle classification binaire car il y a uniquement deux classes.

Il existe de nombreux types de tâches de classification que vous pouvez rencontrer dans l'apprentissage automatique et des approches spécialisées de la modélisation qui peuvent être utilisées pour chacune.
Ces approches seront étudiées plus en détail à la suite du cours.

### Régression
Dans le domaine de l'apprentissage statistique, la régression permet d'**approcher une variable quantitative**.
La régression s'articule autour d'algorithmes simples, qui sont souvent utilisés dans la finance, l'investissement et autres, et établit la relation entre une seule variable dépendante de plusieurs variables.
Prédire le nombre de clics sur un lien ou prédire le rendement d’un plant de maïs sont des exemples de regression classiques.

![image](https://user-images.githubusercontent.com/55838700/157339195-b7585660-1e87-467c-8eb5-b589f493f9d1.png)

Le modèle de régression le plus connu est la de régression linéaire.

### Classification vs Regression
La différence la plus significative entre la régression et la classification est que si la régression aide à prédire une quantité continue, la classification prédit des étiquettes de classe discrètes.
Il existe également des similitudes entre les deux types d'algorithmes d'apprentissage automatique.
* Un algorithme de *régression* peut prédire une valeur discrète qui se présente sous la forme d'une quantité entière.
* Un algorithme de *classification* peut prédire une valeur continue si elle se présente sous la forme d'une probabilité d'étiquette de classe.

Considérons un ensemble de données contenant des informations sur les étudiants d'une université particulière.
Un algorithme de régression peut être utilisé dans ce cas pour prédire la taille de tout élève en fonction de son poids, de son sexe, de son régime alimentaire ou de sa matière principale.
Nous utilisons la régression dans ce cas car la hauteur est une *quantité continue*.
Il existe un nombre infini de valeurs possibles pour la taille d'une personne.

Au contraire, la classification peut être utilisée pour analyser si un e-mail est un spam ou non.
L'algorithme vérifie les mots-clés dans un e-mail et l'adresse de l'expéditeur est essaie de déterminer la probabilité que l'e-mail soit un spam.
De même, alors qu'un modèle de régression peut être utilisé pour prédire la température du lendemain, nous pouvons utiliser un algorithme de classification pour déterminer s'il fera froid ou chaud en fonction des valeurs de température données.

![Capture](https://miro.medium.com/max/1400/1*wH09k0DhF4JQhVMymtVQHQ.jpeg)

Comprendre la différence entre les algorithmes de régression et de classification peut vous aider à appliquer les concepts d'apprentissage automatique de manière plus précise.
Certains algorithmes peuvent nécessiter à la fois des approches de classification et de régression, c'est pourquoi une connaissance approfondie des deux est cruciale.

### Clustering
Le problème d’apprentissage non supervisé le plus fréquent est le problème de partitionnement de données (en anglais *clustering*).
C’est l’étape où l’on essaie de **séparer les données en groupes**.
C’est la pierre angulaire de l’apprentissage non supervisé.
C’est à la fois sa plus grande contrainte et sa plus grande force.
C’est ce qui fait que l’on fait le parallèle entre l’apprentissage non supervisé et la façon humaine de raisonner puisque l’intelligence artificielle est alors autonome.
Il n’y a pas besoin d’intervention humaine préalable pour créer les catégories, ce qui est exactement le cas pour les humains !
On a appris nous-mêmes à distinguer les objets que l’on voit, à savoir que tel animal est un lapin ou un chat par exemple !

![Capture](https://user.oc-static.com/upload/2017/05/12/14946001500306_P3C1-2.png)

Le clustering permet d'identifier des groupes homogènes parmi une population donnée.

### Association
La recherche des règles d’association est une méthode dont le but est de découvrir des relations ayant un intérêt entre deux ou plusieurs variables stockées dans de très importantes bases de données.
Les algorithmes d’association sont particulièrement adaptés pour explorer des bases de données volumineuses ou complexes.
Par exemple, ils peuvent identifier la probabilité de co-occurrence d’éléments dans une collection de données.

Quelques exemples:
* Association entre alimentation et apparition de maladies.
* Association entre génotype et phénotype.
* Association entre activations de neurones et comportement.

### Réduction de dimensions
Un second cas d’apprentissage non supervisé concerne la réduction de dimensions. 
Il  désigne ainsi toute méthode permettant de projeter des données issues d’un espace de grande dimension dans un espace de plus petite dimension.
Cette opération est cruciale en apprentissage automatique pour lutter contre ce qu’on appelle le fléau des grandes dimensions (le fait que les grandes dimensions altèrent l’efficacité des méthodes).

![image](https://user-images.githubusercontent.com/55838700/157340186-6cc1e49f-f2db-4560-8e66-aba94282d054.png)

On emploie ici le mot « dimension » au sens algébrique, i.e. la dimension de l’espace vectoriel sous-jacent aux valeurs des vecteurs de descripteurs.
La réduction de dimensionnalité permet de réduire la complexité d’un problème d’apprentissage automatique à plusieurs niveaux :
* D’un point de vue **théorique**, cela entraîne automatiquement une amélioration des propriétés de stabilité et de robustesse des algorithmes.
* D’un point de vue **pratique**, cela simplifie la résolution du problème d’optimisation associé, en réduisant l’espace des solutions.

En d’autres termes, réduire la dimensionnalité limite le nombre de possibilités à tester, ce qui permet de traiter les données plus rapidement.
Ce gain de temps est fonction de la dépendance de la complexité temporelle de l’algorithme par rapport à la dimension.

## Apprentissage automatique
On sait que le but du ML est de produire un modèle qui capture les relations d'un dataset.
Pour y arriver, on dit que l'on `entraîne` un modèle sur un jeu de données, à l'aide d'un `algorithme d'apprentissage automatique` (*Machine Learning algorithm*).

Le domaine du ML regroupe beaucoup de modèles et d'algorithmes différents dans le but de couvrir un maximum de datasets possibles.
Connaître les cas d'applications de chaque modèle et algorithme d'apprentissage est un bon moyen pour rapidement déployer des solutions à un problème donné.

Afin de bien apprendre, un modèle a besoin de beaucoup de données.
C'est pourquoi il est courant de rencontrer des modèles entraînés à partir de millions d'images ou de documents.
Plus un dataset contient d'exemples divers et plus il sera possible de modéliser des relations complexes entre nos données.

### Apprentissage supervisé
Avec l’apprentissage supervisé, le modèle est entraîné à reproduire une sortie donnée.
Par exemple, il peut apprendre à distinguer les photos de chien et de chat après qu’on lui ait montré des milliers de photos des deux catégories et en précisant pour chaque image à quelle catégorie elle appartient.
Ou bien, il peut apprendre à traduire le français en chinois après avoir vu des centaines de milliers d’exemples de traduction français-chinois. 

Concrètement, on a un dataset $\mathcal{D} = (x_i, y_i)_1^N$ de $N$ couples où $x_i$ est un ensemble de `caractéristiques` (*features*) et $y$ l'`étiquette` (*label*) correspondante.
En reprenant l'exemple précédent, un $x_i$ pourrait être les pixels d'une image de chien et $y_i$ la catégorie chien.
On entraîne alors un modèle $f$ tel que $f(x) \approx y$.

![Capture](https://machinelearnia.com/wp-content/uploads/2019/06/apprentissage-supervise-2-.png)

Dans le cadre de l’apprentissage supervisé, la machine connaît déjà les réponses qu’on attend d’elle.
Elle travaille à partir de données étiquetées.
Reprenons l’exemple d’une application destinée à reconnaître les chiens et les chats.
Pour l’entraîner, on lui présente des images étiquetés comme « chien » ou « chat ».
Par des techniques issues des statistiques et des probabilités, l’algorithme comprend alors quelles sont les caractéristiques qui permettent de classer ces images dans chacune des catégories.
Ainsi, au fur et à mesure qu’on lui présentera de nouvelles images, il pourra les identifier, en donnant un score de probabilité.

### Apprentissage non supervisé
Qu’est-ce que l’apprentissage non supervisé ?
C’est de l’apprentissage sans superviseur, tout simplement… 😊
Plus sérieusement, l’apprentissage non supervisé consiste à apprendre à un modèle des informations *sans l'aide d'étiquettes*, c’est-à-dire sans superviseur (d’où le nom, vous l’aurez compris).

Néanmoins, ce n’est pas parce que l’on parle d’apprentissage non supervisé que l’on doit omettre la notion de catégories pour les algorithmes de classification.
Un algorithme d’apprentissage non supervisé utilise des catégories associées aux données qu’on lui soumet, mais il doit les faire émerger lui-même, afin, par exemple, de reconnaître qu’un chat est un chat.

![image](https://user-images.githubusercontent.com/55838700/157058262-55717286-3591-41d5-8e55-27375f1c2389.png)

En apprentissage supervisé on fournit des milliers d’images de chiens à l’algorithme avec le label ’chien’.
De cette manière, si on lui fournit une autre image quelconque il pourra déterminer si elle représente un chat ou pas.
En apprentissage non supervisé, **aucun label n’est fourni**, en traitant des milliers d’images, l’algorithme doit être en mesurer de créer de lui-même une catégorie ‘’chien’’, même s’il ne sait pas ce qu’est cela représente, il remarquera les similarités entre les images.
L’algorithme a seulement regroupé toutes les images de chiens ensemble car elles avaient toutes un certain nombre de points communs : taille, quatre pattes, forme du visage, forme du museau, etc… (On remarque facilement qu’à l’intérieur d’une catégorie peuvent se trouver plusieurs sous-catégories; par exemple dans la catégorie « chien » peuvent se trouver différentes races de chiens).

#### Différences avec supervisé
L’apprentissage non supervisé est principalement utilisé en matière de clusterisation, procédé destiné à regrouper un ensemble d’éléments hétérogènes sous forme de sous groupes homogènes ou liés par des caractéristiques communes.
La machine **fait alors elle même les rapprochements** en fonction de ces caractéristiques qu’elle est en mesure de repérer sans nécessiter d’intervention externe.
De cette capacité à effectuer de la clusterisation découle également la possibilité de mettre au point un système de recommandation (le système peut par exemple recommander un livre ou un film à un utilisateur en fonction des goûts d’utilisateurs partageant des caractéristiques communes) ainsi que la possibilité de mettre au point un système de détection d’anomalies.

![image](https://user-images.githubusercontent.com/55838700/156841799-c882f919-d5db-48e0-99da-0c38341feb70.png)

### Par renforcement
Le Reinforcement Learning ou l’apprentissage par renforcement (RL) est la science de la prise de décision.
Il s’agit d’apprendre le comportement optimal dans un environnement donné pour obtenir une récompense maximale.
Ce comportement optimal s’acquiert par des interactions avec l’environnement et l’observation de ses réactions.

Le problème du Reinforcement Learning implique qu’un agent explore un environnement inconnu pour atteindre un objectif.
Le RL est basé sur l’hypothèse que tous les objectifs peuvent être décrits par la maximisation de la récompense cumulative attendue.
L’agent doit apprendre à sentir et à perturber l’état de l’environnement en utilisant ses actions pour obtenir une récompense maximale.
Un agent dans un état actuel S apprend de son environnement en interagissant avec ce dernier par le moyen d’actions.
Suite à une action A, l’environnement retourne un nouvel état S’ et une récompense R associée, qui peut être positive ou négative.

![Capture](https://lh3.googleusercontent.com/WqC7aJGjWkjoU4wIjch0WH7ipBKJU1lbnX_-xVHh-zAsH2woxUBN92ug6yJ5mUi3Mpj1CMvg6X4YR9En1PoECUcEbom3wQ6K8fEk0wjUiedOLxwBxoaTjXhpIxbGrddivgoMJxfA)

Le Reinforcement Learning a affiché des performances spectaculaires ces dernières années.
Il a permis à des programmes d’apprendre par eux-mêmes dans des environnements complexe des stratégies extrêmement puissantes et robustes.
Sous l’impulsion de DeepMind, ces algorithmes ont révolutionné l’intelligence artificielle dans de nombreux domaines, notamment dans le domaine des jeux, allant des jeux d’arcade (Agent57) et des jeux de plateau (AlphaGo) jusqu’aux jeux-vidéos (AlphaStar).

![Capture](https://cdn.futura-sciences.com/buildsv6/images/mediumoriginal/d/3/4/d34887ec89_107368_alphago-kejie.jpg)

Un cours est d'ailleurs entièrement dédié à ce vaste sujet.

## Pour aller plus loin

Dans cette dernière partie, nous pouvons aller plus loin et nous intéresser à la partie **semi-supervisée** du machine learning.

![image](https://user-images.githubusercontent.com/55838700/157338748-ef5b97dc-6060-43a8-b62d-78ebb9a958ae.png)

Les algorithmes de machine learning **semi-supervisés** se situent quelque part entre l'apprentissage supervisé et l'apprentissage non supervisé, puisqu'ils utilisent des données étiquetées et non étiquetées pour la formation - généralement une petite quantité de données étiquetées et une grande quantité de données non étiquetées. Les systèmes qui utilisent cette méthode sont capables d'améliorer considérablement la précision de l'apprentissage. Habituellement, l'apprentissage semi-supervisé est choisi lorsque les données étiquetées acquises nécessitent des ressources compétentes et pertinentes afin de les former et d'en tirer des enseignements. Sinon, l'acquisition de données non étiquetées ne nécessite généralement pas de ressources supplémentaires.

Pour en savoir davantage sur l'apprentissage semi-supervisé, vous pouvez consulter :
* Cet article de "LeMondeInformatique" vulgarisant la notion : https://www.lemondeinformatique.fr/les-dossiers/lire-l-apprentissage-semi-supervise-trouve-sa-place-1031.html
* Cet article qui explique en quoi ce type d'apprentissage peut être utile : https://fr.theastrologypage.com/why-is-semi-supervised-learning-helpful-model


## Sources
* [Le chocolat ne rend pas plus intelligent](https://www.youtube.com/watch?v=z_cACapt3Hc)
* [Tout les modèles sont faux, certains sont utiles](https://fr.abcdef.wiki/wiki/All_models_are_wrong)
* https://www.actuia.com/vulgarisation/difference-entre-apprentissage-supervise-apprentissage-non-supervise/
* https://machinelearnia.com/apprentissage-supervise-4-etapes/
* https://dataanalyticspost.com/Lexique/reduction-de-dimensionnalite/
