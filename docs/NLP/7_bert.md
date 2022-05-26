## BERT - Bidirectional Encoder Representations from Transformers

BERT est un modèle de représentation du langage développé par Google AI Language.
Il est capable de traiter plusieurs phrases comme un ensemble de tokens et
produit des embeddings pour chacun d'eux.

La force de ce type de modèle réside dans sa capacité à produire des embeddings universels de bonne qualité.

## Modèle de représentation du langage

Un modèle de représentation du langage transforme une phrase en une représentation abstraite de la phrase qui peut être utilisée pour une variété de tâches :

* Reconnaissance d'entités nommées : Étant donnée une phrase, classer les mots de la phrase (en choisissant parmi un ensemble de labels prédéfinis).
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
De plus, on peut utiliser des tokens spécifiques en input, comme par exemple un token `[CLS]` ayant pour but de classifier l'ensemble de
l'input (cf. Fonctionnement BERT).

Une étape de fine-tuning est souvent nécessaire afin de spécialiser le modèle à la tâche souhaitée.

### Fonctionnement de BERT :

1. Input BERT : Une phrase = séquence de tokens.
2. Output BERT : un état caché final par token en input.

### Couche de sortie supplémentaire spécifique à la tâche :

1. Classification au niveau des phrases (par exemple, analyse des sentiments).
Pour ce faire, il faut ajouter un token spécial `[CLS]` en input. On peut ensuite brancher une couche finale de classification en sortie
sur l'embedding qu'a associé BERT à ce token.

2. Classification au niveau du token (par exemple, la reconnaissance des entités nommées), similaire à la classification au niveau de la phrase, sauf qu'au lieu de faire une seule prédiction en utilisant le token masqué `[CLS]`,
une prédiction est faite pour chacun des états cachés finaux correspondant aux labels associés aux différents tokens.

## Quelle est la particularité de BERT ?

Il utilise un modèle de représentation du langage profond bidirectionnel.

### Différentes approches de la représentation du modèle de langage :

1. Sans contexte :  
    * Chaque mot d'une phrase est transformé en un embedding de mots qui est indépendant du contexte.

       La représentation sans contexte d'une phrase est une séquence d'embeddings de mots.

       Le mot "avocat" dans la phrase "Je mange un avocat" et le mot "avocat" dans la phrase "Je vais faire appel à mon avocat" ont la même représentation par embedding de mots.

2. Contextuel :  

    * Unidirectionnelle : La représentation d'une phrase dépend du contexte ("de gauche à droite").
       La représentation contextuelle de chaque mot dans une phrase est impactée par les mots précédents mais pas par les mots suivants.
    * Bi-directionnel peu profond : La représentation d'une phrase est dépendante du contexte.
       La représentation unidirectionnelle de gauche à droite d'une phrase est combinée avec la représentation unidirectionnelle de droite à gauche pour former la représentation finale.
    * BERT (Deep Bi-directional) : La représentation d'une phrase dépend du contexte.
       Tous les mots (tokens) d'une phrase sont considérés en même temps.
       La représentation contextuelle de chaque mot de la phrase est influencée par les mots précédents ET les mots suivants. Maaaagique ! 🪄🧙


### Comment entrainer un modèle de langage bidirectionnel profond ?

### Fonctionnement global

Le modèle est pré-entraîné de manière non-supervisée sur un très grand ensemble de textes.
Le modèle BERT repose sur deux procédés lors de sa phase de pré-entrainement : *Next Sentence Prediction* (NSP) et *Mask Language Modeling* (MLM) que nous présenterons par la suite.

Le NSP est une tâche de classifiction binaire où le modèle doit prédire si une phrase est la suivante d'une autre.
Le MLM demande au modèle de prédire les mots manquants d'une phrase. Chaque mot manquant est remplacé dans la phrase par un token `[MASK]`.

Bien que le NSP (et le MLM) soient utilisés pour pré-entraîner les modèles BERT,
nous pouvons utiliser ces méthodes exactes pour affiner nos modèles afin de mieux comprendre le style spécifique de la langue dans des uses cases précis.
*Je ne comprends pas cette phrase ?* => *ça fait référence au tranfert learning. BERT a été pré-entrainé sur des tâches de NSP / MLM, je voulais préciser que l'on peut réutiliser ces méthodes sur des tâches précises (NER, analyse de sentiment etc .) en fonction d'une langue donnée.*

#### Fonction de perte (MLM)

Cas profond bidirectionnel (BERT) :

* (Contexte) `Le viewer_1 est [MASK] mais le viewer_2 est mécontent.`

* Tâche de classification : prédire le ou les tokens cibles (`[MASK]`) avec le contexte en entrée.

* Un token choisi au hasard est masqué et le modèle essaie de retrouver le token en se basant sur le contexte.

* La fonction de perte est la log-vraisemblance moyenne de la classification MLM.

#### Prédiction de la phrase suivante (NSP) :

* Choisir deux phrases dans le corpus et les concaténer.
* Les phrases concaténées sont données en entrée au modèle.
* Etiquette NSP = 1 si B suit A dans le corpus de texte
* Label NSP = 0 si B est une phrase choisie au hasard dans le corpus. 
* L'ensemble d'entraînement est construit de telle sorte qu'il y ait 50% de chaque étiquette.
* Tâche de classification binaire : déterminer si B suit A ou non.
* Calculer le score de classification (= score NSP) 

### Exploitation du modèle

Le modèle pré-entraîné peut-être utilisé directement ou alors être fine-tuné pour des tâches spécifiques.
Son pré-entraînement et son architecture très malléable le rend très performant même si on l'utilise pour autre chose que
pour des tâches de NSP et MLM.

Son cas d'utilisation le plus classique est de créer les embeddings des tokens de vos textes. Il n'est pas nécessaire de fine-tuner le modèle pour ce faire.
En revanche, si vous voulez faire du sentiment analysis par exemple, vous aurez besoin de fine-tuner le modèle afin qu'il s'adapte au nouveau rôle
du token `[CLS]`. Ce faisant, vous changerez la façon dont le modèle traite une phrase et la façon dont il va contextualiser le token `[CLS]` avec le reste des tokens.