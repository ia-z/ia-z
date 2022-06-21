# Pourquoi le Machine Learning ?
Lorsque la plupart des personnes entendent Machine Learning (*ML*), ou « apprentissage automatique »,
ils s'imaginent un robot ou le metaverse propulsé par Mark Z.
Mais le Machine Learning n'est pas un simple fantasme futuriste ; il est déjà là.
La première application de ML qui s'est vraiment imposée, en améliorant la vie de centaines de millions de personnes,
a vu le jour dans les années 1990 : le filtre anti-spam. 

Elle a été suivie par des centaines d'applications ML qui alimentent aujourd'hui
des centaines de produits et de fonctionnalités que vous utilisez régulièrement :
qu'il s'agisse de meilleures recommandations, de la compréhension de textes, de la vision par ordinateur ou de la recherche vocale.

Le Machine Learning prend une place de plus en plus grande dans nos vies quotidiennes.
Avant de commencer à comprendre son fonctionnement, il semble judicieux de se demander :

**Pourquoi le ML est si pratique ?**

Pour répondre à cette question, nous allons reprendre notre exemple de filtre anti-spam.

Imaginons que vous souhaitez participer au prochain Meetup organisé par la communauté dans votre ville.
Néanmoins, le filtre anti-spam de Google n’arrête pas de classer les messages des modérateurs au sein de votre rubrique Spam.
Vous souhaitez donc modifier le filtre anti-spam de Google.

Réfléchissez à la manière dont vous écririez le filtre anti-spam en utilisant des techniques dites de  « programmation traditionnelles » :

1) Tout d'abord, vous devez considérer ce à quoi ressemble typiquement le spam.
Vous remarquerez peut-être que certains mots ou expressions ont tendance à revenir souvent dans l'objet du message.
Vous remarquerez peut-être aussi des patterns tels que le nom de l'expéditeur, le corps de l'e-mail et d'autres parties de l'e-mail.

2) Vous écrivez ensuite un algorithme de détection pour chacun des patterns que vous remarquez et votre programme
détectera les courriels comme étant du spam si un certain nombre de ces patterns sont détectés.

3) Vous testez votre programme et répétez les étapes 1 et 2 jusqu'à ce qu'il soit suffisamment bon pour être lancé.

Comme le problème est difficile et chronophage, votre programme deviendra probablement une longue liste de règles complexes - assez difficile à maintenir.

En revanche, un filtre anti-spam basé sur des techniques de ML apprend automatiquement quels mots et phrases sont de bons indicateurs de spam
en détectant des patterns de mots inhabituellement fréquents dans les spams.
Le programme est beaucoup plus court, plus facile à maintenir et très probablement plus précis.

En outre, un filtre anti-spam utilisant des techniques de programmation traditionnelles devrait être mis à jour pour tout nouveau pattern.
Si les spammeurs sont assez malins pour contourner votre filtre anti-spam, vous devrez continuer à écrire de nouvelles règles pour toujours.

En revanche, un filtre anti-spam basé sur des techniques de Machine Learning remarque automatiquement qu'un nouveau pattern est devenu inhabituellement
fréquent dans les spams signalés par les utilisateurs, et il commence à les signaler sans votre intervention.


## Modélisation d'un problème
De manière générale, ce que l'on souhaite faire lorsque l'on veut résoudre un problème informatique, c'est
créer un algorithme qui résout cette tâche. En ML, on parle souvent de modèle, car son travail est de modéliser
les données de façon à résoudre un problème donné.

Par exemple, pour les systèmes de recommandations, le modèle peut se résummer comme étant l'algorithme qui s'occupe
de dire quels sont les items qui pourraient intéresser un consommateur, en prenant en compte l'historique du consommateur.

Construire un tel modèle est la partie la plus difficile, et
il est possible de s'y attaquer de plusieurs manières. Mais deux méthodes principales s'imposent:

* Etablir des hypothèses sur la nature de la relation entre l'historique du consommateur et les items potentiels,
définir un ensemble de règles qui vont choisir quels items mettre en avant.
* Récolter beaucoup de données sous forme de couple `(historique, items achetés)`
et trouver le modèle qui explique le mieux les relations entre les données.

Dans les faits, un mélange des deux méthodes est souvent utilisé.
Le point principal qui les distinguent c'est que dans un cas le modèle est défini à la main,
et dans l'autre le modèle est déduit directement des données.

Les systèmes dits *symboliques* sont des systèmes où le modèle est défini à la main.
Il a l'avantage de pouvoir profiter de l'expérience d'experts du domaine, et de rester simple et facilement interprétable.

Le ML se concentre sur la déduction du modèle directement à partir des données.
Il permet de réduire les hypothèses simplificatrices entre la relation de l'historique des consommateurs
et des items, et de considérer beaucoup plus de modèles différents à la fois avant de trouver un bon modèle.
De plus, dans des situations où il est difficile de définir soi-même un modèle à la main,
le ML permet de s'affranchir de cette étape.

## L'information grâce à la data
On vient de le voir, le ML utilise la data pour établir un modèle.
Ce modèle est une représentation d'une partie de l'information contenue dans la data.

**Il y a de l'information dans la data ?**

Et oui ! Alors ça dépend de la qualité de la data et de ce qu'elle représente, mais toute data contient de l'information.
C'est cette fameuse information qui est le nouvel "or noir" pour les GAFAM et autres grosses entreprises.

En fait, du moment qu'un ensemble de donnée n'est pas généré aléatoirement, c'est qu'il y a un mécanisme sous-jacent qui
dicte un minimum les règles qui produisent ces données.
Le but du ML est justement d'isoler ces règles et de les capturer dans un modèle.

Vous remarquez que dans l'ensemble des achats sur votre site, ceux qui achètent une switch ont tendance à aussi acheter des manettes supplémentaires ?
Vous pouvez manuellement décider de les mettre en avant. Ou alors, vous déduisez ce genre de relation directement à partir de vos ventes et vous
construisez un modèle qui va recommander des produits à vos clients automatiquement à partir du contenu de son panier.

C'est parce que les données sont faciles à générer et omni-présentes que les GAFAM payent cher pour les avoir, les garder et les exploiter.
L'information qu'elles récupèrent est particulièrement rentable.

**Il y a quand même des considérations éthiques lorsqu'il s'agit de manipuler des données privées.
Nous ne rentrerons pas dans ce sujet, mais vous devriez toujours vous poser ce genre de questions avant de vous lancer dans une exploitation de données.**

## Conclusion

* Le ML permet de fabriquer des modèles plus souples, qui ont potentiellement de meilleurs performances que ceux des systèmes symboliques.
* Un modèle de ML peut facilement s'adapter à un environnement dynamique.
* Une combinaison entre les méthodes symboliques et automatiques est souvent ce qui donne de meilleurs résultats.

## Sources

* [Comprendre le Machine Learning en 5min, Defend Intelligence](https://www.youtube.com/watch?v=RC7GTAKoFGA)
* [Machine Learning avec Scikit-Learn, A. Géron](https://www.dunod.com/sciences-techniques/machine-learning-avec-scikit-learn-mise-en-oeuvre-et-cas-concrets-0)
* [Software 2.0, Karpathy](https://karpathy.medium.com/software-2-0-a64152b37c35)