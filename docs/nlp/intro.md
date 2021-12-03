# Traitement automatique du langage naturel - NLP

## La complexité du NLP

- Ambiguïté

Le language est intrinsèquement ambigu, des énoncés peuvent avoir plusieurs interprétations. 

- Variation

Il existe plusieurs manières d'exprimer la même idée. Plusieurs manières de prononcer une même phrase, ou de construire un énoncé.

- Diversité

Il existe des milliers de langues dans le monde.

- Dimension 

Les systèmes de représentations du langage sont souvent de grandes dimensions, due à la taille importante du vocabulaire.

- Distribution

Les fréquences d'utilisations des mots sont très inégales et ils peuvent être combinés de manière infinie pour former des phrases.

## Le périmètre du traitement automatique du language

Le TAL (traitement automatique du langage) est à la frontière entre la linguistique et l'apprentissage automatique.

## Applications 

- Traduction automatique
- Extraction d'information
- Système de Questions - Réponses
- Résumé automatique
- Moteurs de recherche
- Analyse de sentiments

## Technologies

- Part-Of-Speach (PoS) Tagging
- Parsing / Syntaxe
- Entitées Nommées
- Semantic Role Labelling (SRL)
- Language modeling
- Word Sense Disambiguation
- Deep Learning
- Outils statistiques pour le NLP

## Les systèmes symboliques vs statistiques

Ici : Mettre un exemple visuel de système symbolique.

Les systèmes symboliques consistent en un système de règle explicites qui s'appuient sur une expertise linguistique qui imite la perception humaine du langage.

Par exemple, si l'on cherche à extraire les symptômes ainsi leurs date d'apparition, on peut parcourir la structure en dépendances de la phrase et s'appuyer sur les POS-TAGS comme features pour un système de règles précis.

Le développement d'un tel système apporte beaucoup de flexibilité pour ajuster le système de règles en foction d'exemples isolés, sans changer l'approche globale. Le système peut être développé sur des jeux de données de taille réduite.

Néanmoins, ce type d'approche nécessite des compétences de développement et des connaissances de linguistiques évlouées. Par ailleurs, l'addition et l'extension de règles peut rendre le système complexe.

Ici : Mettre un exemple visuel de système statistique.

Les <b>systèmes de machine learning (i.e statistiques)</b>inversent le problème. On ne créer plus des features ou des règles manuellement à partir des exemples. On va proposer un très grand nombre d'exemples au système pour qu'il produise des règles et des features correspondantes au jeu de données.

L'algorithme va calibrer les paramètres des représentations du texte pour attribuer les bons symptômes au plus grand de phrases.

Cette méthode ne nécessite pas de "programmation explicite" mais apprend à modéliser le langage en s'appuyant sur des exemples. Ce type de système permet de développer rapidement des solutions à l'aide de méthodes génériques. L'algorithme apprend seul à se spécialiser pour le cas d'usage. Le temps de développement est généralement réduit.

Le système nécessite un nombre importat d'exemples et un jeu de données conséquent. Il est plus difficile de modifier le système pour classifier correctement des exemples isolés. Les performances sont évaluées de manière agrégées sur un nombre important d'exemples.

## Exemple de jeu de données pour les méthodes NLP statistiques

- Traduction automatique

Pour les systèmes de traduction on dispose de corpus parallèles avec l'expression d'une même phrase dans plusieurs langues.

- Système de Questions/Réponses

Pour les systèmes de Questio / Réponse, on dispose de couple (texte,question). Le passage du texte qui répond à la question est indiqué. Par exemple le jeu de données SQUAD contient 100K exemples.

Source : Pranav Rajpukar, Jian Zhang, Konstatin Lopyrev, Percy Liang : Squad: 100,000+ Questions for Machine Comprehension of Text, EMNLP 2016: 2383-2392

- Résumé automatique

Pour la tâche de résumé automatique, on dispose d'un ensemble de couples (texte,résumé). La taille du résumé peut varier.

Source : Byeongchang Kim, Hyunwoo Kim, Gunhee Kim : Abstractive Summarization of Reddit Posts with Multi-level Memory Networks, NAACL-HLT (1) 2019: 2519-2531

- Analyse de sentiments

Pour l'analyse de sentiment, il s'agit d'une tâche de classification. Le système prend en entrée des couples (phrase,label).

Source :  https://www.kaggle.com//c/sentiment-analysis-on-movie-reviews/overview

## Systèmes symboliques vs statistiques : résumé.

Ici : mettre les principales différences entre système symbolique et statistique sous forme de tableau / pipeline de traitement.

## Définitions

- Le mot w est généralement l'unité de base des systèmes de traitement automatique du langage.

- Un document d est une séquence de N mots notée d = (w1, w2, ... , wN) où wN est le n-ième mot de la séquence.

- Un corpus est une collection de M documents notée D = (d1,d2, ... , dM).

## Représentation des mots

- Création du vocabulaire

Etant donné un corpus, on distingue l'ensemble des différents mots composant le texte. On se donne une taille maximale V de vocabulaire. Les V - 1 mots les plus fréquents du corpus sont indexés par ordre alphabétique. Les autres mots pouvat être attribués au token <UNK> (unknow ou inconnu). La taille de vocabulaire V standard varie entre 50 et 100k mots.

Ici mettre un exemple visuel.

- Représentation "one-hot"

On cherche à associer chaque mot de notre vocabulaire w1,...,wN à une structure de données. La méthode la plus simple à associer chaque mot à un vecteur "one-hot" qui ne contient que des 0,sauf pour la coordonnée correspondant à l'index du mot que l'on assigne à 1.

Ici mettre un exemple visuel.

## Représentation des documents

- Modélisation d'un document

On cherche à associer chaque document à une structure. Chaque document est modélisé par un vecteur "One hot" dont les coordonnées ne peuvent prendre que les valeurs 0 ou 1. Chaque entrée du vecteur correspond à une entrée du dictionnaire. Si le mot est présent dans le document, on attribue la coordonnée 1, sinon on attribue la coordonnée 0.

Ici mettre un exemple visuel.

## Le modèle Bag of Word (BoW)

- Modélisation Bag of Words

Chaque document est modélisé par un vecteur dont les coordonnées correspondent à la fréquence d'occurence de chaque mot. Chaque entrée du vecteur correspond à une entrée du dictionnaire. Si le mot apparait n fois dans le document, on attribue la coordonnée à la valeur n.

Ici mettre un exemple visuel.

- Limites

a) Ne prends pas en compte l'ordre des mots dans un document : "Lactor est plus grand que Rayane" a la même représentation que "Rayane est plus grand que Lactor".
b) Certains mots sont beaucoup plus fréquents que d'autres qui sont pourtant plus caractéristiques du document.
c) La taille des vecteurs de représentation augmente avec la taille du vocabulaire.

## Term Frequency Inverse Document Frequency (TF-IDF)

- Modélisation TF-IDF

Chaque document est modélisé par un vecteur dont les coordonnées correspond à une fonction des occurences de chaque mot dans chacun des documents. Chaque entrée du vecteur correspond à une entrée du dictionnaire. La fonction TF-IDF correspond au produit des deux termes.

- Term Frequency (TF)

Soon.

- Inverse Document Frequency (IDF)

Soon.

- Interprétation de la pondération TF-IDF

Pour un mot donné, le score IDF ne dépend que du corpus tandis que le score TF dépend du document au sein duquel le mot est considéré : le score TF-IDF dépend donc du document considéré. Plus le mot est présent dans le corpus plus son score IDF est pénalisé : les mots communs ont un score TF-IDF faible. Le score TF-IDF va donc privilégier les mots qui sont fréquents dans le document tout en étant peu fréquents dans le reste du corpus.

Soon. Exemple à venir.

Implémentation tuto TF-IDF : scikit-learn / from scratch à faire.
