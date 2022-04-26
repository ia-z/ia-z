# Nom du chapitre
Ce document est un template exemple pour l'écriture d'un chapitre `ia-z`.
**Le nom du chapitre ne doit pas comprendre le numéro du chapitre, simplement son nom.**
Les chapitres sont écrits en format *markdown* ou *jupyter notebook*.
Ces chapitres sont automatiquement compilés par *jupyter-book* afin de générer le site web.
Afin que la compilation se déroule bien, et que les chapitres soient cohérent entre eux, il faut suivre
quelques règles de style.

Il n'est pas nécessaire de faire un sommaire du chapitre, ils sont générés automatiquement par *jupyter-book*.

## Nom de la première section
Les sections en *markdown* commencent par des \#. Le nombre de \# définit le niveau de la section
(2 \# est une section principale, 3 \# est une sous-section d'une section principale...).
**Ne pas sauter de niveau de section**, c'est-à-dire ne pas passer d'une section à 1 \# à une section à 3 \# par exemple...
La section à 1 \# est réservée pour le titre du chapitre.

### Nom d'une sous-section
Exemple d'une sous-section.

* Exemple d'une liste à puce en *markdown*
* Blip bloup

## Mieux visualiser votre chapitre
Pour avoir un retour visuel sur le chapitre que vous êtes en train d'écrire, vous pouvez *fork* le git sur votre ordinateur
et compiler en local le site. Vous aurez alors un retour direct sur la façon dont votre chapitre s'insère dans le site et sur son apparence.
Pour en savoir plus sur la compilation du site web, vous pouvez regarder le [tutoriel jupyter-book](https://jupyterbook.org/start/build.html).
N'hésitez pas non plus à demander de l'aide sur le discord !

## Insertion d'images
Pour insérer des images, il est possible de suivre ce format :

:::{figure-md} nom-figure-md
<img src="chemin.png" alt="Texte alternatif">

Description de l'image, commentaire, source, etc...
:::

Il est possible de renvoyer vers une image du chapitre avec un [lien](#nom-figure-md).
Ces images n'apparaîtront pas sur le git car ce n'est pas une instruction *markdown* de base, mais elles apparaîtront bien sur le site
après la compilation par *jupyter-book*. Pour en apprendre plus sur l'insertion d'images, vous pouvez consulter [la page dédiée sur leur site](https://jupyterbook.org/content/figures.html).

## Formules mathématiques
Les formules mathématiques n'apparaîssent pas sur le git, [pour des raisons de sécurité](https://stackoverflow.com/questions/11256433/how-to-show-math-equations-in-general-githubs-markdownnot-githubs-blog).
Mais lors de la compilation du site, les formules apparaissent bel et bien ! Vous pouvez donc faire des formules de manière classique comme en LateX :

$$
\frac{\pi}{4} = 4 \text{Arctan}(\frac{1}{5}) - \text{Arctan}(\frac{1}{239})
$$

Encore une fois, vous pouvez compiler de votre côté pour visualiser votre chapitre au sein du site.

## Conclusion
* Les conclusions se font par une liste à puce
* Les idées principales du chapitre devraient être rappelées ici

## Sources
* Il faut absolument citer les sources dont vous vous êtes inspirés pour écrire le chapitre.
* De plus, vous pouvez y mettre des liens vers des ressources supplémentaires pour aller plus loin.
* [Mettez les sources dans une liste à puce](https://www.youtube.com/watch?v=dQw4w9WgXcQ).
* Evitez de mettre simplement les liens, essayez de trouver un petit titre à votre source.
