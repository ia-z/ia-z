# Etude des données textuelles

## Sommaire
* [Différences avec les données structurées](#différences-avec-les-données-structurées)
* [Pré-traitements](#pré-traitements)
  * [Stemming](#stemming)
    * [Over Stemming](#over-stemming)
    * [Under Stemming](#under-stemming)
  * [Lemmatisation](#lemmatisation)
  * [Régularisation des expressions](#régularisation-des-expressions)
  * [Supression des Stop Words](#supression-des-stop-words)
  * [Tokenisation](#tokenisation)
* [Exemple de pré-traitement](#exemple-de-pré-traitement)

## Différences avec les données structurées

Tout d'abord nous devons nous intéresser au type de donnée que nous manipulerons tout au long de ce cours, à savoir du texte.

De ce texte découle des mots, des phrases, des langues et des contextes difficilement quantifiable d'un point de vue mathématique, car contrairement aux chiffres le texte n'a pas de relation d'ordre ou d'axiome permettant de le manipuler facilement, or le but d'une donnée structurée est d'avoir une information claire permettant son interprétation et son traitement par des machines.

Cependant le texte suit des régles, qu'elles soient grammaticales ou syntaxiques qui vont nous permettre de le transformer en une donnée structurée par la suite.

Prenons par exemple la construction d'une phrase:

<p align="center">
<img src="https://user-images.githubusercontent.com/65224852/166940035-1d1ed107-06ca-490e-85ed-b95c46b78865.jpg" width=600 height=302>
<br /><i> Oui, entraîner une machine c'est comme apprendre la grammaire à un enfant </i>
</p>

Avec cela nous avons déjà plusieurs catégories pour classer un mot ou un groupe de mots en sujet, verbe, complément...

Nous verrons plus tard que les **transformers**, un modèle de deep learning, sont capable d'analyser le contexte d'une phrase avec un mécanisme d'**attention** et d'utiliser les mêmes régles syntaxiques que celles illustrées ci-dessus.

Mais pour pouvoir travailler sur ces données textuelles il faudra dans un premier temps les *soigner* afin que le modèle sur lequel on souhaite travailler puisse comprendre le jeu de données.

En effet il est difficile pour une machine de comprendre que "est" et "sois" font tous les deux partis du verbe être ou encore qu'une conjonction de coordination n'apporte qu'une vague plus-value à l'information dans un texte lorsque l'on souhaite analyser une page internet rapidement par exemple.

## Pré-traitements

Nous étudierons quelques-uns des pré-traitements les plus courant en NLP:

*(Il est à noter que certains algorithmes ne fonctionnent qu'en anglais)*

### Stemming:
Le Stemming est un procédé permettant de convertir un mot en sa *racine* ou *forme canonique*, par exemple les mots "Chocolaterie", "Chocolatier" ou encore "Choco" seront convertis en "Chocolat", les algorithmes permettant de réaliser une telle conversion sont nommés les Stemmers.

Les Stemmers sont parfois sujet aux erreurs, en particulier:
#### Over Stemming:

Cette erreur intervient lorsque la partie du mot découpée est trop grande pour la racine ciblée.

```
Exemple: "Université" -> "Univers" et "Univers" -> "Univers" suggérant que Université et Univers ont le même sens.
```
#### Under Stemming:

Cette erreur intervient lorsque la partie du mot découpée est trop petite pour la racine ciblée.

```
Exemple: "Data" -> "Dat" et "Datum" -> "Datu" quand "Datum" devrait donner "Dat".
```

Plusieurs algorithmes sont disponible, chacun ayant ses avantages et désavantages, tel que:
- Porter's Stemmer
- Lovins Stemmer
- Dawson Stemmer
- Krovetz Stemmer
- Xerox Stemmer
- N-Gram Stemmer
- Snowball Stemmer
- Lancaster Stemmer

### Lemmatisation:
La Lemmatisation est un procédé consistant en l'analyse lexicale d'un texte avec pour but de regrouper les mots d'une même famille afin d'être analysé comme un seul objet, cette méthode est souvent couplée au Stemming.

```
Exemple: "est", "sois", "fut", "étais" et "fussions" seront convertis en le verbe "être".
```

Traditionnellement, les moteurs de recherche analysent votre page en essayant de retrouver chacune des variantes pour les regrouper autour de lemmes ; Le principe étant de définir le sujet principal. 

### Régularisation des expressions:
Ce procédé consiste à supprimer ou remplacer par un espace tous les caractéres ne comportant pas d'information comme les paranthéses, crochets, ou encore slash...

```
Exemple: "Ceci est_une phrase, (très intéressante)." -> "Ceci est une phrase très intéressante"
```
### Supression des Stop Words:
Les Stop Words sont des mots courants qui n'apportent qu'une légére aide lors de la classification d'un document par exemple.

La stratégie pour pouvoir déterminer une liste de Stop Words est de trier les termes par une collection de fréquences, puis prendre les termes les plus fréquents.

### Tokenisation:
La Tokenisation est un procédé de segmentation des phrases ou mots d'un corpus en petites unités, des *tokens*.

On peut voir les mots comme des tokens des phrases, ou encore les phrases comme des tokens d'un corpus.

```
Exemple: "Ceci est une phrase très intéressante" -> | Ceci | est | une | phrase | très | intéressante |
```
## Exemple de pré-traitement

Pour pouvoir traiter des phrases en Python nous auront besoin de plusieurs librairies:
- re ou Regular Expressions est une librairie native de Python permettant d'utiliser des caractères spéciaux sans contexte comme '(' qui serait mal interprété.
- unidecode est une librairie native de Python permettant de décoder un code *unicode* qui est attribué par Python à chaque caractére, cela est important lorsque l'on travaille avec plusieurs langues différentes comme l'anglais, le français, le russe ou encore l'hébreux.
- nltk ou Natural Language Toolkit est une librairie qui procure un ensemble d'outils tel que des Stemmers ou de la Lemmatisation.

Pour installer nltk il suffit d'entrer la commande:

```
pip install nltk
```

Le code suivant permet de convertir des phrases en un format plus compréhensible pour un modèle de machine learning donné.

``` python
import re
import unidecode
import nltk
from nltk.stem import SnowballStemmer

def text_processing(text):
    ''' Return cleaned text for Machine Learning '''
    REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
    NEW_LINE = re.compile('\n')
    BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')
    STOPWORDS = set(nltk.corpus.stopwords.words('french'))
    STEMMER = SnowballStemmer('french')

    text = text.lower()
    text = unidecode.unidecode(text)
    text = NEW_LINE.sub(' ',text)
    text = REPLACE_BY_SPACE_RE.sub(' ',text)
    text = BAD_SYMBOLS_RE.sub(' ',text)
    text = ' '.join([STEMMER.stem(word) for word in text.split() if word not in STOPWORDS])
    return text
    
text = "Je mangerais bien-une poire_aprés mon repas de ce midi.\n"
print(text)
print(text_processing(text))
tmp = input("Program paused...")
```

Et on obtient:

```
Je mangerais bien-une poire_aprés mon repas de ce midi.

mang bien poir apre rep mid
```

Magnifique ! N'est ce pas ?
