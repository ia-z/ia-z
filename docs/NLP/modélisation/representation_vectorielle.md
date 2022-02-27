# Bag of Words - Term Frequency-Inverse Document Frequency (TF-IDF)

Le score Term Frequency-Inverse Document Frequency (TF-IDF) permet de représenter un texte au sein d'un corpus sous forme vectorielle. Ces vecteurs sont par la suite utiliser par des modèles de machine learning pour effectuer des prédictions.

Le texte est représenté sous la forme d'un "bag of words" et chacun des mots se voit affecté un score en fonction de sa fréquence d'apparition au sein d'un vecteur.

Ce score comprend deux composantes :
* TF : Qui désigne la fréquence de ce mot dans le document
* IDF : Inversement proportionnelle à la fréquence d'apparition dans l'ensemble du corpus (un corpus correspond à un ensemble de document)

D'un point de vue mathématique, voici la formule associée :

$TF = \frac{\text{Nombre de fois ou le mot apparait dans le document}}{\text{Nombre de mots dans le document}}$


$IDF = log\left(\frac{\text{Nombre de documents}}{\text{Nombre de documents ou le mot apparait}}\right)$

$TFIDF = TF*IDF$

On peut ainsi interpréter ce score de la manière suivante : Plus le mot est fréquent dans le texte, plus il a un poid important, mais plus il est fréquent dans l'ensemble du corpus et plus son poids décroit.
Ainsi les termes récurents dans l'ensemble du corpus (du type déterminant, conjonctions de coordinations ..) auront un poids faible mais les mots caractéristiques d'un texte particulier, avec un réel sens métier, seront d'autant plus pondérés.

Cette métrique est utile pour les taches de classification des documents et permet d'obtenir simplement et rapidement une représentation du texte assez robuste.

Il existe une implémentation dans scikit-learn.

L'utilisation est assez simple, ci-dessous un extrait de code :

```python
from sklearn.feature_extraction.text import TfidfVectorizer
corpus = ["La communauté dfi",
          "On remercie les rédacteurs ia-z pour ce cours communautaire",
          "Anis représente la communauté dfi sur Twitch",
          "La communauté dfi souhaite avoir plus d'émots"]
vectorizer = TfidfVectorizer(min_df=1)
X = vectorizer.fit_transform(corpus)
idf = vectorizer.idf_
print(dict(zip(vectorizer.get_feature_names_out(), idf)))

{'anis': 1.916290731874155, 
'avoir': 1.916290731874155, 
'ce': 1.916290731874155, 
'communautaire': 1.916290731874155, 
'communauté': 1.2231435513142097, 
'cours': 1.916290731874155, 
'dfi': 1.2231435513142097, 
'ia': 1.916290731874155, 
'la': 1.2231435513142097, 
'les': 1.916290731874155, 
'on': 1.916290731874155, 
'plus': 1.916290731874155, 
'pour': 1.916290731874155, 
'remercie': 1.916290731874155, 
'représente': 1.916290731874155, 
'rédacteurs': 1.916290731874155, 
'souhaite': 1.916290731874155, 
'sur': 1.916290731874155, 
'twitch': 1.916290731874155, 
'émots': 1.916290731874155}
```

Un problème avec ce type d'approche de représentation vectorielle est la non-prise en compte du contexte au sein des phrases. Nous verrons par la suite d'autres approches tenant compte de cet aspect (notamment avec des modèles plus évolués de type Bert).

En résumé, le score tf-idf est facile à calculer et nous permet de disposer d'une métrique de base pour extraire les termes les plus descriptifs d'un document. Vous pouvez facilement calculer la similarité entre 2 documents en l'utilisant qui fera l'objet d'un article de blog par la suite.

Néanmoins, étant donné que tf-idf est basé sur le  modèle "bag of words" il ne capture donc pas la position dans le texte, la sémantique et les co-occurences dans différents documents. Pour cette raison, le tf-idf n'est utile qu'en tant que feature au niveau lexical. Il ne permet pas de capturer la sémantique (à la différence des words embeddings de type word2vec ou Bert)

Cela dépend donc beaucoup de l'usage que vous voulez faire de TF-IDF !

## Sources 

- https://en.wikipedia.org/wiki/Tf%E2%80%93idf