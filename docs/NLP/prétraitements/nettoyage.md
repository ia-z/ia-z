# Nettoyage

Sujet incontournable dans tout projet de NLP, le preprocessing est une étape importante car un langage est rarement propre : 

- balises html non pertinentes
- Fautes d'orthographe
- Caractères spéciaux 

 Le français compte plus de 30 000 mots. Cela engendre la résolution de problèmes en très très grande dimension. L'objectif du preprocessing est de diminuer la dimension de notre espace de travail.

## Expressions régulières

Les expressions régulières nous aiderons à nettoyer du texte. Ci-dessous quelques exemples récurrents.

### Adresses Email
```python
import re
match = re.search('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)', word)
```

### Balises HTML
```python
import re
sentence = re.sub('<[^>]*>', '', sentence)
sentence = re.sub('\[[^\]]*\]', '', sentence)
sentence = re.sub('{[^{]*}', '', sentence)
sentence = re.sub('div* ', '', sentence)
sentence = re.sub('\.text[1-9]', '', sentence)
sentence = re.sub('http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', sentence)
sentence = re.sub('www\.(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', sentence)
```

## Lowercase

Cette opération de mettre en minuscule le texte permet de diminuer la dimension de l'espace de travail

```python
new_sentence = sentence.lower()
```

## Les accents

Un autre moyen de diminuer la dimension du problème est de ramener les accents à leur forme *ASCII* "racine". Par exemple, transformer « é » en « e » : 

```python
import unicodedata

def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

s = strip_accents('dééfênndre intêlligénce')
```
