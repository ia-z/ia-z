# Chap 2 - Eléments de définition

À l’intersection des statistiques et de l’informatique, le machine learning se préoccupe de la modélisation des données. Les grands principes de ce domaine ont émergé des statistiques fréquentistes ou bayésiennes, de l’intelligence artificielle ou encore du traitement du signal. Dans ce livre, nous considérons que le machine learning est la science de l’apprentissage automatique d’une fonction prédictive à partir d’un jeu d’observations de données étiquetées ou non.

Ce chapitre se veut une introduction aux concepts et aux premières définitions qui fondent le machine learning, et en propose plusieurs approches, décrites et illustrées.

## 1. Typologie de méthodes de fouille de données

### 1.1 Typologie selon le type de modèle obtenu

Typologie selon l’objectif
- Prédiction : sortie d'un modèle de machine learning.
Le terme prédiction est un peu trompeur, car on ne prédit pas le futur mais on utilise un modèle
qui a appris de données passées pour effectuer des suppositions sur de nouvelles données.
- Classification : examiner les caractéristiques d’un objet et lui attribuer
une classe. e.g. diagnostic ou décision d’attribution de prêt à un client.
- Régression : tâche où la prédiction est une valeur continue.
- Association : déterminer les attributs qui sont corrélés. e.g. analyse du panier d'un client.
- Segmentation : former des groupes homogènes à l’intérieur d’une
population.

### 1.2 Typologie selon le type d'apprentissage utilisé

**Apprentissage supervisé : fouille supervisée *(fouille supervisée ?)***
- Méthode d'apprentissage qui nécessite des exemples d’apprentissage contenant à la fois
des données d’entrée (les *inputs*) et de sortie (les *labels*).
- Les exemples d’apprentissage sont fournis avec leur classe.
- But : prédire correctement un nouvel exemple.
- Utilisés principalement en classification et en régression.

**Apprentissage non supervisé : fouille non supervisée *(?)***
- Processus qui prend en entrée des exemples d’apprentissage contenant que des données d’entrée (et pas de *labels*).
- Pas de notion de classe.
- But : regrouper les exemples en paquets (clusters) d’exemples similaires.
- Utilisés principalement en segmentation et association.


## 2. Plusieurs approches en ML

Le machine learning est un champ assez vaste, et nous dressons dans cette section une liste des plus grandes classes de problèmes auxquels il s’intéresse. Une description précise de chaque approche sera apportée, toujours illustrée d'exemples précis. Chaque approche a ses spécificités et permet de répondre à des objectifs précis. 

### 2.1 Supervisé
Qu’il s’agisse des types d’apprentissage supervisé ou non supervisé, tout part d’un jeu de données très important. Et quand on dit « très important », cela peut signifier jusqu’à plusieurs millions d”images ou plusieurs millions de documents. C’est à partir de cette base que l’algorithme peut apprendre.  
Avec l’apprentissage supervisé, la machine peut apprendre à faire une certaine tâche en étudiant des exemples de cette tâche. Par exemple, elle peut apprendre à reconnaître une photo de chien après qu’on lui ait montré des millions de photos de chiens. Ou bien, elle peut apprendre à traduire le français en chinois après avoir vu des millions d’exemples de traduction français-chinois. 
D’une manière générale, la machine peut apprendre une relation $f: x → y$
qui relie $x$ à $y$ en ayant analysé des millions d’exemples d’associations.

![Capture](https://machinelearnia.com/wp-content/uploads/2019/06/apprentissage-supervise-2-.png)
 
Dans le cadre de l’apprentissage supervisé, la machine connaît déjà les réponses qu’on attend d’elle. Elle travaille à partir de données étiquetées. Reprenons l’exemple d’une application destinée à reconnaître les chiens et les chats. Pour l’entraîner, on lui présente des images étiquetés comme « chien » ou « chat ». Par des techniques issues des statistiques et des probabilités, l’algorithme comprend alors quelles sont les caractéristiques qui permettent de classer ces images dans chacune des catégories. Ainsi, au fur et à mesure qu’on lui présentera des nouveaux images, il pourra les identifier, en donnant un score de probabilité. Par exemple : « cette image a 95 % de chances de représenter un chat. » Et ses premières réponses seront corrigées à la main, pour qu’il s’améliore au fur et à mesure.
Cette méthode permet de réaliser deux types de tâches :
-	Classification 
-	Régression

#### 2.1.1 Enjeux Classification VS Régression
Une première grande distinction à faire en machine learning est la différence entre apprentissage supervisé et non supervisé. En anglais, ces deux notions se nomment respectivement supervised learning et unsupervised learning.
Si le modèle est un modèle supervisé, il peut-être de 2 types ou sous-catégories : modèle de régression ou de classification.

![Capture](https://assets.moncoachdata.com/v7/moncoachdata.com/wp-content/uploads/2020/01/segmentation-machine-learning.png?w=1242)

 
Pour bien comprendre la différence, allons plus dans le détail :


######  2.1.1.1.2  Classification

La classification est une tâche qui nécessite l'utilisation d'algorithmes d'apprentissage automatique qui apprennent à attribuer une étiquette de classe aux exemples du domaine du problème. Un exemple facile à comprendre consiste à classer les e-mails comme « spam » ou « non spam ».
Imaginez qu'un système souhaite détecter des pommes et des oranges dans un panier de fruits.

![Capture](https://www.jobboom.com/carriere/wp-content/uploads/2014/08/pomme-orange.jpg)

Le système peut prélever un fruit, en extraire certaines propriétés (par exemple le poids de ce fruit). Supposons que le système ait un enseignant ! cela enseigne au système quels objets sont des pommes et lesquels sont des oranges . Ceci est un exemple de problème de classification supervisé . Il est supervisé car nous avons des exemples étiquetés. C'est la classification parce que la sortie est une prédiction de la classe à laquelle appartient notre objet. Dans cet exemple, nous considérons 3 entités (propriétés / variables explicatives):

![image](https://user-images.githubusercontent.com/55838700/156841599-7fd3cb4b-9a14-4428-9a8b-dd34d4e8c741.png)


le poids du fruit sélectionné est-il supérieur à 5 grammes1. est la taille supérieure à 10cm2 est la couleur est rouge3. (0 signifie non et 1 signifie oui) Donc, pour représenter une pomme / orange, nous avons une série de trois propriétés (appelées vecteur) (par exemple, [0,0,1] signifie que ce poids de fruit n'est pas supérieur à 0,5 gramme et que sa taille est inférieure à 10 cm et que sa couleur est rouge)
Donc, nous sélectionnons 10 fruits au hasard et mesurons leurs propriétés. L'enseignant (humain) identifie ensuite chaque fruit manuellement comme étant pomme => [1] ou orange => [2] . Par exemple, le professeur choisit un fruit qui est pomme. La représentation de cette pomme pour le système pourrait être quelque chose comme ceci: [1, 1, 1] => [1] , cela signifie que ce fruit a un poids supérieur à 0,5 gramme , une taille supérieure à 10 cm et 3. la couleur de ce fruit est rouge et enfin c'est une pomme (=> [1]) Ainsi, pour chacun des 10 fruits, l'enseignant a étiqueté chaque fruit comme étant pomme [=> 1] ou orange [=> 2] et le système a trouvé ses propriétés. comme vous pouvez le deviner, nous avons une série de vecteurs (appelés matrice) pour représenter 10 fruits entiers.

Il existe de nombreux types de tâches de classification que vous pouvez rencontrer dans l'apprentissage automatique et des approches spécialisées de la modélisation qui peuvent être utilisées pour chacune. Ces approches seront étudiées plus en détails à la suite du cours.


######  2.1.1.1.1  Regression

Littéralement en mathématiques, la régression est le fait d’approcher une variable (le prix d’un appartement) à partir d’autres qui lui sont liées (la superficie et le nombre de pièces). 
Pour atteindre cet objectif, plusieurs modèles d’approches sont possibles : approcher les données par une droite (cf exemple ci-contre) = régression linéaire, par un polynôme = régression polynômiale, par une fonction logarithmique, etc…
Par extension, on appelle régression en intelligence artificielle tout problème qui consiste à prédire une variable qualitative (i.e. un nombre) ! La prédiction de l’IA sera donc généralement une valeur comprise entre -1 et 1.
Les domaines d’application sont nombreux, des finances (prédiction du cours de la Bourse…) au commerce (stocks futurs à prévoir…) en passant par la maintenance prédictive (anticiper une panne).
Il existe plusieurs algorithmes pour la régression:
•	Régression linéaire
•	Régression polynomiale
•	Régression logistique *C'est en fait un modèle de classification*
•	Régression quantile
•	etc.

L’objectif de la régression linéaire (ici) est de proposer un modèle qui, pour chaque valeur entre 0 et 4, prédit la position du point rouge. On remarque que le modèle ne prédit (quasiment) jamais la bonne valeur mais n’en est pas très loin !


Voici quelques autres exemples de problèmes de régression :
 Prédire le nombre de clics sur un lien.
 Prédire le nombre d’utilisateurs et utilisatrices d’un service en ligne à un moment
donné.
 Prédire le prix d’une action en bourse.
 Prédire l’affinité de liaison entre deux molécules.
 Prédire le rendement d’un plant de maïs.

##### 2.1.1.1.3 Classification vs Regression

La différence la plus significative entre la régression et la classification est que si la régression aide à prédire une quantité continue, la classification prédit des étiquettes de classe discrètes. Il existe également des similitudes entre les deux types d'algorithmes d'apprentissage automatique.
•	Un algorithme de régression peut prédire une valeur discrète qui se présente sous la forme d'une quantité entière
•	Un algorithme de classification peut prédire une valeur continue si elle se présente sous la forme d'une probabilité d'étiquette de classe
Considérons un ensemble de données contenant des informations sur les étudiants d'une université particulière. Un algorithme de régression peut être utilisé dans ce cas pour prédire la taille de tout élève en fonction de son poids, de son sexe, de son régime alimentaire ou de sa matière principale. Nous utilisons la régression dans ce cas car la hauteur est une quantité continue. Il existe un nombre infini de valeurs possibles pour la taille d'une personne.
Au contraire, la classification peut être utilisée pour analyser si un e-mail est un spam ou non. L'algorithme vérifie les mots-clés dans un e-mail et l'adresse de l'expéditeur est de déterminer la probabilité que l'e-mail soit un spam. De même, alors qu'un modèle de régression peut être utilisé pour prédire la température du lendemain, nous pouvons utiliser un algorithme de classification pour déterminer s'il fera froid ou chaud en fonction des valeurs de température données.
 
 ![Capture](https://miro.medium.com/max/1400/1*wH09k0DhF4JQhVMymtVQHQ.jpeg)
 
Comprendre la différence entre les algorithmes de régression et de classification peut vous aider à appliquer les concepts d'apprentissage automatique de manière plus précise. Certains algorithmes peuvent nécessiter à la fois des approches de classification et de régression, c'est pourquoi une connaissance approfondie des deux est cruciale.

#####  2.1.1.2  Définition et caractéristiques d’un Data set

Comme pour apprendre la langue chinoise, on parle d’apprentissage supervisé lorsque l’on fournit à une machine beaucoup d’exemples (x, y) dans le but de lui faire apprendre la relation qui relie x à y.
En Machine Learning, on compile ces exemples (x, y) dans un tableau que l’on appelle Dataset :
Dans l’apprentissage supervisé, la machine reçoit un Dataset où les exemples (x) sont étiquetés d’une valeur (y) (on appelle ça un Labelled Dataset). Il est alors possible de trouver une relation générale qui relie (x) à (y). Pour cela,, on doit définir nos variables :
• La variable y porte le nom de target (la cible). C’est la valeur que l’on cherche à prédire.
• La variable x porte le nom de feature (facteur). Un facteur influence la valeur de y, et on a en général beaucoup de features (x1, x2, ... ) dans notre Dataset que l’on regroupe dans une matrice X.

Ci-dessous, un Dataset qui regroupe des exemples d’appartements avec leur prix y ainsi que certaines de leurs caractéristiques (features).

![image](https://user-images.githubusercontent.com/55838700/156841475-38a86098-22ac-4151-bc4b-112bebd60b54.png)

 

Le prix est notre variable cible « target » tandis que la surface en m2, le nombre e chambres et la qualité sont des variables « features »

### 2.2 Non Supervisé
Qu’est-ce que l’apprentissage non supervisé ? C’est de l’apprentissage sans superviseur, tout simplement… 😊 L’apprentissage non supervisé consiste à apprendre à un algorithme d’intelligence artificielle des informations qui ne sont ni étiquetées (on ne précisera pas que telle image est un chat ou je ne sais quoi d’autre), ni classées pour permettre à cette algorithme de réagir à ces informations sans intervention humaine, c’est-à-dire sans superviseur (d’où le nom, vous l’aurez compris). De plus, l’algorithme traite les données sans aucun entrainement préalable, il « s’entraine lui-même » avec les données qu’il reçoit. 

Néanmoins, ce n’est pas parce que l’on parle d’apprentissage non supervisé que l’on doit omettre la notion de catégories pour les algorithmes de classifications. Un algorithme d’apprentissage non supervisé utilise des catégories associées aux données qu’on lui soumet, mais il doit les faire émerger lui-même, afin, par exemple, de reconnaître qu’un chat est un chat, ou qu’un article de la revue IA est un article de la revue IA. En apprentissage supervisé on fournit des milliers d’images de chiens à l’algorithme avec le label ‘’chien’’. De cette manière, si on lui fournit une autre image quelconque il pourra déterminer si elle représente un chat ou pas. En apprentissage non supervisé, aucun label n’est fourni, en traitant des milliers d’images, l’algorithme doit être en mesurer de créer de lui-même une catégorie ‘’chien’’, même s’il ne sait pas ce qu’est cela représente, il remarquera les similarité entre les images. L’algorithme a seulement regroupé toutes les images de chiens ensemble car elles avaient toutes un certain nombre de points communs : taille, quatre pattes, forme du visage, forme du museau etc… (On remarque facilement qu’à l’intérieur d’une catégorie peuvent se trouver plusieurs sous-catégories; par exemple dans la catégorie « chien » peuvent se trouver différentes races de chiens).

#### 2.2.1 Différences avec supervisé
L’apprentissage non supervisé est principalement utilisé en matière de clusterisation, procédé destiné à regrouper un ensemble d’éléments hétérogènes sous forme de sous groupes homogènes ou liés par des caractéristiques communes. La machine fait alors elle même les rapprochements en fonction de ces caractéristiques qu’elle est en mesure de repérer sans nécessiter d’intervention externe. De cette capacité à effectuer de la clusterisation découle également la possibilité de mettre au point un système de recommandation ( le système peut par exemple recommander un livre ou un film à un utilisateur en fonction des goûts d’utilisateurs partageant des caractéristiques communes) ainsi que la possibilité de mettre au point un système de détection d’anomalies.

![image](https://user-images.githubusercontent.com/55838700/156841799-c882f919-d5db-48e0-99da-0c38341feb70.png)


#### 2.2.3 CLustering
Le problème d’apprentissage non supervisé le plus fréquent est la segmentation (en anglais le clustering), c’est l’étape où l’on essaie de séparer les données en catégories. C’est la pierre angulaire de l’apprentissage non supervisé. C’est à la fois sa plus grande contrainte et sa plus grande force. C’est ce qui fait que l’on fait le parallèle entre l’apprentissage non supervisé et la façon humaine de raisonner puisque l’intelligence artificielle est alors autonome. Il n’y a pas besoin d’intervention humaine préalable pour créer les catégories, ce qui est exactement le cas pour les humains ! On a appris nous-mêmes à distinguer les objets que l’on voit, à savoir que tel animal est un chat et tel autre est un chien. 
 
![Capture](https://user.oc-static.com/upload/2017/05/12/14946001500306_P3C1-2.png)

Le clustering permet d'identifier des groupes homogènes parmis une population donnée.

#### 2.2.2 Association
La recherche des règles d’association est une méthode dont le but est de découvrir des relations ayant un intérêt entre deux ou plusieurs variables stockées dans de très importantes bases de données. Les algorithmes d’association sont particulièrement adaptées pour explorer des bases de données volumineuses ou complexes. Par exemple, ils peuvent identifier la probabilité de co-occurrence d’éléments dans une collection de données.
 
Quelques exemples
•	Association entre alimentation et apparition de maladies
•	Association entre génotype et phénotype
•	Association entre activations de neurones et comportement

#### 2.2.2 Réduction de dimensions
Un second cas d’apprentissage non supervisé concerne la réduction de dimensions. Imaginons que l’on dispose d’un volume d’informations très conséquent, réparti sur un grand nombre de variables, par exemple pour une population humaine l’âge, le poids, la taille, la durée de trajet quotidienne moyenne, le niveau de revenu, le pays de résidence, le nombre d’enfants à charge, la consommation de lait par an… On cherche à déterminer quelles sont les variables les plus explicatives afin de simplifier le problème tout en conservant le maximum d’information. Supposons que nous disposions de trois quantités seulement pour chaque observation, et que nous représentions notre échantillon sur trois axes correspondant. Supposons enfin que les points se répartissent à l’intérieur d’un volume en forme de galet, assez plat et plus long que large :
 

Si l’on réduit naïvement le nombre de variables en en choisissant deux, par exemple les deux axes du « fond » on perdra une quantité importante d’information sur notre nuage (assimilable à l’ombre portée). En revanche, si on effectue une rotation des axes de manière à « redresser » notre galet, l’information s’en trouve représentée différemment :
 

Cette rotation des axes revient à construire de nouvelles variables par combinaison des variables originales. Grâce à elles, nous avons une représentation plus « nette » du galet, et nous pouvons choisir de retenir préférentiellement les variables qui représente le mieux notre nuage de points : par exemple, en choisissant de ne retenir que deux variables parmi trois, on pourra choisir successivement  le « plancher », puis le « fond » et enfin le « mur de gauche » pour le décrire.
C’est ce que vont rechercher à faire des techniques comme l’analyse factorielle ou l’analyse en composantes principales : trouver des variables composites (des axes) qui portent le maximum d’information, et permettre de n’en garder que quelques-unes pour concentrer l’analyse elles, en considérant la petite perte d’information comme du « bruit » dans la représentation simplifiée ainsi obtenue.
Cette technique trouve son intérêt dans un certain nombre d’applications comme la visualisation de données complexes (typiquement en deux dimensions), la compression avec perte, mais également… la sélection des caractéristiques les plus pertinentes.

### 2.3 Par renforcement

Le reinforcement learning ou l’apprentissage par renforcement (RL) est la science de la prise de décision. Il s’agit d’apprendre le comportement optimal dans un environnement donné pour obtenir une récompense maximale. Ce comportement optimal s’acquiert par des interactions avec l’environnement et l’observation de ses réactions.
Le problème du reinforcement learning implique qu’un agent explore un environnement inconnu pour atteindre un objectif. Le RL est basé sur l’hypothèse que tous les objectifs peuvent être décrits par la maximisation de la récompense cumulative attendue. L’agent doit apprendre à sentir et à perturber l’état de l’environnement en utilisant ses actions pour obtenir une récompense maximale.
Un agent dans un état actuel S apprend de son environnement en interagissant avec ce dernier par le moyen d’actions. Suite à une action A, l’environnement retourne un nouvel état S’ et une récompense R associée, qui peut être positive ou négative.
 
 
 ![Capture](https://lh3.googleusercontent.com/WqC7aJGjWkjoU4wIjch0WH7ipBKJU1lbnX_-xVHh-zAsH2woxUBN92ug6yJ5mUi3Mpj1CMvg6X4YR9En1PoECUcEbom3wQ6K8fEk0wjUiedOLxwBxoaTjXhpIxbGrddivgoMJxfA)

Le Reinforcement Learning a affiché des performances spectaculaires ces dernières années, en permettant à des programmes d’apprendre par eux-mêmes, dans des environnements complexes, des stratégies extrêmement puissantes et robustes. Sous l’impulsion de DeepMind, ces algorithmes ont révolutionné l’intelligence artificielle dans de nombreux domaines, notamment dans le domaine des jeux,  allant des jeux d’arcade (Agent57) et des jeux de plateau (AlphaGo), jusqu’aux jeux-vidéos (AlphaStar).
 
![Capture](https://cdn.futura-sciences.com/buildsv6/images/mediumoriginal/d/3/4/d34887ec89_107368_alphago-kejie.jpg)

