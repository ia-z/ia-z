# Normalisation

Kézako ? Encore une normalisation ? Réfère-elle à la normalisation évoquée lors du cours de Machine Learning ? Pas de panique. Ici on parle de normalisation des mots.

Quelques définitions théoriques nous permettant de comprendre ce procédé : 

* **Normalisation** : processus de standardisation des mots de manière générale. Par exemple, on souhaite identifier de la même manière les termes "DFI" et "D.F.I".

* La **lemmatisation** processus consistant à ramener les mots à leur forme de base. Par exemple rapporter l'ensemble des formes du verbe être : suis, es, est, sont à sa forme non conjugée : être.

* Le **stemming** est une manière simplifiée de pratiquer la lemmatisation en procédant à des suppressions de lettres en fin de mot. Une série de règle explicite permet ainsi de ramener "automate", "automatique", "automates" au radical "automat".

# Le stemming

Le procédé le plus simple pour se rapporter au radical est le stemming, il existe plusieurs procésus de stemming et plusieurs déclinaisons d'algortihmes. Le plus connue étant le stemmer de Porter.

Néanmoins ce procédé n'est pas toujours utile et ses performances sont inégales. Il peut être utile de conserver la notion de conjugaison pour certains cas d'usages. La vectorisation des mots permet également sur des corpus suffisament importants de s'affranchire en partie de ces procédés (c.f partie embeddings / representation_vectorielle).

L'implémentation la plus couramment utilisée est celle fournie par la librairie NLTK de stanford. ci-dessous quelques applications classiques.

```
import nltk
ps = nltk.stem.PorterStemmer()
ps.stem('chats')
'chat'
ps.stem('chiens')
'chien'
ps.stem('apprentissage')
'apprentissage'
ps.stem('automatique')
'automatiqu'
```
