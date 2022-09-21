Plus un modèle d'**Intelligence artificielle** rencontre des données, plus il peut devenir intelligent. En ce sens, les modèles d'**IA**se nourrissent de **Big Data**, tout comme les cerveaux humains **sont** formés par les données accumulées grâce **à** de multiples expériences.

C’est dans ce contexte que cette partie du cours décrit de manière synthétique ce que peut apporter la valorisation des données au service de l’intelligence artificielle.

# Chapitre 1 – Eléments de définition

Avant de plonger dans le monde passionnant des Big Data, ce chapitre introductif définit ainsi quelques éléments de définition de l’or noir du 21ème siècle : la donnée !

## 1.1 - Un peu d’histoire

En informatique, les données sont  des informations qui ont été traduites sous une forme efficace pour le mouvement ou le traitement. Par rapport aux ordinateurs et aux supports de transmission d'aujourd'hui, les données sont des informations converties sous  forme numérique binaire. Il est acceptable que les données soient utilisées comme sujet singulier ou comme sujet pluriel. Les données brutes sont un terme utilisé pour décrire les données dans leur format numérique le plus élémentaire.

Le concept de données dans le contexte de l'informatique trouve ses racines au milieu du 20 sicèle dans les travaux de Claude Shannon, un mathématicien américain connu comme le père de la théorie de l'information. Il a inauguré des concepts numériques binaires basés sur l'application de la logique booléenne à deux valeurs aux circuits électroniques. 

Très tôt, l'importance des données dans l'informatique d'entreprise est devenue évidente par la popularité des termes « traitement des données » et « traitement électronique des données », qui, pendant un certain temps, en sont venus à englober toute la gamme de ce que l'on appelle aujourd'hui les technologies de l'information . Au cours de l'histoire de l'informatique d'entreprise, une spécialisation s'est produite et une profession de données distincte a émergé parallèlement à la croissance du traitement des données d'entreprise.

## 1.2 - Qu’est-ce qu’une donnée ?

La plupart d’entre nous ne manipulent pas des données pour leur simple plaisir, certains en manipulent sans même le savoir. Elles sont utilisées à dessein ou pour rendre visible des phénomènes.

Vous commencerez la plupart du temps à partir d’une problématique de type : «Combien de fois le soleil brille dans ma ville natale?» ou «Comment mon gouvernement dépense-t-il son argent? Et d’où proviennent les fonds? ». Une question est un bon point de départ pour explorer des données, cela permettra de préciser votre recherche et vous aidera à détecter des tendances intéressantes. Comprendre qui seront les personnes intéressées par votre problématique vous aidera également à définir le public auquel vous vous adressez, et vous aidera à modéliser votre projet.

Quelle que soit votre problématique, vous devez toujours rester attentif aux observations inattendues, aux résultats inhabituels, ou à tout ce qui pourra vous surprendra. Souvent, les phénomènes les plus intéressants ne sont pas ceux que vous recherchez.

Les données sont donc omniprésentes autour de nous. Mais qu’est-ce exactement qu’une donnée ? On va partit sur un exemple simple : des balles de tennis

![image](https://user-images.githubusercontent.com/55838700/191488104-cdb20cd1-1f5f-42c1-b17f-f9bfd9f618e8.png)

Que pouvons nous en dire ? Ce sont des balles de tennis. L’une des premières choses que l’on sait est donc qu’elles sont utilisées pour jouer… au tennis. Par ailleurs, le tennis est un sport, qui peut être individuel ou collectif ce qui nous permet de placer la balle de tennis dans une ou plusieurs **taxonomies (classifications)**

Même les objets d’apparence banale révèlent en réalité une quantité de données importantes qui leurs sont attachées. Vous aussi, vous avez un nom de famille, une date de naissance, un poids, une taille, une nationalité, etc. Toutes ces choses, éléments sont des données.


Dans l’exemple ci-dessus, nous pouvons déjà constater qu’il y a différents types de données. Il y a principalement des données **qualitatives** et des données **quantitatives**.

- Les **données qualitatives** se réfèrent à la qualité : La description d’une couleur, de textures et l’aspect d’un objet, la description d’une expérience sont toutes des données qualitatives. Par exemple, nos balles de tennis sont sphériques et jaunes.
- Les **données quantitatives** sont des données qui se réfèrent aux chiffres. Ex : Le nombre de balles de tennis, la taille, le prix, le nombre de jongles maximum avec cette balle.

Cependant, vous allez rencontrer d’autres types de données :

- Les **données catégorielles** permettent de classer les objets que vous traitez par catégories. Dans notre exemple, l’aspect « usagé » serait une catégorie au sein de la typologie suivante : « nouveau », « usagé », « cassé », etc.
- Les **données discrètes** sont des données dénombrables. Ex: le nombre de balles de tennis. Il ne peut y avoir qu’un nombre entier de balles de tennis  (il ne peut pas y avoir 0,3 balles de tennis). Le résultat d’un test ou une pointure de chaussure constituent d’autres exemples.
- Les **données continues** sont des données numériques non entières. Ex: le diamètre des balles de tennis (ex: 6,30 cm, 6,50 cm, 6,60 cm), ou la taille précise de votre pied (en opposition à la pointure, qui elle est discrète). Toutes les valeurs sont admises.

![image](https://user-images.githubusercontent.com/55838700/191488169-1b2f6700-69ae-4d50-b5b7-de33b8bc6017.png)

Quand elles sont collectées et structurées, les données deviennent très utiles. Structurons les dans le tableau ci-dessous :

|Couleur|Jaune|
| :- | :- |
|Catégories|Sport, Tennis|
|État|Usagé|
|Diamètre|635 mm|
|Prix (par balle)|2,50 €|

Mais ces données n’ont pas de sens exploitées individuellement. Pour faire émerger l’information, nous devons les interpréter.

Prenons la taille : Un diamètre de 630 mm ne signifie rien. Il devient intéressant quand il est comparé à une autre donnée, un autre diamètre. Dans certains sports, il y a une réglementation pour les équipements. La taille minimale d’une balle de tennis en compétition est de 63,5 mm. Nous ne pouvons donc pas utiliser cette balle en compétition. C’est une information. En revanche, ce n’est toujours pas de la connaissance. La connaissance est créée lorsque l’information est apprise, appliquée et comprise.

## 1.3 - Données non structurées contre données structurées

### 1.3.1 - Les données non-structurées

« Il y a 5 balles de tennis usagées avec un diamètre de 64 mm à 0,5 € chacune » est une phrase facilement compréhensible pour un humain, mais compliquée à comprendre par un ordinateur. La phrase ci-dessus est considérée comme de la donnée non structurée. Elle n’a pas de structure sous-jacente. La tournure de la phrase pourrait être changée et il n’est pas évident de déterminer quel mot correspond à quelle donnée. De la même manière, les PDFs et les images peuvent contenir des informations interprétables par l’oeil humain, mais ne pas être compréhensibles par un ordinateur.

### 1.3.2 - Les données structurées

Les ordinateurs sont fondamentalement très différents des humains. Il peut être extrêmement difficile pour une machine d’extraire des données provenant de certaines sources. Certaines tâches facilement réalisables par un individu sont encore difficilement exécutables par les machines. Par exemple, l’interprétation d’un texte encapsulé dans une image est toujours un défi pour l’ordinateur. Si l’on veut que l’ordinateur analyse la donnée, il faut qu’il soit capable de la lire et de la traiter. **Ce qui signifie qu’elle doit être structurée dans un format lisible par la machine.**

L’un des formats les plus couramment utilisé pour l’échange de données est le format CSV. Le CSV sépare les données par des virgules. De la donnée transcrite en CSV pourrait ressembler à cela :

“quantité”, “couleur”, “condition”, “objet”, “catégorie”, “diamètre(mm)”, “prix unitaire (€)” 5,”jaune”,”usagé”,”balle”,”tennis”,65,0.36

C’est un format simplifié pour l’ordinateur et lisible par des tableurs. Vous noterez que les mots sont entourés de guillemets, ce qui les distingues en tant que texte (chaîne de caractères dans le langage informatique), alors que les nombres n’ont pas de guillemets. À noter qu’il existe beaucoup d’autres formats structurés et lisibles par une machine.

![image](https://user-images.githubusercontent.com/55838700/191488285-aae2acb8-cafe-4032-9e09-091bf0acd60f.png)

## 1.4 - Comment collecter des données ?

Les données peuvent être collectées de plusieurs façons. Le moyen le plus simple est l'observation directe.

**Exemple : Compter le nombre de voitures sur la route** 

![image](https://user-images.githubusercontent.com/55838700/191488349-34cf10dc-d899-4d49-8850-a85f3fa2a26b.png)


Vous voulez savoir combien de voitures passent à un certain point sur une route dans un intervalle de 10 minutes.

Donc : placez-vous près de cette route et comptez les voitures qui passent en 10 minutes.

Vous voudrez peut-être compter de nombreux intervalles de 10 minutes à différents moments de la journée et à différents jours également !

Nous recueillons des données en faisant une enquête.
## **Recensement ou échantillon**
Un **recensement** consiste à collecter des données pour **chaque** membre du groupe (l'ensemble de la "population").

Un **échantillon** est lorsque nous recueillons des données uniquement pour **les membres sélectionnés** du groupe.
### **Exemple : Echantillon de 100 voitures sur la route**
Vous pouvez demander (toutes les 100 voitures) quelle est leur marque. C'est un recensement.

Ou vous pouvez simplement choisir les voitures qui seront sur la route uniquement l’après-midi. C'est un échantillon.

Un recensement est précis, mais difficile à faire. Un échantillon n'est pas aussi précis, mais peut être assez bon, et c'est beaucoup plus facile.

## 1.5 - Une fois les données collectées, il faut les stocker.

Le stockage, mais aussi la sauvegarde, de ses données peut très vite s’avérer comme un véritable casse-tête si l’on ne maîtrise pas cette notion importante de l’informatique.

Tous les contenus que l’on crée ou que l’on télécharge sur ses machines, ordinateurs, tablettes, smartphones et autres objets connectés, que ce soient des photos, des lettres, des documents administratifs, des factures et j’en passe… doivent être stockés pour les utiliser.

Le stockage fait référence à des méthodes et technologies utilisées pour stocker des données numériques. Cela s’applique à tous les différents types d’appareils numériques, et pour cela des supports bien connus comme les disques durs, les clés USB et quantité d’autres moyens sont à notre disposition.

Le disque dur est un élément indispensable de votre machine. C’est là que tout est stocké : le système d’exploitation, les applications et vos fichiers personnels eux y sont stockés automatiquement si l’appareil a été configuré pour.

Examinons ci-après quelques formats de stockage des données, du simple fichier texte aux bases de données sophistiquées :

- Vous avez déjà joué à un jeu sur un ordinateur ou une tablette ? De nombreux jeux informatiques gardent la trace de vos meilleurs scores pour vous aider à mesurer vos progrès personnels.

Un jeu peut enregistrer vos meilleurs scores dans un **fichier texte** sur l'ordinateur.

Ce fichier peut être aussi simple que celui ci-dessous listant les scores sur 100 d’un joueur.

![image](https://user-images.githubusercontent.com/55838700/191488501-81c09e87-5322-4a73-89f1-ff5ba0a63d27.png)

Et si le jeu souhaite également enregistrer la date du meilleur score et le niveau atteint ? Chaque ligne du fichier devra stocker plusieurs éléments d'information connexes. Nous appelons cela des données "tabulaires", car chaque ligne est comme une ligne d'un tableau et chaque ligne comporte plusieurs colonnes.

- Un autre format courant pour stocker des données tabulaires dans des fichiers texte est le format **CSV (comma-separated values)**.

![image](https://user-images.githubusercontent.com/55838700/191488560-c21cd771-0703-4f23-a0ee-1eca103807ac.png)

La première ligne du fichier déclare les colonnes "date", "level » et « score ». Les lignes suivantes contiennent les lignes de données réelles, avec la date en premier, puis le niveau, puis le score, tous séparés par des virgules.

Les fichiers CSV sont un format courant, et il existe donc de nombreux outils capables de lire et d'écrire des fichiers CSV. Certains de ces outils sont destinés à l'utilisateur, comme les tableurs. Pour les développeurs, il existe des bibliothèques dans les langages de programmation pour lire et écrire des fichiers CSV à partir de leurs applications.

- **Un tableur** est un outil permettant de stocker, d'organiser et d'analyser des données. Les tableurs peuvent généralement ouvrir une variété de formats de fichiers texte populaires (comme CSV, TSV et XLS) et enregistrer les données dans ces formats.

![image](https://user-images.githubusercontent.com/55838700/191488643-84728f32-d4d1-4881-a810-f32b31d440d4.png)

Cependant, les applications n'utilisent pas les feuilles de calcul comme mécanisme de stockage des données, car une application de feuille de calcul est un outil pour les personnes, pas pour les programmes.

- La plupart des applications stockent des données dans **une base de données**, un système qui stocke des données sur un ordinateur de manière à pouvoir y accéder, les mettre à jour, les interroger et les supprimer facilement.

Une base de données stocke également les données dans des fichiers. Cependant, le système de gestion de la base de données s'occupe de tous les détails pour nous, comme la division des données en fichiers de taille appropriée et la mémorisation des données stockées dans chaque fichier.

Pour interagir avec la base de données, en tant que programmeurs ou analystes de données, nous utilisons souvent un langage d'interrogation. Le langage d'interrogation le plus populaire est le SQL (Structured Query Language).

![image](https://user-images.githubusercontent.com/55838700/191488729-81e04172-625f-43df-94df-63a20ed03bc5.png)

Il existe également des systèmes de stockage qui fonctionnent avec une connexion internet. Aujourd’hui le **Cloud** à le vent en poupe par exemple.Avec le Cloud, il devient très simple de partager ses documents d’un simple clic ou via des outils de communication comme Gmail par exemple.
Cet outil fonctionne avec une connexion internet, il dispose d’une bonne capacité de stockage mais reste la plupart du temps payant dés lors que l’on augmente sa capacité de stockage, comme les autres moyens de stockage d’ailleurs !

![image](https://user-images.githubusercontent.com/55838700/191488757-7bf5b5d5-53c8-4bc3-980c-9cbd0b92ed0f.png)

L’un des plus connu est Google Drive mais ils en existe des centaines, plus ou moins sécurisés et qui respectent votre confidentialité. Là encore, il va falloir apprendre à les paramétrer !

## 1.6 - Conclusion

Nous avons introduit quelques concepts essentiels, les principaux enjeux qui apparaissent constamment dans les discussions autour de la donnée, l’or noir du 21ème siècle. Dans les prochains chapitres nous rentrerons dans les détails sur comment les données peuvent être modélisées, et nous irons plus loin avec l’avènement des données massives ou « Big Data ». Enfin, nous verrons quelle est la place et comment l’intelligence artificielle arrive à s’imbriquer avec ces données complexes !


