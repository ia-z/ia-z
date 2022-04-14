# Régularisation & tradeoff biais-variance
La régularisation ainsi que les biais inductifs sont deux moyens
de limiter les capacités d'un modèle afin d'éviter l'overfitting.

La variance décrit la puissance à laquelle un modèle peut facilement s'adapter
à des données. C'est une puissance à double tranchant car s'il s'adapte trop facilement
alors il sera prone à de l'overfitting.

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

### Régularisation L2
La régularisation L2 demande à ce que la norme quadratique des paramètres soit la plus petite possible.
Cette norme étant une fonction quadratique, elle est continue et dérivable en tout point ce qui est souvent apprécié.

Mathématiquement on peut écrire :

$$\begin{align}
\text{L2}(w) & = \sum_i w_i^2\\
\text{loss}_{\text{final}}(w) & = \text{loss}(w) + \lambda \text{L2}(w)
\end{align}$$

Afin de moduler la force de pénalisation par rapport à la loss, on définit un hyperparamètre $\lambda$ qui est une constante positive
définie avant l'entraînement. Un $\lambda$ trop gros empêchera le modèle d'apprendre (il ne pourra plus s'exprimer
car la moindre modification de ses poids sera fortement pénalisée), mais un $\lambda$ trop faible masquera l'effet
de la régularisation.

On parle de *Ridge Regression* lorsque l'on fait une régression linéaire couplée à une régularisation L2.

### Régularisation L1
La régularisation L1 contraint la norme L1 des paramètres à être la plus petite possible.
Elle n'est pas dérivable en 0, mais ce n'est en pratique pas gênant.

$$\begin{align}
\text{L1}(w) & = \sum_i |w_i| \\
\text{loss}_{\text{final}}(w) & = \text{loss}(w) + \lambda \text{L1}(w)
\end{align}$$

Cette régularisation a tendance à pousser des coefficients $w$ à valoir 0 exactement, ce qui est utile
pour faire de la sélection de features. En effet, si une feature a un coefficient associé qui
vaut exactement 0, alors on peut se débarasser de cette feature car elle n'influe clairement pas le calcul des prédictions !

On parle de *Lasso Regression* lorsque l'on fait une régression linéaire couplée à une régularisation L1.

### Visualisation L1 vs L2
Pour mieux visualiser leur effet sur l'entraînement de nos modèles, nous pouvons considérer un cas simple où nous
avons deux paramètres $w_1$ et $w_2$ à entraîner. On peut reformuler les problèmes de minimisation comme des problèmes
de minimisation sous contraintes :

$$\begin{align}
\arg \min_{w_1, w_2} = \text{loss}(w_1, w_2) + \lambda (|w_1| + |w_2|)
& \iff \arg \min_{|w_1| + |w_2| \leq \beta} = \text{loss}(w_1, w_2) \\
\arg \min_{w_1, w_2} = \text{loss}(w_1, w_2) + \lambda (w_1^2 + w_2^2)
& \iff \arg \min_{w_1^2 + w_2^2 \leq \beta} = \text{loss}(w_1, w_2)
\end{align}$$

Ces deux façons de voir le problème sont équivalentes. $\beta$ est inversement proportionnel à $\lambda$.
On peut ainsi tracer les courbes de niveaux du loss en fonction des valeurs de $w_1$ et $w_2$ et visualiser
les zones où les contraintes sont satisfaites (l'espace des solutions réalisables).

:::{figure-md} L1vsL2-fig
<img src="L1vsL2.png" alt="L1vsL2">

Visualisation de la régularisation L1 (à gauche) et L2 (à droite).
:::

Comme on peut le voir, la régularisation L1 impose des solutions dans un espace en forme de diamant, alors
que la L2 génère un espace de solutions en forme de cercle.
La solution optimale sans régularisation est représentée par le point $w^*$.
Le loss ici est une simple *MSE*, dont les courbes de niveaux tracent des ellipses de plus en plus grandes autour du minimum $w^*$.
La solution obtenue avec régularisation est représentée par le point $\hat w$.

*Visuellement, la solution optimal $\hat w$ est à la jonction
entre les courbes de niveau du loss et la frontière de l'espace des solutions.*

Ainsi, il est plus facile de comprendre pourquoi la régularisation L1 pousse plus facilement les coefficients $\hat w$ vers 0.
En prenant un point $w^*$ au hasard sur le plan 2D, il est plus probable que la projection des courbes de niveaux sur le
diamant arrive sur un des angles !

Rien n'empêche d'utiliser à la fois la régularisation L1 et L2. Lorsque les deux méthodes sont utilisées pour une
régression linéaire, on dit que l'on utilise une méthode *Elastic Net*. En pratique, *Elastic Net* qui a tendance à donner
de meilleurs résultats que la L1 et la L2 pris séparéments.

## Biais & variance
Lorsque l'on parle du *tradeoff biais-variance*, on parle du biais inductif et de la variance d'un modèle de Machine Learning.
Concrètement :
* Les **biais inductif** d'un modèle représente l'espace des fonctions apprenables par un modèle.
* La **variance** d'un modèle est une mesure de la sensibilité que possède un modèle par rapport aux données utilisées pour l'entraîner.

### Biais inductif
Il est en fait [impossible d'entraîner un modèle sans biais inductif](https://fr.abcdef.wiki/wiki/Ugly_duckling_theorem).
Sans cela, il existerait une infinité de fonctions qui sont capables de modéliser les relations entres les couples $(x, y)$.
L'ensemble des biais inductifs constituent des hypothèses sur les fonctions qui pourraient le mieux modéliser la relation entre
nos couples $(x, y)$. L'étape d'apprentissage se résume alors à la recherche de la meilleure fonction parmis l'espace des fonctions
modélisables.

Le biais le plus courant est celui de **la continuité** : on suppose que si deux points $x$ et $x'$ sont proches dans l'espace, alors
il est probable que $f(x)$ et $f(x')$ soient proches l'un de l'autre. Intuitivement, cela revient à dire que si deux images ne diffèrent
que de quelques pixels, alors si l'une des deux images représente un chien, la seconde sera très probablement une image de chien.

La régularisation est en fait une façon de biaiser notre modèle vers des solutions plus simples. C'est aussi une hypothèse que l'on
choisit lorsque l'on entraîne le modèle !

### Variance
La variance d'un modèle résume son besoin de données pour apprendre au mieux. Plus un modèle a de variance et plus il aura besoin
de grosses quantités de données afin de ne pas sur-apprendre.

Pour être plus précis, on considère que les données utilisées à l'apprentissage proviennent toutes d'une source aléatoire capable
de générer toutes les données possibles d'une distribution fixée. On peut alors échantillonner plusieurs jeux de données à partir de cette source.
Cela permet alors d'entraîner autant de modèles qu'il y a de jeux de données, et chaque modèle va converger vers une solution finale
qui peut être évaluer sur un ensemble de test commun.
Dans ce cas, la variance d'un modèle de ML est mesurée à la variance des performances des différents modèles évalués sur le jeu de test,
mais entraînés sur des données différentes.

Si les prédictions d'un modèle sont trop dépendantes des données utilisées pour l'entraîner, alors c'est qu'il est en sur-apprentissage,
car cela signifie qu'il s'est trop spécialisé sur les données fournies à l'apprentissage.

### Exemple: régression linéaire vs KNN
Le modèle utilisé lors de la régression linéaire ne peut apprendre que des fonctions de la forme $f(x) = ax + b$ (ici nous n'avons qu'une feature $x$).
Pour ce modèle, le biais inductif est l'hypothèse que les données peuvent se modéliser sous la forme d'une droite.
L'espace de recherche est donc extrêmement contraint ! Mais l'avantage d'un tel modèle c'est qu'il suffit de peu de points
pour rapidement converger vers une fonction $f$ de bonne qualité. En effet, il suffit de deux points pour tracer une droite !
*Dans la vie réelle, les points sont bruités donc il faut plus de points pour mieux estimer la droite, mais l'idée reste la même.*

On peut comparer cet exemple à celui du KNN. Le KNN ne fait que l'hypothèse de continuité, il prédit la valeur d'un point $x$ par rapport
aux autres points vus pendant l'entraînement qui sont au voisinage de $x$. C'est l'hypothèse la plus simple qui soit, et cela laisse place à
un ensemble de fonctions modélisables énorme. Cela permet de garder un fort potentiel de modélisation, mais ça demande aussi un nombre de données
très élevé pour modéliser précisément une fonction en tout point.
*En fait, à cause de la malédiction de la dimension, le nombre de données nécessaires pour couvrir l'ensemble de définition d'un KNN
croit exponentiellement avec le nombre de dimensions de nos features.*

A travers ces deux exemples, on peut voir qu'il peut y avoir des comportements drastiquement différents lors de l'entraînement de nos modèles.
Avec peu de points et une hypothèse forte sur la relation entre nos données, on peut utiliser un modèle simple qui va converger sans problème.
Cependant, si nous faisons une hypothèse trop forte ou mauvaise, on peut se retrouver avec un modèle trop contraint qui ne pourra pas trouver de bonne façon
de modéliser le problème. Il faudra alors trouver (ou tester) de meilleures hypothèses, ou adoucir celles déjà faites. Le cas le plus simple
est alors d'entraîner un modèle plus expressif comme le KNN, mais il faut alors assez de données pour que ce dernier soit capable d'apprendre
une relation utile sans sur-apprendre.

## Tradeoff biais-variance
Le compromis biais-variance est fondamental en Machine Learning.
Intuitivement, on a un équilibre à trouver dans la taille de l'espace des fonctions que peuvent modéliser nos modèles.
Si on laisse cet espace être trop grand, alors le modèle va trouver une fonction qui sera très performante sur les données d'entraînement
mais qui aura un loss élevé sur de nouvelles données à cause d'un sur-apprentissage sévère. A l'inverse, à trop réduire cet espace,
on ne va laisser au modèle que des fonctions sous-efficaces pour modéliser la relation entre nos couples $(x, y)$.
Idéalement, on voudrait appliquer uniquement des biais qui correspondent à la nature de la vraie relation entre nos données. Cependant
il faut garder en tête que ces biais sont souvent inconnus, nous ne pouvons donc que tester différentes hypothèses afin de regarder
ce qui fonctionne le mieux en pratique sur les données à considérer.
*Une relation linéaire est peut-être sous-efficace par rapport à la vraie relation de votre couple $(x, y)$, mais elle est peut-être
ce que vous aurez de mieux entre le compromis "biais simplificateur" vs "nombre de données".*

:::{figure-md} biais-variance-fig
<img src="biais_variance.jpg" alt="tradeoff biais-variance">

Visualisation du compromis biais-variance. L'erreur totale (en jaune) est mesurée sur le jeu de validation.
Image en open access obtenue [ici](https://www.ncbi.nlm.nih.gov/books/NBK543534/figure/ch8.Fig3/).
:::

Le biais et la variance sont deux erreurs opposées, ajouter du biais réduit la variance, et vice versa.
Le meilleur modèle est celui qui a eu juste assez de biais pour bien généraliser sur le jeu de test sans pour autant sur-apprendre.

### (\*\*) Détails mathématiques
Soit :
* $x, y$ : Des couples de données où $x$ est un ensemble de features et $y$ la valeur à déterminer à partir du vecteur $x$.
Ces couples proviennent d'une distribution de probabilité $P$ quelconque.
* $D$ : Un jeu de données quelconque constitué de couples $(x_i, y_i)$.
$D$ est la réalisation d'un échantillonage de $P$. On définit $y_i = y(x_i)$.
* $h$ : Un modèle de ML capable d'apprendre à partir d'un jeu de données $D$.
Si $h$ a été entraîné sur $D$, on le note $h_D$, et on note ses prédictions $h_D(x)$.

On peut alors décomposer le loss moyen d'un modèle $h$ :

$$\begin{align}
\text{loss}_{\text{test}}(h) & = \text{variance}(h) + \text{biais}(h)^2 + \text{bruit}\\
E_{x, y, D}[(h_D(x) - y)^2] & = E_{x, D}[(h_D(x) - \bar h(x))^2] + E_x[(\bar h(x) - \bar y(x))^2] + E_{x, y}[(\bar y(x) - y(x))^2]
\end{align}$$

Où :

$$\begin{align}
\bar h(x) & = E_D[h_D(x)] \\
\bar y(x) & = E_{y, x}[y(x)]
\end{align}$$

Explications des valeurs ci-dessus :
* $\bar h(x)$ représente la prédiction moyenne du modèle $h$ lorsqu'on l'entraîne sur tous les datasets $D$ probables provenant de la distribution $P$.
* $\bar y(x)$ représente la valeur moyenne de $y$ associée à $x$. En effet, la valeur de $y$ peut être bruitée ou même ne pas complètement dépendre de $x$,
donc il faut prendre en compte que même si l'on mesure deux fois le même $x$, il est possible que l'on se retrouve avec des valeurs de $y$ différentes.
* $\text{loss}_{\text{test}}(h)$ est la performance moyenne du modèle $h$ entraîné sur l'ensemble de $D$ probables et évalué sur l'ensemble des couples $(x, y)$ probables,
provenant de la distribution $P$.
* La variance est une mesure de l'écart moyen entre la prédiction d'un modèle entraîné avec un dataset $D$ lambda et
la prédiction espérée $\bar h(x)$ de l'ensemble des datasets.
* Le biais est une mesure de l'écart moyen entre la prédiction espérée $\bar h(x)$ et la valeur espérée $\bar y(x)$.
* Le bruit mesure la variance moyenne entre points $y(x)$ et leur moyenne $\bar y(x)$

Ce que définit cette équation, c'est simplement qu'il est possible de réduire les pertes d'un modèle en réduisant sa variance et son biais.
Ce c'est pas une preuve qu'il y a forcément un compromis à faire entre la variance et les biais. Ce compromis est intrinsèque à la définition
de ces termes : l'un réduit l'espace de recherche et l'autre l'augmente.

Cependant, il faut savoir que les modèles $h$ ne sont pas tous égaux dans cette équation. Une fois que l'on choisit d'utiliser un modèle linéaire,
le biais sera forcément très fort. Si le biais n'est pas bon (c.a.d. si $\bar h(x)$ est loin de $\bar y(x)$), notre modèle aura de la peine à
faire diminuer le loss. Au contraire, un réseau de neurones peut plus facilement contrôler la force de son biais à travers plusieurs mécanismes de régularisation.
Cela nous permet mieux choisir la force des biais et de la variance de notre modèle.

*Si ici on utilise $h$ pour désigner un modèle, c'est parce que l'on considère qu'un modèle est pleinement défini par ses hypothèses.*

## No Free Lunch (NFL)
Le théorème du NFL statue qu'aucun algorithme de recherche de solution n'est meilleur que les autres sur tous les problèmes possibles.
La recherche d'un unique algorithme qui serait meilleur que tout les autres est donc inutile. Il est nécessaire de faire des hypothèses sur les biais qui seraient
intéressants, afin de choisir le ou les modèles de Machine Learning à entraîner.

## Conclusion
* La régularisation force un modèle à apprendre des solutions simples et efficaces, évitant ainsi le sur-apprentissage.
* Les biais inductifs représentent toutes les hypothèses que l'on fait pour réduire l'espace de recherche des solutions.
* Il est nécessaire de choisir les bons biais qui permettront à un modèle de bien généraliser. Ils évitent le sur-apprentissage.
* Ces biais doivent être utilisés avec parcimonie afin d'éviter le sous-apprentissage.
* Avoir beaucoup de données permet l'utilisation de modèles plus expressifs (avec peu de biais), tout en évitant le sur-apprentissage.
Les données supplémentaires peuvent être vues comme un moyen de régulariser l'entraînement.

## Sources
* [Linear Algebra and Learning from Data, Gilbert Strang, 2019](https://math.mit.edu/~gs/learningfromdata/)
* [L1 vs L2, Terence Parr](https://explained.ai/regularization/L1vsL2.html)
* [Tradeoff biais-variance, Kilian Weinberger, Cornell University](https://www.cs.cornell.edu/courses/cs4780/2018fa/lectures/lecturenote12.html)
* [Biais inductif, page wiki](https://fr.abcdef.wiki/wiki/Inductive_bias)
* [No Free Lunch, page wiki](https://fr.abcdef.wiki/wiki/No_free_lunch_in_search_and_optimization)
* [Rasoir d'Ockham, page wiki, Terence Parr](https://fr.wikipedia.org/wiki/Rasoir_d%27Ockham)
* [Théorème du vilain petit canard, page wiki](https://fr.abcdef.wiki/wiki/Ugly_duckling_theorem)
* no-free-lunch.org
