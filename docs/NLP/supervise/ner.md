# NER : Named-entity recognition - Détection d'entités nommées

La détection d'entités nommées consiste d'extraire d'un texte des objets ayant une thématique recherchée.

Dans la phrase *« Anis a encore stream sur Twitch»*, on peut extraire les 2 entités suivantes :
- *Anis* est le prénom de ton streameur préféré.
- *Twitch* est la plateforme où se déroule ses streams.

Essayer de détecter ces entités est donc une procédure d'apprentissage supervisé, puisqu'à partir d'une caractéristique textuelle (Twitch), l'objectif est de prédire une entité (une plateforme).

## Modélisation du problème

On considère que l'on a une séquence d'observations (mots d'une phrase) et l'on souhaite prédire la séquence d'entités associée
Par exemple : <br> 

| Anis | a | encore | stream | sur | Twitch |
|-------|------|----|-------|---|-------|
| Prénom | O | O | O | O | Plateforme |

## En pratique

### Cas classiques

Dans le cas où les entités à détecter sont dites "classiques" (Lieu : France, date : 1998, personne : Zidane .. ), il serait contre-productif de réimplémenter un modèle. 

Il est préférable dans ce cas d'exploiter des modèles déjà entraînés (en anglais et/ou français), comme ceux disponibles dans la librairie [spaCy](https://spacy.io). 

```bash
pip install -U spacy
!python3 -m spacy download fr_core_news_sm
```

```python
import spacy

nlp = spacy.load('fr_core_news_sm')
doc = nlp(u'En 1998, Zidane a permi à la France de remporter la coupe du monde.')

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

Zidane 9 15 PER
la France 26 35 LOC
```

### Cas spécifiques

Dans le cas où les entités à détecter sont spécifiques à un domaine particulier (industrie, santé, recherche ..), il faut entraîner un modèle.

La première alternative consiste en la spécialisation d'un modèle existant aux entités pertinentes du problème. Une fois encore, il est possible de se reposer sur la librairie [spaCy](https://spacy.io).


```

Créer un folder nlp_iaz, copier coller le snippet de code ci-dessous au sein d'un fichier .py puis installer les packages au sein d'un virtual environment : 

python3 -m venv env
source env/bin/activate
pip install spacy plac
```

```python
"""
Training: https://spacy.io/usage/training
NER: https://spacy.io/usage/linguistic-features#named-entities
"""

import plac
import random
from pathlib import Path
import spacy
from spacy.training.example import Example

# training data
TRAIN_DATA = [
    ('Qui est Zidane?', {
        'entities': [(8, 14, 'PERSON')]
    }),
    ('Je supporte Paris et le Bayern.', {
        'entities': [(12, 17, 'LOC'), (24, 30, 'LOC')]
    })
]

@plac.annotations(
    model=("Model name. Defaults to blank 'fr' model.", "option", "m", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int))
def main(model=None, output_dir=None, n_iter=100):
    """Load the model, set up the pipeline and train the entity recognizer."""
    if model is not None:
        nlp = spacy.load(model)  
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('fr') 

    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe('ner', last=True)
    else:
        ner = nlp.get_pipe('ner')

    for _, annotations in TRAIN_DATA:
        for ent in annotations.get('entities'):
            ner.add_label(ent[2])

    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes): 
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            losses = {}
            for text, annotations in TRAIN_DATA:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update(
                    [example],  
                    drop=0.5,  # dropout 
                    sgd=optimizer, 
                    losses=losses)
            print(losses)
    

    for text, _ in TRAIN_DATA:
        doc = nlp(text)
        print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
        print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])

    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.to_disk(output_dir)

        nlp2 = spacy.load(output_dir)
        for text, _ in TRAIN_DATA:
            doc = nlp2(text)
            print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
            print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])


if __name__ == '__main__':
    plac.call(main)

    # Expected output:
    # Entities [('Zidane', 'PERSON')]
    # Tokens [('Qui', '', 2), ('est', '', 2), ('Zidane', 'PERSON', 3), ('?', '', 2)]
    # Entities [('Paris', 'LOC'), ('Bayern', 'LOC')]
    # Tokens [('Je', '', 2), ('supporte', '', 2), ('Paris', 'LOC', 3), ('et', '', 2), ('le', '', 2), ('Bayern', 'LOC', 3), ('.', '', 2)]
```

Pour utiliser cette démarche avec Spacy, il est nécessaire d'avoir un TRAIN_DATA dans ce format.
Si vous souhaitez créer un TRAIN_DATA avec ce format en utilisant plusieurs centaines/milliers de phrases puis de réutiliser la démarche précédente, il est possible de le faire en suivant ce blog : https://thinkinfi.com/prepare-training-data-and-train-custom-ner-using-spacy-python/.


## Librairies

- **pytorch-transformers** ([Hugging Face](https://github.com/huggingface/pytorch-transformers))
- **Flair** ([Flair](https://github.com/zalandoresearch/flair))