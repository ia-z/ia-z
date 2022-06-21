# Régularisation & tradeoff biais-variance : une introduction

On a pu voir dans dans le chapitre précédent que le but d'un modèle de ML est de bien généraliser.
Dans un court exemple de régression polynômiale, on a vu qu'il y était possible d'améliorer
les performances du modèle en augmentant le degré de notre polynôme, mais qu'il fallait être précautionneux
pour éviter le sur-apprentissage.

Ce comportement n'est pas spécifique à la régression polynômiale. Ce phénomène apparaît partout en ML,
à tel point qu'on lui a donné un nom : **le compromis biais-variance**.
Ce compromis (*tradeoff* en anglais) se modélise par une équation décrivant les trois sources d'erreurs possibles
par tout modèle de ML : le biais, la variance et le bruit.

La régularisation est un moyen de réduire l'erreur de généralisation d'un modèle en limitant explicitement
sa capacité à apprendre. C'est une des méthodes les plus utilisées en ML lorsque l'on fait face à du sur-apprentissage.

Dans ce chapitre, nous allons voir rapidement ce qu'est le compromis biais-variance et la régularisation, afin d'en avoir
une intuition. Les deux prochains chapitres aborderont ces deux concepts plus profondément.

## Compromis biais-variance
Comme nous l'avons vu, un modèle doit être entraîné de sorte à ne pas tomber dans le sous-apprentissage ni le sur-apprentissage.
*Mathématiquement, on peut décrire le sous-apprentissage comme un phénomène étant causé par un modèle trop biaisé.
De la même façon, il est possible de définir la source d'un sur-apprentissage d'un modèle par sa variance.*

Mais alors, qu'entends-t-on par *biais* et *variance* d'un modèle ?

Pour faire simple, les biais d'un modèle réunissent l'ensemble des contraintes qui définissent l'ensemble des modélisations que peuvent
exprimer notre modèle. Par exemple, un modèle linéaire ne peut modéliser que des fonctions affines entre ses entrées et sa sortie,
ce qui en fait un modèle très biaisé.

La variance, elle, peut se visualiser par la sensibilité d'un modèle face aux données d'entraînement. Un modèle avec une haute variance
sera très sensible à un changement dans ses données d'entraînement. Il va donc plus facilement sur-apprendre, car une grosse variance
est en général synonyme d'une grosse capacité d'adaptation aux données. Un *K-NN* est sensible aux données car ces dernières définissent
directement la façon dont il va faire ses prédictions. A l'inverse, un modèle linéaire prend en compte l'ensemble des données
pour trouver la courbe qui passe le mieux à travers celles-ci.


## Régularisation
La régularisation est une méthode pour limiter le sur-apprentissage d'un modèle.
Le principe est d'empêcher un modèle à apprendre des relations trop complexes entre les features `X` et l'objectif `y`.

En fait, il est possible de voir la régularisation comme une façon d'ajouter un biais à notre modèle, afin de réduire sa variance.
Ce biais indique au modèle que nous préférons trouver des solutions simples, en partant de l'hypothèse que
[ces solutions simples sont généralement les meilleures](https://fr.wikipedia.org/wiki/Rasoir_d%27Ockham).

La régularisation prend souvent la forme d'une pénalité ajoutée à la fonction de perte d'entraînement du modèle.
Cette pénalité modélise la complexité du modèle (que le modèle cherche donc à minimiser).
