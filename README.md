# Markov chain generator

[![forthebadge](/badges/0-percent-optimized.svg)](https://forthebadge.com)
![Hackatime stats](https://hackatime.hackclub.com/api/v1/badge/U0A4QT7PB5K/AdJakub/bookbot)

A command-line Markov chain text generator, that learnsf rom a book and writes new text in its style.

> The shy, unknown street? I shall be simply a puppy, and a pack of perspiration stood open. Peasants stood before his

1. it reads a book and builds tables of which words follow which 1, 2 or 3-wordsequences
2. generates text by picking the next word randomly, weighted by how often it appeared
3. uses longest memory when there's a real choice and uses backoff to fall back to shorter memory when there's only one option to avoid plagiarizing the source text
4. an originality checker that measures how much of the output is copied word for word

## Requirements

- Python 3 (no exterlan packages; only the standard library)

## Usage

Put a plain-text book from [Project Gutenberg](https://www.gutenberg.org) in the `books/` folder, then:

```bash
python3 main.py <book_file> [options]
```

| Option          | Default | Description                                                                                    |
| --------------- | ------- | ---------------------------------------------------------------------------------------------- |
| `--length`      | 30      | How many words to generate                                                                     |
| `--max-n`       | 3       | Biggest memory size (n-gram order)                                                             |
| `--min-options` | 2       | Backoff threshold: minimum number of possible next words before falling back to shorter memory |
| `--count`       | 1       | How many texts to generate                                                                     |
| `--experiment`  | off     | Run the copy-score tests and the min_options experiment                                        |

### Examples

```bash
python3 main.py crimeandpunishment.txt
```

```bash
wretched little beast was still life and strength that moment without this three roubles; I may have had nothing to do with you. I do no exactly.” “Do tell you something more essential
```

```bash
python3 main.py crimeandpunishment.txt --count 3 --length 50
```

```bash
spoke rather loud noise and animated conversation with a sharp little nose off with my sister--the day before yesterday.’ ‘And where did you go, will all keep him on the score of the old, dirty, by this. Then he remembered quite different. “Yes, Mr. Captain, and I am an ass; forgive myself for
why he went,” Raskolnikov by way will sing ‘My Village’ only, for the smart lady who was so unfortunate girl were asking your _fiancé_ in and weighed upon him. Here is some water. The feeling that it was like the latch on an empty tea-glass on a staircase, he mounted to tell you
scripture, too,” she was growing up, moved a night cap with new mourning had done _that_, could never bear that hardly audibly and God has smitten you, has no skill in such attire. Suddenly he withdrew his short-sighted eyes. You might well not such a fool I was afraid of!” Porfiry Petrovitch, receiving
```

````bash
python3 main.py crimeandpunishment.txt --experiment```
````

```bash
away in her will, ha-ha!). And she would not overlook anything. For the family who wanted a handkerchief, had turned the pocket is honourable. The vast quantities he said that he would not
202521
203612
--- SANITY TEST ---
1.0
--- ACTUAL TEST ---
0.034482758620689655
--- 1 ---
{3: 900}
0.9045977011494255
corner was disproportionately obtuse. There was scarcely any furniture in the big room: in the corner and several chairs--all government furniture, of polished yellow wood. In the further wall there was a time....
--- 2 ---
{1: 380, 2: 361, 3: 159}
0.08275862068965514
They’ve taken them food... I spoke about her mistrustfully, but that probably from his face. “And here... however queer, almost sullen insistence. “You’re right: she put them all so fond of Sonia? Sonia
--- 3 ---
{1: 509, 2: 313, 3: 78}
0.051724137931034475
this hesitating question, Sonia....” He stopped for me...” He rang the glass, put a stop here was the gate. She read loudly, cold with her own account, hasn’t said suddenly. “He is himself,”
--- 4 ---
{1: 555, 2: 288, 3: 57}
0.035632183908045977
and went in. He looked carefully and exactly what the doctor says!” Katerina Ivanovna, pale, thin spare the bridge. He became at parting for a poor student, or hunchback, I forgot! A plain,
--- 5 ---
{1: 599, 2: 266, 3: 35}
0.028735632183908046
“but what help the habit he said this with some other general’s.... Only just getting home in my opinions.... You know my opinion, and describing a change it, the business, and then to
```

## Results

Tested on _Crime and Punishment_ (about 200k words).

**Memory size vs copying** The longer the memory the more often there is one possible next word so the generator just copies the book:

| Memory  | Keys with only one possible next word |
| ------- | ------------------------------------- |
| 1 word  | 59%                                   |
| 2 words | 82%                                   |
| 3 words | 94%                                   |

**Backoff vs copying** Copy score = share of 5-0word chunks in the output that appear word for word in the book (average of 30 texts per setting):

| min_options    | 3-word memory used | Copy score |
| -------------- | ------------------ | ---------- |
| 1 (no backoff) | 100%               | 91%        |
| 2              | 16%                | 7.5%       |
| 3              | 10%                | 6.1%       |
| 4              | 5%                 | 2.6%       |
| 5              | 6%                 | 2.6%       |

backoff cuts the copying form 91% to about 7.5. above 2 copying barely drops and the text gets more mashed up. thats why 2 is the default

## Roadmap

- Generating text from other data sources like JSON
- Cleaning the source text depending on the type

## Credits

- Book source: Project gutenberg, shoutout :)
