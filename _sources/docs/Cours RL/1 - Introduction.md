# Introduction au Reinforcement learning
Vous êtes un joueur capable d'interagir avec un environnement.
Vous voulez jouer les meilleurs coups à chaque fois que c'est à vous de prendre une décision.
La seule chose qui vous intéresse, c'est qu'à la fin de la partie vous ayez le meilleur score possible.

**Comment faire pour choisir les meilleurs coups ?**

Ce cadre ne se limite pas qu'aux jeux. Dès lors que vous avez une série de décisions à prendre,
il est envisageable de vouloir apprendre quels sont les choix optimaux à chaque étape du processus.
Cependant, l'exemple du jeu d'échecs ou d'un jeu vidéo de manière générale est un exemple d'application
très parlant.

Il peut être extrêmement difficile de trouver des règles permettant de trouver l'action optimale à chaque fois.
Comment décider du meilleur coup aux échecs ? Une méthode serait de tester toutes les possibilités et de voir
quelle est le coup qui a le plus de chance de mener à la victoire par la suite. Cependant ce genre de méthodes
ne fonctionne pas bien en pratique car le nombre de coups possibles est bien trop élevé lorsque l'on considère
tous les coups suivants.

Lorsqu'il est difficile de donner un algorithme précis pour résoudre une tâche, il peut être intéressant
de se pencher vers les techniques de machine learning, et c'est ce que nous allons faire !

Un premier angle d'attaque intuitif pour apprendre à un agent les coups optimaux serait d'utiliser une méthode
de `supervised learning`. Il nous faudrait alors un ensemble de couples de données (état du plateau d'échec, mouvement d'une pièce).
Mais alors survient un deuxième problème : comment récolter un tel jeu de données ? On pourrait récolter des
coups de joueurs professionnels. Cette façon de procéder se nomme `imitation learning`. Elle a cependant quelques défauts:

* Les coups des professionnels ne sont pas forcément optimaux
* Il existe des environnements pour lesquels aucun coup optimal (ou plus simplement bons) n'est connu

Pour illustrer le dernier point, imaginons que vous voulez que votre agent apprenne à marcher.
Votre environnement ici est simplement une liste d'informations sur la disposition de ses membres,
la position de son centre de gravité et peut être une information sur la force de gravité qui s'applique sur son corps.
Comment trouver à un instant précis quel est le déplacement optimal de ses membres afin que l'agent ne tombe pas
par terre et qu'il avance en avant ?

C'est alors qu'entre en scène le **reinforcement learning**. Cette méthode d'apprentissage se distingue des autres
paradigmes car ici l'agent apprend activement. L'agent interagit avec l'environnement et apprend grâce à ses
interactions et aux retours que lui fournissent celles-ci. A chaque décision, l'agent reçoit une récompense
et apprend petit à petit comment maximiser la somme des récompenses finales obtenues. Ainsi,
nous n'avons plus besoin de donner les coups optimaux, **c'est l'agent qui apprend les coups optimaux tout seul**.

Les enjeux principaux deviennent alors:

* La création d'un environnement dans lequel un agent peut interagir
* Le choix des récompenses à donner en fonction du coup de l'agent et de l'état de l'environnement

Le problème peut alors être bien plus simple à modéliser. Simuler une partie d'échec n'est pas trop compliqué.
Donner une récompense de +1 lorsque l'agent gagne la partie, et -1 lorsque l'agent perd la partie est simple.
D'autres challenges apparaissent, mais ce paradigme a eu le temps de maturer et il existe maintenant des
algorithmes d'entraînement solides permettant de faire face à ces challenges.

Comment entraîner un agent à partir de ses interactions ? Quelles sont les limites de ce mode d'entraînement ?
Comment choisir les récompenses ? Quels sont les challenges auxquels il faut faire face ?
L'étude de ces questions est exactement le sujet du reinforcement learning !

### Prérequis
Statistiques, optimisation, algèbre (pour les NNs).

## Présentation
Définitions plus rigoureuses des termes principaux.
Environnement, agent, récompense, policy, value functions.
Comment intéragissent ces différents concepts, schéma général.
Markov Decision Processus.

Présentation des challenges principaux (choix des récompenses, exploration vs exploitation,
dynamique de l'environnement, off/on policy, function approximator).

Les grandes méthodes d'apprentissage RL :

* Value based : la policy est choisie à partir de value functions
    * Immediate RL : k-armed bandit problem, pas de planification
    * Dynamic programming : dynamiques de l'environnement connues
    * Monte Carlo : épisodes d'entraînement finis
    * Temporal difference : bootstrapping, n'attends pas la fin d'un épisode pour apprendre
* Policy based : la policy est directement apprise
    * Policy gradient
    * Model free/model based

## Ressources principales
Ce cours est inspiré par le [cours de Polytechnique Montréal](https://chandar-lab.github.io/INF8953DE/).
La référence principale est [le livre de Sutton & Barto](http://incompleteideas.net/book/the-book-2nd.html),
disponible gratuitement en ligne.
