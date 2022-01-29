# Introduction

Le NLP "Natural Language Processing" t'intéresses ? Tu as entendu parler de BERT, de modèles Transformers, Cedille, tf-idf, skip-gram, cbow, de modèles de langues ou de différents termes mais tu ne sais guère par où débuter ? Tu aimerais pouvoir exploiter des données textuelles pour tes projets perso ?

Cette série de blogs/cours est là pour t'accompagner. Celle-ci te permettra de familiariser avec à ces différentes notions et t'apporter un socle de connaissance solides pour bien débuter en NLP.

Avant de débuter cette aventure, attardons-nous sur des points essentiels relatifs au NLP à avoir en tête tout au long de cette série de cours.

## Les principales caractéristiques du NLP

- Ambiguïté

Le language est intrinsèquement ambigu, des énoncés peuvent avoir plusieurs interprétations.

- Variation

Il existe plusieurs manières d'exprimer la même idée. Plusieurs manières de prononcer une même phrase, ou de construire un énoncé.

- Diversité

Il existe des milliers de langues dans le monde.

- Dimension

Les systèmes de représentations du langage sont souvent de grandes dimensions, due à la taille importante du vocabulaire.

- Distribution

Les fréquences d'utilisation des mots sont très inégales et ils peuvent être combinés de manière infinie pour former des phrases.

## Le périmètre du NLP

Le TAL (traitement automatique du langage) est à la frontière entre la linguistique et le Machine Learning (c.f série la série de cours de Machine Learning).

## Des applications du NLP

- Traduction automatique
- Extraction d'information
- Système de Questions - Réponses
- Résumé automatique
- Moteurs de recherche
- Analyse de sentiments

## Keywords important en NLP

- Part-Of-Speach (PoS) Tagging
- Parsing / Syntaxe
- Entitées Nommées
- Semantic Role Labelling (SRL)
- Language modeling
- Word Sense Disambiguation
- Deep Learning
- Outils statistiques pour le NLP

## Les systèmes symboliques (dit "classiques") vs statistiques en NLP

Si tu as lu la série de cours de Machine Learning, tu as pu te rendre compte de la distinction effectuée entre une programmation dite "classique" reposant sur un système de règles qui diffère avec celle utilisée lorsqu'on fait du Machine Learning reposant sur une approche statistique.

Cette distinction a aussi son importance en NLP.

Ici : Mettre un exemple visuel de système symbolique.

Les systèmes symboliques consistent en un système de règle explicites qui s'appuient sur une expertise linguistique qui imite la perception humaine du langage.

Par exemple, si l'on cherche à extraire les symptômes ainsi leurs date d'apparition, on peut parcourir la structure en dépendances de la phrase et s'appuyer sur les POS-TAGS comme features pour un système de règles précis.

=> Qu'est un POS-TAGS (à expliquer)

Le développement d'un tel système apporte beaucoup de flexibilité pour ajuster le système de règles en foction d'exemples isolés, sans changer l'approche globale. Le système peut être développé sur des jeux de données de taille réduite.

Néanmoins, ce type d'approche nécessite des compétences de développement et des connaissances de linguistiques assez évoluées. Par ailleurs, l'addition et l'extension de règles peut rendre le système complexe.

Ici : Mettre un exemple visuel de système statistique.

Les <b>systèmes de machine learning (i.e statistiques)</b>inversent le problème. On ne créer plus des features ou des règles manuellement à partir des exemples. On va proposer un très grand nombre d'exemples au système pour qu'il produise des règles et des features correspondantes au jeu de données.

L'algorithme va calibrer les paramètres des représentations du texte pour attribuer les bons symptômes au plus grand nombre de phrases.

Cette méthode ne nécessite pas de "programmation explicite" mais apprend à modéliser le langage en s'appuyant sur des exemples. Ce type de système permet de développer rapidement des solutions à l'aide de méthodes génériques. L'algorithme apprend seul à se spécialiser pour le cas d'usage. Le temps de développement est généralement réduit.

Le système nécessite un nombre important d'exemples et un jeu de données conséquent. Il est plus difficile de modifier le système pour classifier correctement des exemples isolés. Les performances de ce système sont évaluées de manière agrégées sur un nombre important d'exemples.

## Systèmes symboliques vs statistiques : résumé.

Ici : mettre les principales différences entre système symbolique et statistique sous forme de tableau / pipeline de traitement.

Tout au long de ce cours, nous allons principalement axé notre approche sur les méthodes dites de NLP statistiques qui représente à notre sens un point d'entrée accessible pour un débutant en NLP sans forcément avoir un background de linguiste.

## Exemple de jeux de données pour les méthodes dites de  "NLP statistiques"

- Traduction automatique

Pour les systèmes de traduction on dispose de corpus parallèles avec l'expression d'une même phrase dans plusieurs langues.

- Système de Questions/Réponses

Pour les systèmes de Question / Réponses, on dispose de couple (texte,question). Le passage du texte qui répond à la question est indiqué. Par exemple le jeu de données SQUAD contient 100K exemples.

Source : Pranav Rajpukar, Jian Zhang, Konstatin Lopyrev, Percy Liang : Squad: 100,000+ Questions for Machine Comprehension of Text, EMNLP 2016: 2383-2392

- Résumé automatique

Pour la tâche de résumé automatique, on dispose d'un ensemble de couples (texte,résumé). La taille du résumé peut varier.

Source : Byeongchang Kim, Hyunwoo Kim, Gunhee Kim : Abstractive Summarization of Reddit Posts with Multi-level Memory Networks, NAACL-HLT (1) 2019: 2519-2531

- Analyse de sentiments

Pour l'analyse de sentiment, il s'agit d'une tâche de classification. Le système prend en entrée des couples (phrase,label).

## Sources

- https://www.kaggle.com//c/sentiment-analysis-on-movie-reviews/overview
