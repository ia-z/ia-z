
# Mener une recherche internet efficacement

Au cours de votre apprentissage et de votre carrière de data scientist, vous aurez souvent besoin d’effectuer des recherches internet pour élargir votre culture générale, acquérir de nouvelles connaissances ou compétences, résoudre des erreurs dans vos programmes ou encore chercher de l’aide pour la réalisation de vos projets. Internet est en effet l'outil parfait pour cela, c'est une vraie mine d'or qui regorge d'informations.
Mais c'est là son principal défaut : pour n'importe quelle recherche, il y aura toujours trop de résultats. Essayez, par exemple, de chercher 'chocolat' sur Google, 1 580 000 000 résultats vous seront proposés. Vous ne pourrez jamais consulter toutes ces pages web dans un temps raisonnable. Il est donc primordial de savoir cibler ses recherches et filtrer les résultats. Il peut être aussi pratique de sauvegarder certain d'entre eux pour les consulter plus tard ou les intégrer dans une synthèse par exemple. 
Nous aborderons en premier lieu dans la suite de cette rubrique les points clés importants pour mener une bonne recherche. Ensuite, nous verrons les outils pratiques pour restreindre le champ d'une recherche. Nous vous présenterons ensuite des solutions pour sauvegarder et organiser des résultats.
--
 
 
## 1 - Méthodes de recherche
Voici une liste (non-exhaustive) rassemblant les conseils qu'il faut respecter pour obtenir des informations pertinentes, complètes et fiables. 

* Evitez de polluer vos recherches : Cherchez par mots-clé, éliminez les mots superflus
  * _Ne cherchez pas “pourquoi mon message ne s’affiche-t-il pas dans la console” mais “problème affichage console”, les résultats seront plus nombreux et plus pertinents car aucun mot ne vient perturber la recherche._

* Si les résultats sont peu satisfaisants, ne pas hésiter à reformuler, réutiliser les expressions que vous pouvez lire sur les sites que vous avez déjà trouvé. Cela permet d'élargir le champ de la recherche sans vous éloigner de l’information que vous cherchez.

* Utilisez la langue de Shakespear : n’hésitez pas à passer par l’anglais, les résultats seront très nombreux (Pour ceux qui auraient du mal avec la langue, les services de traduction automatique sont très performants de nos jours, pensez-y !).

* Vérifiez la qualité de l'information :
 * Pensez toujours à chercher plusieurs sources différentes pour recouper et affiner les informations.
 * Pensez également à vérifier la date des articles que vous lisez. Une information n’est utile que si elle est encore à jour. Pour les conventions de codage ou documentations, vérifiez que la version dont il est question est la même que celle que vous devez utiliser.

* Utilisez les outils de votre navigateur : 
 * Sur une longue page, vous pouvez chercher les occurences d'une expression en utilisant le raccourci 'Ctrl+F'.
 * Les opérateurs de recherche (nous aborderons cela dans la partie suivante)

* Pour des recherches orientées sciences, vous pouvez utiliser des moteurs de recherche spécialisé comme :
  * _[Google Scholar](https://scholar.google.fr/) qui permet de rechercher des expression parmi un grand nombre de livres et articles scientifiques ( Cet outil propose d'utiliser les opérateurs de recherche de Google pour affiner vos recherches)._<br>
  * _[arXiv](https://arxiv.org/) qui permet de chercher des articles scientifiques parmi des archives de différents domaines des sciences._
  * _[Elsevier](https://www.elsevier.com/fr-fr) qui permet de chercher des ressources parmi une large base de livres et pages web entre autres. Ce site est axé plutôt sur la biologie._

* Pensez à enregistrer les résultats les plus pertinents que vous avez pu trouver. Enregistrez les et organisez les de manière à facilement retrouver les informations importantes. Pour cela, vous pouvez vous aider d’outils spécialisés :
  * _Les favoris dans votre navigateur de recherche : vous pouvez créer des dossiers et organiser vos favoris. C’est la manière la plus rapide de sauvegarder les résultats de vos recherches._
  * _[Zotero](https://www.zotero.org/) vous propose de télécharger les articles scientifiques sur votre pc et de les classer facilement._
  * _[Mendeley …](https://www.mendeley.com/download-reference-manager/windows) est un service semblable à Zotero._
  * _[Research Rabbit](https://www.researchrabbit.ai/) propose en plus de visualiser le lien entre les articles enregistrés et d'autres fonctionnalités avancées._

## 2 - Outils pratiques
Nous allons développer dans cette partie les 3 derniers points de la liste précédente. Nous allons découvrir quelques outils très pratiques pour vous assister dans vos recherches.

### Bien utiliser son navigateur:
Utilisez les outils offerts par votre navigateur pour filtrer les résultats et ne garder que les plus pertinents.
Nous allons découvrir maintenant les mots-clés réservés ou opérateurs de recherche. Les moteurs de recherche modernes (Google, Duckduckgo, ...) proposent de cibler votre recherche grâce à des mots clés ou des opérateurs spécifiques. Vous pouvez ainsi sélectionner les résultats suivant leur date de publication, le type de fichier qu'il contient (html, pdf, ...), filtrer par nom de domaine. Nous allons vous présenter dans la suite les mots-clé les plus utiles.

#### Les opérateurs:
 - "" : Pour rechercher une expression exacte, par exemple une citation, mettez cette requête entre guillemets.
 - AND / OR : Opérateurs bouléens qui permettent de renvoyer les résultats qui contiennent les expressions X ET Y (AND) ou X OU Y (OR). Vous pouvez combiner les expressions
 - () : Vous permet de rassembler des termes ensemble pour former des expressions (comme en maths). Cela vous permet de combiner les opérateurs logiques vus ci-dessus
    - _'(X AND Y) OR Z' sélectionnera à la fois les résultats contenant X ET Y, et les résultats contenant Z._
 - .. : Permet de chercher sur une plage de nombres.
    - _'voiture 2000..2010' vous retournera des résultats à propos des voitures des années 2000 à 2010._
 - * : Remplacer des mots manquants. Si vous cherchez une phrase particulière mais qu'il vous manque certains mots, vous pouvez combler les trous avec "*"
    - _'En * te décourvre pas d'un fil' vous retournera directement le fameux dicton 'En avril ne te découvre pas d'un fil'._
 - - : Vous pouvez exclure certains termes avec '-'(moins).
    - _'Lyon -ville' vous renverra des résultats sur les clubs de sport lyonnais par exemple, mais rien qui ne contienne le terme ville._
  
#### Les mots-clé :
Pour utiliser les mots-clé, il suffit de les placer à la fin de votre requête et suivis de ":" : `ce que je recherche <mot-clé>:<valeur mot-clé> <autre mot-clé>:<valeuyr autre mot-clé>
 - 'filetype:<extension>' : Spécifiez un type de fichier. Le navigateur ne vous retournera que des résultats contenant ce type de fichier.
 - 'site:<nom de domaine>' : Ne sélectionnez que les résultats provenant d'un nom de domaine spécifique.
 - 'before/after:<date>' : Sélectionnez les résultats publiés avant/après une certaine date.
   - _'before:21/12/2012' ne vous renverra que des résultats antérieurs à la fin du monde._
 - 'related:<url>' : Cherchez les résultats en lien avec une url.
   - _'related:google.fr' vous permettra de chercher les principaux moteurs de recherche._
 - 'inURL:<mot-clé>' : Permet de chercher les résultats contenant <mot-clé> dans leur url.
 - 'intitle:<mot-clé>' : Même principe avec le titre du résultat.
 - 'intext:<mot-clé>' : Idem mais dans le corps de la page.

 Pour plus de précidions, voici les pages qui ont servi de base à cette rubrique. Elles sont très complètes et très accessibles :
  - [27 Opérateurs Google pour affiner ses recherches](https://www.blogdumoderateur.com/operateurs-recherche-google/), Thomas Coëffé, Blog du Modérateur;
  - [Les opérateurs de recherche Google](https://www.journaldunet.com/solutions/seo-referencement/1194524-les-operateurs-de-recherche-google-la-recherche-avancee-pour-une-meilleure-analyse-seo/), Tommy Guyennot, Journal du Net;
  - [L'opérateur Google "site" : cas concrets de recherches avancées](https://www.imagile.fr/les-operateurs-google-cas-concrets-de-recherches-avancees-partie-1/), Julien Naufaulo, Imagile.fr;
  - [Faire une recherche sur Internet](https://openclassrooms.com/fr/courses/1757041-faire-une-recherche-sur-internet), Openclassroom;
  - [5 astuces pour mieux chercher sur google](https://www.youtube.com/watch?v=Xul8BQN8Z9A),  Shubham SHARMA, Youtube;
 
### Outils de recherche
 * Google scholar : Lancé par Google en 2004, c'est un moteur de recherche spécialisé qui regroupe un immense base de données de livres et d'articles scientifiques dont la plupart sont gratuitement accessibles. Lçe service permet de rechercher dans expressions dans ces ouvrages mais permet liste aussi par exemple le citations d'un article. Il permet aussi d'enregistrer des articles ou de recevoir une notification par mail lorsqu'une publication paraît.
 NB : A noter que les ouvrages répertoriés par Google scholar ne sont pas seulement scientifiques, le moteur recense aussi des archives historiques par exemple. 
 <br>
 Pour en savoir plus sur Google Scholar, voici quelques ressources intéressantes : <br>
    - [Présentation de Google Scholar (GS)](http://www.ist.agropolis.fr/les-formations/pour-les-etudiants-enseignants-et-chercheurs/item/focus-sur-google-scholar-trucs-et-astuces)

 * ArXiv : Un moteur de recherche regroupant également de nombreux articles scientifiques. On y retrouve notamment beaucoup de publications en intelligence artificielle. Il faut toutefois noter que ces publications ne sont pas soumises à une révision par les pairs, mais que lorsqu'un article est publié dans un journal scientifique qui l'impose, cela est généralement précisé sur la page de l'article.

 * StackOverflow : Un forum sur le thème de l'informatique qui est majoritairement connu pour regrouper une immense base de données de questions/réponses en informatique. Pour faire simple, l'intégralité des erreurs ou problèmes que vous pourriez rencontrer en programmation ont déjà été posté sur ce site, et bien souvent il y a une solution fonctionnelle parmi les réponses. Attention toutefois aux dates des posts. De vieux posts peuvent proposer des solutions qui ne sont plus valables aujourd'hui. Ce site est généralement référencé parmi les premiers résultats, parfois même avant les documentations officielles. Pour l'utiliser, il suffit de copier/coller votre erreur ou l'énoncé de votre problème dans la barre de recherche. Le site tombera parmi les premiers résultats.

# Outils de gestion des ressources
Lors de vos recherches il peut être utile d'enregistrer et d'organiser des ressources pour les retrouver facilement ou les consulter plus tard par exemple. C'est ce que proposent les outils suivants.
 * Zotero : Logiciel installé en local sur votre machine. Il permet d'enregistrer des articles, des vidéos, des pages webs et des les organiser dans une bibliothèque pour vous aider à gérer vos ressources. Le logiciel est capable de détecter le titre et les auteurs des articles enregistrés (il peut y avoir quelques problèmes avec des articles anciens). Il existe également une extension web pour enregistrer vos ressources depuis votre navigateur sans avoir à ouvrir l'application. Nous reviendrons sur cet outil plus en détail dans la suite de ce cours.
 * Researchrabbit : Un site web qui propose les mêmes fonctionnalités que zotero directement dans un navugateur web. Votre compte vous permet de vous connecter à votre bibliothèque depuis une autre machine que votre pc. L'application propose également des fonctions supplémentaires très utiles comme la recherche les citations des articles et la création de graphes de relations entre ces derniers. N'hésitez pas à aller jeter un oeil par vous même. Cette application étant plus complexe à prendre en main que Zotero, qui est tout de même relativement complet et polyvalent, nous ne nous y attarderons pas.
 * Mendeley : Un logiciel équivalent à Zotero, qui propose cependant des outils facilitant l'annotation d'articles dans l'application, un peu à la manière d'Acrobat Reader(lecteur de pdf). Etant moins polyvalent que Zotero, nous ne nous y attarderons pas non-plus, mais n'hésitez pas à aller le tester.


## 3 - Cas de recherches classiques 

Voici quelques conseils pour réaliser deux types de recherches que vous aurez souvent l’occasion de mener au long de votre apprentissage des sciences de la donnée et de votre parcours de programmeur

#### 1. L’état de l’art 
 Vous voulez une information globale et générale à propos d’un sujet. Vous ne désirez pas rentrer dans le détail tout en acquérant une base de connaissances et de vocabulaire nécessaires à la compréhension globale du sujet. Voici quelques conseils pour orienter vos recherches :

 * Cherchez le nom du sujet sur internet.
 * Wikipédia apporte une vision d’ensemble du sujet et une base de vocabulaire. C’est bien de commencer par là. N’hésitez pas à aller lire les pages connexes ou relatives aux mots de vocabulaire de la page.
 * Si les ressources sont peu nombreuses, n'hésitez pas à aller chercher des sources en anglais (Si vous n’êtes pas bilingues, les traductions automatiques sont plutôt efficaces). Pour être sûr d’avoir la bonne traduction pour des termes techniques, vous pouvez chercher l’article français sur wikipédia puis sélectionner la version anglaise.

 Il peut être utile de garder les résultats de vos recherches dans un coin. Pour cela il existe des outils comme **Zotero** qui permet d’enregistrer des articles depuis le web sur votre pc et de classer vos articles.

#### 2. Pour des recherches liées à une notion d’un langage de programmation
 * Pour comprendre comment utiliser une fonction/librairie :
 * Pour chercher la documentation relative à une librairie, tapez :  < nom du module > documentation (éventuellement < nom du langage >)
 * Pour chercher la documentation relative à une fonction, tapez : < nom de la fonction > (< nom du module > si la fonction provient d’une librairie externe) < nom du langage >
 * Certains sites regroupent des documentations non officielles avec des exemples, voire dans certains cas proposent la possibilité de tester une fonction sur le site ou des exercices d’entraînement. A titre d’exemple, on peut citer W3School ou geekforgeeks.org.
 * Cherchez des exemples d’utilisation de la fonction, pour cela, tapez : < nom de la fonction > exemples (ou “examples” pour une recherche en anglais). N’hésitez pas à consulter les sites suivants qui regorgent d’exemples et d’explications : Stackoverflow, Github, pythonexamples.org
 * Pour résoudre les erreurs (si la lecture de l’erreur ne vous permet pas de résoudre le problème) :
 * copier coller l’erreur dans la barre de recherche
 * Cherchez des solutions soit dans la documentation du langage ou de la librairie, soit sur les forums comme Stackoverflow.

 Le plus important ici est de vérifier que la version dont il est question est la même que celle que vous utilisez. Vérifiez également les dates des posts sur les forums, si la solution proposée ne fonctionne pas, cela peut venir du fait qu’il s’agit d’une ancienne version.

 <br><br>
## En résumé

### Points-clés d’une recherche réussie :

* Chercher par mots-clé, c’est la clé du succès !
* Varier les expressions, reformuler c'est c’est la clé pour avancer !
* Croisez vos sources pour une information fiable !
* Une bonne information est une information à jour !
* Sauvegardez les ressources dignes d’intérêt !

### Liste des outils pratiques :

* Problèmes de programmation :
  * StackOverflow;
  * GitHub (exemples, librairies, ...)
  * Les documentations officielles
  * Openclassroom : le forum et les cours
  * W3School : Cours, extraits de documentation avec des exemples et la possibilité de tester sur le site
  
* Recherche d'informations générales :
  * Wikipédia

* Recherche d'informations spécifiques :
  * Google Scholar : recherchez des articles ou des livres dans une large base de données
  * arXiv : Cherchez des articles scientifiques parmi des archives de différentes disciplines scientifiques

* Sauvegarder vos recherches :
  * Zotero : Sauvegarder des articles intéressants sur son pc et les classer
  * Research Rabbit
  * Mendeley

### Les tips utiles :

* Pour obtenir la bonne traduction d’un terme technique, cherchez le dans une langue sur Wikipédia et changez la langue de l’article
* Avant de vous intéresser à une information très précise, il est bien de comprendre le contexte qui l’entoure. Soyez curieux lors de vos recherches !
 
