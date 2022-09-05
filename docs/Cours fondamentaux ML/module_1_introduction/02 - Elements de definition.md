# Eléments de définition

À l’intersection des statistiques et de l’informatique, le machine learning se préoccupe de la modélisation des données. Les grands principes de ce domaine ont émergé des statistiques fréquentistes ou bayésiennes, de l’intelligence artificielle ou encore du traitement du signal. Dans ce livre, nous considérons que le machine learning est la science de l’apprentissage automatique d’une fonction prédictive à partir d’un jeu d’observations de données étiquetées ou non.

Ce chapitre se veut une **introduction aux concepts et aux premières définitions qui fondent le machine learning**, et en propose plusieurs approches, décrites et illustrées.

## 1. Plusieurs approches en ML

Le machine learning est un champ assez vaste, et nous dressons dans cette section une liste des plus grandes classes de problèmes auxquels il s’intéresse. Une description précise de chaque approche sera apportée, toujours illustrée d'exemples précis. Chaque approche a ses spécificités et permet de répondre à des objectifs précis. 

### 2.1 Supervisé

Qu’il s’agisse des types d’apprentissage supervisé ou non supervisé, tout part d’un jeu de données très important. Et quand on dit « très important », cela peut signifier jusqu’à plusieurs millions d'images ou plusieurs millions de documents. C’est à partir de cette base que l’algorithme peut apprendre.  
Avec l’apprentissage supervisé, la machine peut apprendre à faire une certaine tâche en étudiant des exemples de cette tâche. Par exemple, elle peut apprendre à reconnaître une photo de chien après qu’on lui ait montré des millions de photos de chiens. Ou bien, elle peut apprendre à traduire le français en chinois après avoir vu des millions d’exemples de traduction français-chinois. 

D’une manière générale, la machine peut apprendre une relation f: x-->y qui relie x à y en ayant analysé des millions d’exemples d’associations.

![Capture](https://machinelearnia.com/wp-content/uploads/2019/06/apprentissage-supervise-2-.png)
 
Dans le cadre de l’apprentissage supervisé, la machine connaît déjà les réponses qu’on attend d’elle. Elle travaille à partir de données étiquetées. Reprenons l’exemple d’une application destinée à reconnaître les chiens et les chats. Pour l’entraîner, on lui présente des images étiquetés comme « chien » ou « chat ». Par des techniques issues des statistiques et des probabilités, l’algorithme comprend alors quelles sont les caractéristiques qui permettent de classer ces images dans chacune des catégories. Ainsi, au fur et à mesure qu’on lui présentera de nouvelles images, il pourra les identifier, en donnant un score de probabilité. Par exemple : « cette image a 95 % de chances de représenter un chat. » Et ses premières réponses seront corrigées à la main, pour qu’il s’améliore au fur et à mesure.

Cette méthode permet de réaliser deux types de tâches :
-	**Classification** 
-	**Régression**

#### 1.1.1 Enjeux Classification VS Régression

Une première grande distinction à faire en machine learning est la différence entre **apprentissage supervisé** et **non supervisé**. En anglais, ces deux notions se nomment respectivement "supervised learning" et "unsupervised learning".

Si le modèle est un modèle supervisé, il peut-être de 2 types ou sous-catégories : modèle de régression ou de classification.


![Capture](https://assets.moncoachdata.com/v7/moncoachdata.com/wp-content/uploads/2020/01/segmentation-machine-learning.png?w=1242)

 
Pour bien comprendre la différence, allons plus dans le détail :


######  1.1.1.1.1  Classification

La classification est une tâche qui nécessite l'utilisation d'algorithmes d'apprentissage automatique qui apprennent à attribuer une étiquette de classe aux exemples du domaine du problème. Revenons une nouvelle fois sur notre problématique de détection de chat et de chien.

![image](https://user-images.githubusercontent.com/55838700/157056018-c7a0bede-030e-4074-ba78-8b2706aa0f75.png)

Imaginons un système de classification d'images de chiens et de chats. En entrée, notre système va extraire les caractéristiques des images pour les classer en **chat** ou en **chien**. Supposons que le système ait un enseignant ! Il enseigne au système quels animaux sont des chiens et lesquels sont des chats. Ceci est un exemple de problème de classification supervisée car nous avons des exemples étiquetés définis au préalabe. Les labels des images sont soit "chien" soit "chat". De plus, il s'agit bien de la classification parce que la sortie est une prédiction de la classe à laquelle appartient notre objet. 

Il existe de nombreux types de tâches de classification que vous pouvez rencontrer dans l'apprentissage automatique et des approches spécialisées de la modélisation qui peuvent être utilisées pour chacune. Ces approches seront étudiées plus en détail à la suite du cours.


######  1.1.1.1.2  Régression

Dans le domaine de l'apprentissage statistique, la régression permet d'**approcher une variable quantitative** à partir d'autres qui lui sont corrélées.

La régression s'articule autour d'algorithmes simples, qui sont souvent utilisés dans la finance, l'investissement et autres, et établit la relation entre une seule variable dépendante de plusieurs variables indépendantes. 

Il existe plusieurs algorithmes pour la régression:
•	Régression linéaire

•	Régression polynomiale

•	Régression quantile

•	etc.

Le modèle de régression le plus connu est le modèle de régression linéaire.

![image](https://user-images.githubusercontent.com/55838700/157339195-b7585660-1e87-467c-8eb5-b589f493f9d1.png)

Lorsque le modèle n'est pas linéaire, on peut effectuer une régression approchée par des algorithmes itératifs, on parle de régression non linéaire. 

Prédire le nombre de clics sur un lien ou prédire le rendement d’un plant de maïs sont des exemples de regression classiques.

##### 1.1.1.1.3 Classification vs Regression

La différence la plus significative entre la régression et la classification est que si la régression aide à prédire une quantité continue, la classification prédit des étiquettes de classe discrètes. Il existe également des similitudes entre les deux types d'algorithmes d'apprentissage automatique.

•	Un algorithme de **régression** peut prédire une valeur discrète qui se présente sous la forme d'une quantité entière

•	Un algorithme de **classification** peut prédire une valeur continue si elle se présente sous la forme d'une probabilité d'étiquette de classe

Considérons un ensemble de données contenant des informations sur les étudiants d'une université particulière. Un algorithme de régression peut être utilisé dans ce cas pour prédire la taille de tout élève en fonction de son poids, de son sexe, de son régime alimentaire ou de sa matière principale. Nous utilisons la régression dans ce cas car la hauteur est une **quantité continue**. Il existe un nombre infini de valeurs possibles pour la taille d'une personne.

Au contraire, la classification peut être utilisée pour analyser si un e-mail est un spam ou non. L'algorithme vérifie les mots-clés dans un e-mail et l'adresse de l'expéditeur est essaie de déterminer la probabilité que l'e-mail soit un spam. De même, alors qu'un modèle de régression peut être utilisé pour prédire la température du lendemain, nous pouvons utiliser un algorithme de classification pour déterminer s'il fera froid ou chaud en fonction des valeurs de température données.
 
 ![Capture](https://miro.medium.com/max/1400/1*wH09k0DhF4JQhVMymtVQHQ.jpeg)
Comprendre la différence entre les algorithmes de régression et de classification peut vous aider à appliquer les concepts d'apprentissage automatique de manière plus précise. Certains algorithmes peuvent nécessiter à la fois des approches de classification et de régression, c'est pourquoi une connaissance approfondie des deux est cruciale.

#####  1.1.1.2  Définition et caractéristiques d’un Data set

Comme pour apprendre la langue chinoise, on parle d’apprentissage supervisé lorsque l’on fournit à une machine beaucoup d’exemples (x, y) dans le but de lui faire apprendre la relation qui relie x à y.

En Machine Learning, on compile ces exemples (x, y) dans un tableau que l’on appelle **Dataset** :

Dans l’apprentissage supervisé, la machine reçoit un Dataset où les exemples (x) sont étiquetés d’une valeur (y) (on appelle ça un **labelled** Dataset). Il est alors possible de trouver une relation générale qui relie (x) à (y). Pour cela,, on doit définir nos variables :

• La variable **y** porte le nom de **target** (la cible). C’est la valeur que l’on cherche à prédire.

• La variable **x** porte le nom de **feature** (facteur). Un facteur influence la valeur de y, et on a en général beaucoup de features (x1, x2, ... ) dans notre Dataset que l’on regroupe dans une matrice X.

Ci-dessous, un exemple de Dataset de données numériques qui regroupe des exemples d’appartements avec leur prix ainsi que certaines de leurs caractéristiques (features).

![image](https://user-images.githubusercontent.com/55838700/157341943-acb21b6e-fbed-4611-9d7f-4af90cb82509.png)

Par convention, on dit que notre Dataset contient m exemples, c’est-à-dire **m** lignes. Si vous avez visité 3 appartements, alors m=3. On note également **n** le nombre de features dans notre Dataset, c’est-à-dire le nombre de colonnes (**hormis la colonne y**). Si vous avez noté 3 caractéristiques pour vos appartement (Surface, qualité, ville), alors n=3.
 
Le prix est notre variable cible « target » tandis que la surface en m2, le nombre de chambres et la qualité sont des variables « features ».

Quand on développe un **programme de vision par ordinateur**, les features de notre Dataset changent de format et peuvent être **les caractéristiques des pixels présents sur l’image** ou dans une vidéo. Dans le cadre de notre exemple de début de chapitre (classification chien/chat), nos données sont des images de chiens ou de chats. Ces données sont labellisées, c'est à dire que l'on va associer une classe à ces images. Notre target est la classe cible, c'est à dire image de chien ou image de chat.

![image](https://user-images.githubusercontent.com/55838700/157762744-98c7af47-3122-42af-817f-088266790225.png)

Les data sets sont donc des ensembles de caractéristiques dont le format et la structure varient **selon le type de données manipulé**.

Avec de tels datasets, il devient possible de prédire de nouvelles valeurs y à partir de valeurs de x en développant un modèle de classification supervisé selon la problématique à traiter.

### 1.2 Non Supervisé

Qu’est-ce que l’apprentissage non supervisé ? C’est de l’apprentissage sans superviseur, tout simplement… 😊 L’apprentissage non supervisé consiste à apprendre à un algorithme d’intelligence artificielle des informations qui ne sont **ni étiquetées** (on ne précisera pas que telle image est un chat ou je ne sais quoi d’autre), **ni classées** pour permettre à cette algorithme de réagir à ces informations sans intervention humaine, c’est-à-dire sans superviseur (d’où le nom, vous l’aurez compris). De plus, l’algorithme traite les données sans aucun entrainement préalable, il « s’entraine lui-même » avec les données qu’il reçoit. 

Néanmoins, ce n’est pas parce que l’on parle d’apprentissage non supervisé que l’on doit omettre la notion de catégories pour les algorithmes de classification. Un algorithme d’apprentissage non supervisé utilise des catégories associées aux données qu’on lui soumet, mais il doit les faire émerger lui-même, afin, par exemple, de reconnaître qu’un chat est un chat.

![image](https://user-images.githubusercontent.com/55838700/157058262-55717286-3591-41d5-8e55-27375f1c2389.png)

En apprentissage supervisé on fournit des milliers d’images de chiens à l’algorithme avec le label ’chien’. De cette manière, si on lui fournit une autre image quelconque il pourra déterminer si elle représente un chat ou pas. En apprentissage non supervisé, **aucun label n’est fourni**, en traitant des milliers d’images, l’algorithme doit être en mesurer de créer de lui-même une catégorie ‘’chien’’, même s’il ne sait pas ce qu’est cela représente, il remarquera les similarités entre les images. L’algorithme a seulement regroupé toutes les images de chiens ensemble car elles avaient toutes un certain nombre de points communs : taille, quatre pattes, forme du visage, forme du museau, etc… (On remarque facilement qu’à l’intérieur d’une catégorie peuvent se trouver plusieurs sous-catégories; par exemple dans la catégorie « chien » peuvent se trouver différentes races de chiens).

#### 1.2.1 Différences avec supervisé

L’apprentissage non supervisé est principalement utilisé en matière de clusterisation, procédé destiné à regrouper un ensemble d’éléments hétérogènes sous forme de sous groupes homogènes ou liés par des caractéristiques communes. La machine **fait alors elle même les rapprochements** en fonction de ces caractéristiques qu’elle est en mesure de repérer sans nécessiter d’intervention externe. De cette capacité à effectuer de la clusterisation découle également la possibilité de mettre au point un système de recommandation (le système peut par exemple recommander un livre ou un film à un utilisateur en fonction des goûts d’utilisateurs partageant des caractéristiques communes) ainsi que la possibilité de mettre au point un système de détection d’anomalies.

![image](https://user-images.githubusercontent.com/55838700/156841799-c882f919-d5db-48e0-99da-0c38341feb70.png)


#### 1.2.2 Clustering

Le problème d’apprentissage non supervisé le plus fréquent est la segmentation (en anglais le clustering), c’est l’étape où l’on essaie de **séparer les données en catégories**. C’est la pierre angulaire de l’apprentissage non supervisé. C’est à la fois sa plus grande contrainte et sa plus grande force. C’est ce qui fait que l’on fait le parallèle entre l’apprentissage non supervisé et la façon humaine de raisonner puisque l’intelligence artificielle est alors autonome. Il n’y a pas besoin d’intervention humaine préalable pour créer les catégories, ce qui est exactement le cas pour les humains ! On a appris nous-mêmes à distinguer les objets que l’on voit, à savoir que tel animal est un lapin ou un chat par exemple !

![Capture](https://user.oc-static.com/upload/2017/05/12/14946001500306_P3C1-2.png)

Le clustering permet d'identifier des groupes homogènes parmi une population donnée.

#### 1.2.3 Association
La recherche des règles d’association est une méthode dont le but est de découvrir des relations ayant un intérêt entre deux ou plusieurs variables stockées dans de très importantes bases de données. Les algorithmes d’association sont particulièrement adaptés pour explorer des bases de données volumineuses ou complexes. Par exemple, ils peuvent identifier la probabilité de co-occurrence d’éléments dans une collection de données.
 
Quelques exemples:

•	Association entre alimentation et apparition de maladies

•	Association entre génotype et phénotype

•	Association entre activations de neurones et comportement


#### 1.2.4 Réduction de dimensions
Un second cas d’apprentissage non supervisé concerne la réduction de dimensions. 

Il  désigne ainsi toute méthode permettant de projeter des données issues d’un espace de grande dimension dans un espace de plus petite dimension. Cette opération est cruciale en apprentissage automatique pour lutter contre ce qu’on appelle le fléau des grandes dimensions (le fait que les grandes dimensions altèrent l’efficacité des méthodes).

![image](https://user-images.githubusercontent.com/55838700/157340186-6cc1e49f-f2db-4560-8e66-aba94282d054.png)

On emploie ici le mot « dimension » au sens algébrique, i.e. la dimension de l’espace vectoriel sous-jacent aux valeurs des vecteurs de descripteurs. La réduction de dimensionnalité permet de réduire la complexité d’un problème d’apprentissage automatique à plusieurs niveaux :

• d’un point de vue **théorique**, cela entraîne automatiquement une amélioration des propriétés de stabilité et de robustesse des algorithmes.

• d’un point de vue **pratique**, cela simplifie la résolution du problème d’optimisation associé, en réduisant l’espace des solutions. En d’autres termes, réduire la dimensionnalité limite le nombre de possibilités à tester, ce qui permet de traiter les données plus rapidement. Ce gain de temps est fonction de la dépendance de la complexité temporelle de l’algorithme par rapport à la dimension.


### 1.3 Par renforcement

Le reinforcement learning ou l’apprentissage par renforcement (RL) est la science de la prise de décision. Il s’agit d’apprendre le comportement optimal dans un environnement donné pour obtenir une récompense maximale. Ce comportement optimal s’acquiert par des interactions avec l’environnement et l’observation de ses réactions.
Le problème du reinforcement learning implique qu’un agent explore un environnement inconnu pour atteindre un objectif. Le RL est basé sur l’hypothèse que tous les objectifs peuvent être décrits par la maximisation de la récompense cumulative attendue. L’agent doit apprendre à sentir et à perturber l’état de l’environnement en utilisant ses actions pour obtenir une récompense maximale.
Un agent dans un état actuel S apprend de son environnement en interagissant avec ce dernier par le moyen d’actions. Suite à une action A, l’environnement retourne un nouvel état S’ et une récompense R associée, qui peut être positive ou négative.
 
 
 ![Capture](https://lh3.googleusercontent.com/WqC7aJGjWkjoU4wIjch0WH7ipBKJU1lbnX_-xVHh-zAsH2woxUBN92ug6yJ5mUi3Mpj1CMvg6X4YR9En1PoECUcEbom3wQ6K8fEk0wjUiedOLxwBxoaTjXhpIxbGrddivgoMJxfA)

Le Reinforcement Learning a affiché des performances spectaculaires ces dernières années, en permettant à des programmes d’apprendre par eux-mêmes, dans des environnements complexes, des stratégies extrêmement puissantes et robustes. Sous l’impulsion de DeepMind, ces algorithmes ont révolutionné l’intelligence artificielle dans de nombreux domaines, notamment dans le domaine des jeux, allant des jeux d’arcade (Agent57) et des jeux de plateau (AlphaGo), jusqu’aux jeux-vidéos (AlphaStar).
 
![Capture](https://cdn.futura-sciences.com/buildsv6/images/mediumoriginal/d/3/4/d34887ec89_107368_alphago-kejie.jpg)

Un cours est d'ailleurs entièrement dédié à ce vaste sujet.

### 2. Pour aller plus loin

Dans cette dernière partie, nous pouvons aller plus loin et nous intéresser à la partie **semi-supervisée** du machine learning.

![image](https://user-images.githubusercontent.com/55838700/157338748-ef5b97dc-6060-43a8-b62d-78ebb9a958ae.png)

Les algorithmes de machine learning **semi-supervisés** se situent quelque part entre l'apprentissage supervisé et l'apprentissage non supervisé, puisqu'ils utilisent des données étiquetées et non étiquetées pour la formation - généralement une petite quantité de données étiquetées et une grande quantité de données non étiquetées. Les systèmes qui utilisent cette méthode sont capables d'améliorer considérablement la précision de l'apprentissage. Habituellement, l'apprentissage semi-supervisé est choisi lorsque les données étiquetées acquises nécessitent des ressources compétentes et pertinentes afin de les former et d'en tirer des enseignements. Sinon, l'acquisition de données non étiquetées ne nécessite généralement pas de ressources supplémentaires.

Pour en savoir davantage sur l'apprentissage semi-supervisé, vous pouvez consulter :
- cet article de "LeMondeInformatique" vulgarisant la notion : https://www.lemondeinformatique.fr/les-dossiers/lire-l-apprentissage-semi-supervise-trouve-sa-place-1031.html
- cet article qui explique en quoi ce type d'apprentissage peut être utile : https://fr.theastrologypage.com/why-is-semi-supervised-learning-helpful-model


### 3. Sources

Ci-dessous quelques sources web empruntées dans le cadre de la réalisation de ce chapitre :

https://www.actuia.com/vulgarisation/difference-entre-apprentissage-supervise-apprentissage-non-supervise/

https://machinelearnia.com/apprentissage-supervise-4-etapes/

https://dataanalyticspost.com/Lexique/reduction-de-dimensionnalite/
