# Embeddings : comment les machines comprennent les mots ?

0. ["Pré-requis"](#prerequis)
1. ["Comprendre" versus "Lire un texte"](#introduction)
2. [Vecteurs de mots](#vecteur2mots)
    1. [One-hot representation](#1-hot-representation)
    2. [word2vec](#word2vec)

## "Pré-requis" <a name="prerequis"></a>

Avant de commencer cette section, veillez à bien avoir suivi au préalable le module de Machine Learning (notamment les principes généraux et la partie feature engineering).

## "Comprendre" versus "Lire un texte" <a name="introduction"></a>

Depuis longtemps, les machines sont capables de représenter des caractères, des mots, des phrases de manière numérique. L'idée d'utiliser un système de codage binaire pour le langage et la communication remonte au moins à l'invention du télégraphe au XIXe siècle.

L'une des premières formes de codage des langues était le code Morse. Dans ce système, des signaux binaires, comme l'allumage et l'extinction d'une lumière ou l'envoi d'une séquence d'impulsions audio longues et courtes, étaient utilisés pour représenter différents caractères.

Il s'agissait de l'une des méthodes les plus anciennes et les plus simples pour intégrer le langage humain naturel dans un format binaire avec lequel les machines pouvaient travailler d'une certaine manière.

Depuis, de nombreuses améliorations ont été apportées à notre capacité à coder le texte/langage. Il s'agit notamment des enregistrements audio, des nouveaux algorithmes d'encodage tels que l'ASCII, qui utilise un nombre entier pour représenter le texte, et l'Unicode, qui nous permet d'utiliser les caractères de nombreuses écritures différentes.

Votre disque dur n'aura aucun mal à épeler "defend intelligence" un million de fois avec une précision parfaite. Mais pendant la plus grande partie de leur histoire, les ordinateurs n'ont pas été capables de comprendre que le mot "pomme" peut être à la fois une entreprise technologique dont la capitalisation boursière atteint des milliards de dollars et un fruit rouge ou vert juteux.

Lorsque nous voyons un texte, nous voyons plus que l'information brute qui nous est présentée. Les connaissances que nous avons accumulées au fil du temps donnent un contexte supplémentaire aux choses que nous lisons, ce qui rend le langage et la communication significatifs et efficaces.

Il est normal que les ordinateurs ne puissent pas comprendre le texte pour construire des choses intéressantes. 

Plusieurs systèmes de NLP basés sur des approches dites *rules-based* étaient alors jusque là utilisées.
Mais ce type de système basé sur des règles codées en dur est très fragile et ne se généralise pas bien.

A l'inverse des chiffres qui sont dotés de multiples propriétés mathématiques, les mots se prêtent mal à des traitement par des algorithmes. Il faut donc passer par des représentations numériques.

## Vecteurs de mots <a name="vecteur2mots"></a>

Pour récapituler : nous savons que nous pouvons coder du texte brut avec précision en utilisant des méthodes établies comme l'ASCII et l'Unicode. Cependant, nous avons remarqué que le fait de disposer du texte brut ne suffit pas pour créer des modèles NLP. Nous avons donc besoin d'un moyen d'établir une correspondance avec des chiffres qui codent le sens des mots plutôt que l'information brute.

### One-hot representation <a name="1-hot-representation"></a>

Etant donnée un corpus de texte, nous distinguerons l'ensemble des mots distincts du texte. On se donne une taille maximale N de vocabulaire. Les N-1 mots les plus fréquents du corpus sont indexés par ordre alphabétique. Les autres mots pouvant être attribués au token "OTHER"

```python
>>> from sklearn.feature_extraction.text import CountVectorizer

>>> text = ["""
Les Français prennent dès le coup d'envoi le contrôle du milieu de terrain. Dès la troisième minute, Stéphane Guivarc'h, sur une passe de Zinédine Zidane, obtient une occasion de but mais ne cadre pas son tir.

Alors que le match tend à s'équilibrer et que le Brésil se procure plusieurs occasions de buts (notamment un centre au-dessus de la transversale de Roberto Carlos à la 20e minute et une tête de Rivaldo à la 24e minute), les Bleus remettent la pression sur leur adversaire. À la 27e minute, à la suite d'un coup de pied de coin concédé par Roberto Carlos, l'Équipe de France inscrit un but : sur un tir d'Emmanuel Petit, Zinédine Zidane, à 6 m au premier poteau, place une tête piquée en extension au centre du but.

Le gardien français Fabien Barthez réalise une sortie spectaculaire à la 30e minute en passant au-dessus de Ronaldo dans un choc avec l'attaquant brésilien. Alors que la première mi-temps se termine, l'équipe de France inscrit un deuxième but, à nouveau sur corner : tiré par Youri Djorkaeff, le ballon est dévié dans le but brésilien par Zinédine Zidane au premier poteau, lequel se retrouve démarqué à la suite de la glissade de Dunga. 
"""]

>>> count_vect = CountVectorizer(max_features=None)
>>> count_vect.fit(text)

>>> len(count_vect.vocabulary_.values())

109

>>> count_vect.get_feature_names_out()[:20]

array(['20e', '24e', '27e', '30e', 'adversaire', 'alors', 'attaquant',
       'au', 'avec', 'ballon', 'barthez', 'bleus', 'brésil', 'brésilien',
       'but', 'buts', 'cadre', 'carlos', 'centre', 'choc'], dtype=object)

>>> count_vect.vocabulary_.get(u'barthez')

10

>>> print(count_vect.transform(['barthez']).toarray()[0])

[0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]

```

### Word2Vec <a name="word2vec"></a>

Notre espace de représentation obtenu avec la méthode one-hot est de très grande dimentionalité étant donné qu'il dépend de la taille de notre vocabulaire.

De plus, il ne tient pas compte de l'encapsulation du sens du texte. Plusieurs algorithmes proposent de construire une représentation qui encapsule le sens, correspondant à la notion 'embeddings', et en particulier de l'algorithme word2vec.

L'algorithme a été introduit dans deux articles principaux

- Mikolov, T., Sutskever, I., Chen, K., Corrado, G. S., & Dean, J. (2013). Distributed representations of words and phrases and their compositionality. In Advances in neural information processing systems (pp. 3111-3119).

- Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). Efficient estimation of word representations in vector space. arXiv preprint arXiv:1301.3781.

Plusieurs versions et architectures de l'algorithme existent : L'architecture Skip-Gram cherche à prédire les mots dans le contexte de la cible. A l'inverse l'architecture CBow cherche à prédire un mot en fonction de son contexte.

Différents articles par la suite dans le cadre de ce guide de NLP seront réalisés pour vous présenter ces algorithmes en détails.

On remarquera que plusieurs versions de l'algorithme sont disponibles sur le net en utilisant la libraire gensim.

`pip install --upgrade gensim`


## Sources

- https://eu.udacity.com/course/deep-learning--ud730
