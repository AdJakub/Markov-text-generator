# Markov chain reader

huge WIP, so far i got a working markov chain table generator working

version A:

```
{'the': ['cat', 'mat.', 'cat', 'fish.', 'dog', 'cat.'], 'cat': ['sat', 'ate'], 'sat': ['on', 'on'], 'on': ['the', 'the'], 'mat.': ['the'], 'ate': ['the'], 'fish.': ['the'], 'dog': ['sat']}
```

version B:

```
{'the': {'cat': 2, 'mat.': 1, 'fish.': 1, 'dog': 1, 'cat.': 1}, 'cat': {'sat': 1, 'ate': 1}, 'sat': {'on': 2}, 'on': {'the': 2}, 'mat.': {'the': 1}, 'ate': {'the': 1}, 'fish.': {'the': 1}, 'dog': {'sat': 1}}
```
