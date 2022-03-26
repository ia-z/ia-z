# Topic modeling

Le topic modeling est une branche de l'analyse de texte qui vise à définir la thématique d'un ensemble de documents. L'objectif est d'extraire des thèmes d'intérêt, qui sont récurrents dans les documents, sans aucun a priori. Il s'agit donc d'une procédure non supervisée.

## Latent Dirichlet Allocation (LDA)

### Description

La LDA est une procédure permettant de construire $k$ thèmes d'intérêt, $k$ étant choisi arbitrairement. Chaque thème est une combinaison pondérée de mots. Et chaque document est une combinaison pondérée de thèmes.

### En pratique

**Choix du paramètre $k$**

- Lorsque $k$ est petit: nous obtenons un faible nombre de topics avec des groupes hétérogènes.
- Lorsque $k$ est élevé: nous obtenons un grand nombre de topics avec des groupes plus fins.

**Code**

La LDA repose sur un corpus vu comme un Bag Of Word (BoW). 

La première étape consiste en la génération de la matrice des fréquences, dont les paramètres essentiels de celle-ci sont décrits ci-dessous:

```python
from sklearn.feature_extraction.text import CountVectorizer

params_tf = {
    'strip_accents': 'unicode',
    'stop_words': None,
    'lowercase': True,
    'max_df': .95,
    'min_df': 3, 
    'ngram_range': (1,2) 
}

tf = CountVectorizer(**params_tf)
corpus_tf = tf.fit_transform(corpus)
```
Vous devez définir corpus comme étant une liste de phrase (de type string) en mettant un ensemble de phrases de votre choix. Chaque phrase est considéré comme un document. 

corpus_tf est une matrice de taille (#documents, #mots dans le vocabulaire)

L'étape suivante est l'estimation du modèle, dont les paramètres essentiels sont décrits ci-dessous:

```python
from sklearn.decomposition import LatentDirichletAllocation

params_lda = {
    'max_iter': 200, 
    'evaluate_every': 4, 
    'perp_tol': .01, # Perplexity 
    'n_components': 20 
}

lda = LatentDirichletAllocation(**params_lda)

corpus_lda = lda.fit_transform(corpus_tf)

Ici, corpus_lda est une matrice de taille (nombre de documents, n_components)

Enfin, on effectue une assignation du topic avec le score le plus élevé avec corpus_topic étant une matrice de taille (nombre de documents, 1).

corpus_topics = corpus_lda.argmax(axis=1) 
```


## Visualisation des résultats - pyLDAvis

Cette librairie utile pour l'interprétation des topics.

```bash
pip install pyldavis
```

```python
import pyLDAvis
import pyLDAvis.sklearn
#pyLDAvis.enable_notebook() à préciser dans un notebook
vis = pyLDAvis.sklearn.prepare(lda, corpus_tf, tf, mds='tsne', R=10, sort_topics=False)
pyLDAvis.display(vis)
```

La visualisation repose sur un paramètre essentiel : la **relevance** d'un mot. Elle est définie comme suit:

$\begin{aligned}\text{relevance}(\text{word } w / \text{topic } t) = \lambda p(w/t) + (1-\lambda)\frac{p(w/t)}{p(w)}\end{aligned}$

- $`\lambda`$ proche de 1: les mots caractérisant un topic remontent dans le classement du topic. Ce sont des mots fréquents dans le topic ; mais ils peuvent également être fréquents dans d'autres topics.
- $`\lambda`$ proche de 0: les mots caractérisant ce topic, et uniquement celui-ci, remontent dans le classement. Ces mots ne sont donc contenus que dans ce topic, mais ils sont en nombre limité.

## Sources

- https://towardsdatascience.com/topic-modeling-and-latent-dirichlet-allocation-in-python-9bf156893c24
- https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.htmls
- https://towardsdatascience.com/topic-model-visualization-using-pyldavis-fecd7c18fbf6