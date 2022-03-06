# Régularisation & tradeoff biais-variance
La régularisation ainsi que les biais inductifs sont deux moyens
de limiter les capacités d'un modèle afin d'éviter l'overfitting.

La variance décrit la puissance à laquelle un modèle peut facilement s'adapter,
à des données. C'est une puissance à double tranchant car s'il s'adapte trop facilement
alors il sera prone à l'overfitting.

## Comment fonctionne la régularisation
Le principe général est de contraindre les paramètres appris par un modèle.
Pour ce faire, on peut ajouter un terme supplémentaire dans la fonction de loss
que l'on souhaite minimiser.
Ce terme supplémentaire compte comme une pénalité, elle permet de réduire l'overfitting.

*Mais pourquoi ajouter une pénalité permet de réduire l'overfitting ?*

Cela peut paraître contre-intuitif, mais en fait réduire les capacités d'apprentissage d'un modèle
peut l'aider à mieux généraliser !
Si on reprends notre exemple du chapitre précédent, on peut imaginer qu'ajouter une pénalité
à notre modèle revient à l'obliger à travailler avec un kit réduit d'outils à sa disposition.
Il va être obliger de faire avec moins, et donc il ne pourra pas sur-optimiser son apprentissage sur
les exercices d'entraînement (les petites corrélations qui améliorent marginalement les performances
mais qui se trouvent inutiles voire désastreuses lors de l'évaluation sur de nouveaux exercices).

D'une certaine manière, ajouter une pénalité sur les paramètres du modèle revient à demander au modèle
de trouver une solution simple et efficace au problème donné. Cette solution est
[généralement la meilleure](https://fr.wikipedia.org/wiki/Rasoir_d%27Ockham) !

## Régularisations classiques
Il existe plusieurs régularisations possibles, mais les plus connues sont certainement la régularisation L1 et L2.
D'autres régularisations peuvent directement dépendre de la tâche considérée ou du type de modèle utilisé.

### L2
La régularisation L2 demande à ce que la norme quadratique des paramètres soit la plus petite possible.
Mathématiquement on peut écrire :

<img src="https://render.githubusercontent.com/render/math?math=L2(w) = \sqrt{\sum_i w_i^2}">
<img src="https://render.githubusercontent.com/render/math?math=Loss_{final}(w) = loss(w) \+ \lambda L2(w)">

*Comment afficher ça mieux ? :'( jupyter notebook ?*

Afin de moduler la force de pénalisation par rapport au loss, on définit un hyperparamètre \lambda qui est une constante
définit avant l'entraînement. Un lambda trop gros empêchera le modèle d'apprendre (il ne pourra plus s'exprimer
car la moindre modification de ses poids sera fortement pénalisée), mais un lambda trop faible masquera l'effet
de la régularisation.

*Image du cercle autour de w_1 et w_2 pour comprendre comment la régularisation réduit l'espace de recherche.*

### L1
*Image du diamant autour de w_1 et w_2 pour comprendre la différence avec la reg L2, et pour mieux comprendre
pourquoi la L1 pousse les poids à valoir 0.*

### Lasso


## Biais & variance
*C'est quoi le biais inductif d'un modèle ?*
*C'est quoi la variance d'un modèle ?*
### Exemple: régression linéaire vs KNN

## Biais vs régularisation
| Régularisation                                                     | Biais                                                                   |
|--------------------------------------------------------------------|-------------------------------------------------------------------------|
| Contraintes sur les paramètres du modèle.                          | Contraintes sur l'architecture du modèle.                               |
| Réduit l'espace de recherche des solutions pendant l'entraînement. | Réduit l'espace des solutions potentielles dès la définition du modèle. |
| Réduit l'overfiting.                                               | Réduit l'overfitting.                                                   |

## Tradeoff biais-variance
### L'intuition
### (\*\*) Les détails mathématiques

## Conclusion


## Sources

https://math.mit.edu/~gs/learningfromdata/
