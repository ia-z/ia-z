## BERT

BERT est un modèle de représentation du langage développé par Google AI Language.

## Modèle de représentation du langage

Un modèle de représentation du langage transforme une phrase en une représentation abstraite de la phrase qui peut être utilisée pour une variété de tâches :

* Reconnaissance d'entités nommées : Étant donné une phrase, classer les mots de la phrase (en choisissant parmi un ensemble de labels prédéfinis).
* Réponse à une question (tâche de classification binaire) : Étant donné une question et une phrase, déterminez si la phrase répond à la question.
* Réponse à une question (traditionnelle) : Étant donné une question, trouver dans un corpus textuel la phrase qui répond à la question (marquer son début et sa fin).
* Analyse de sentiment : Étant donné une phrase, déterminer le score du sentiment (score faible = tristesse, score élevé = heureux).
* Acceptabilité linguistique : Étant donné une phrase, déterminer s'il s'agit d'une phrase linguistiquement acceptable.
* Équivalence sémantique : pour deux phrases, déterminez si elles sont sémantiquement équivalentes.

## Objectifs du modèle BERT

1. Pré-entraîner un modèle de représentation du langage qui peut être facilement ajusté pour une variété de tâches.  
2. Rendre le transfer-learning pour le NLP aussi accessible que le transfer-learning pour le Computer Vision (le "ImageNET" du langage naturel).

## Utilisation de BERT pour une tâche spécifique


Pour utiliser BERT pour une tâche spécifique, une couche de sortie spécifique à la tâche doit être ajoutée à l'architecture de base de BERT.

### Fonctionnement de BERT : 

1. Input BERT : Une phrase = séquence de tokens.
2. Output BERT : un état caché final par token en input.

### Couche de sortie supplémentaire spécifique à la tâche :

1. Classification au niveau des phrases (par exemple, analyse des sentiments). Ajoutez une couche finale avec K neurones correspondant aux K classes possibles.

2. Classification au niveau du token (par exemple, la reconnaissance des entités nommées), similaire à la classification au niveau de la phrase, sauf qu'au lieu de faire une seule prédiction en utilisant le token masqué [CLS], une prédiction est faite pour chacun des états cachés finaux correspondant aux labels associés aux différents tokens.

## Quelle est la particularité de BERT ?

Il utilise un modèle de représentation du langage profond bidirectionnel.

### Différentes approches de la représentation du modèle de langage :

1. Sans contexte :  
    * Chaque mot d'une phrase est transformé en un embedding de mots qui est indépendant du contexte (c.f word2vec ou GloVe).

       La représentation sans contexte d'une phrase est une séquence d'embeddings de mots.

       Le mot "avocat" dans la phrase "Je mange un avocat" et le mot "avocat" dans la phrase "Je vais faire appel à mon avocat" ont la même représentation par embedding de mots.

2. Contextuel :  

    * Unidirectionnelle : La représentation d'une phrase dépend du contexte ("de gauche à droite")
       La représentation contextuelle de chaque mot dans une phrase est impactée par les mots précédents mais pas par les mots suivants.
    * Bi-directionnel peu profond : La représentation d'une phrase est dépendante du contexte.
       La représentation unidirectionnelle de gauche à droite d'une phrase est combinée avec la représentation unidirectionnelle de droite à gauche pour former la représentation finale.
    * BERT (Deep Bi-directional) : La représentation d'une phrase dépend du contexte.
       Tous les mots (tokens) d'une phrase sont considérés en même temps.
       La représentation contextuelle de chaque mot de la phrase est influencée par les mots précédents ET les mots suivants. Maaaagique ! 🪄🧙
    

### Comment former un modèle de langage bidirectionnel profond ?

### Fonctionnement global

Le modèle BERT repose sur deux procédés lors de sa phase de pré-entrainement : *Next Sentence Prediction* (NSP) et Mask Language Modeling (MLM) que nous présenterons par la suite.

Bien que le NSP (et le MLM) soient utilisés pour pré-entraîner les modèles BERT, nous pouvons utiliser ces méthodes exactes pour affiner nos modèles afin de mieux comprendre le style spécifique de la langue dans des uses cases précis.

### Optimiser par rapport à une fonction de perte :

La fonction perte de BERT = fonction de perte MLM + fonction de perte NSP.

### Fonction de perte pour l'entraînement d'un modèle de langage traditionnel

Cas unidirectionnel :

* Première étape

  (Contexte) Le viewer_1 est [?] satisfait mais le viewer_2 est mécontent. 
  
  Tâche de classification : prédire [?] en tenant compte du contexte comme entrée.

* Étape 2

  Le viewer_1 (Contexte) est satisfait [?] mais le viewer_2 est mécontent.

  La fonction de perte est la vraisemblance moyenne de cette classification.

### Fonction de perte (MLM)

Cas profond bidirectionnel (BERT) :

* (Contexte) Le viewer_1 est [?] [Token masqué] mais le viewer_2 est mécontent. 

* Tâche de classification : prédire la cible avec le contexte en entrée.

* Un token choisi au hasard est masqué et le modèle essaie de retrouver le token en se basant sur le contexte.

* La fonction de perte est la probabilité moyenne de la classification MLM.

### Prédiction de la phrase suivante (NSP) :

* Choisir deux phrases dans le corpus et les concaténer.
* Les phrases concaténées sont données en entrée au modèle.
* Etiquette NSP = 1 si B suit A dans le corpus de texte
* Label NSP = 0 si B est une phrase choisie au hasard dans le corpus. 
* L'ensemble d'entraînement est construit de telle sorte qu'il y ait 50% de chaque étiquette.
* Tâche de classification binaire : déterminer si B suit A ou non.
* Calculer le score de classification (= score NSP) 

## Liens intéressants : 

## Tutoriels :
* https://colab.research.google.com/github/tensorflow/tpu/blob/master/tools/colab/bert_finetuning_with_cloud_tpus.ipynb

* Publication originale : https://arxiv.org/abs/1810.04805
* https://towardsdatascience.com/bert-explained-state-of-the-art-language-model-for-nlp-f8b21a9b6270
* https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html
* https://lesdieuxducode.com/blog/2019/4/bert--le-transformer-model-qui-sentraine-et-qui-represente