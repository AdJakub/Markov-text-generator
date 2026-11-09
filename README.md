# markovka

[![forthebadge](https://forthebadge.com/badges/0-percent-optimized.svg)](https://forthebadge.com)

markovka is a Markov chain text generator. Feed it plain-text books from [Project Gutenberg](https://www.gutenberg.org), Messenger chat exports, or both, and it writes new text in their style. It counts which words follow which 1, 2 or 3-word sequences, picks each next word at random weighted by those counts, and falls back to shorter memory when the longer one has only one option, so it doesn't just copy the source. There's also a talk mode, where it answers whatever you type, in a command-line version and a small GUI.

> The shy, unknown street? I shall be simply a puppy, and a pack of perspiration stood open. Peasants stood before his

## Install

```bash
pip install markovka
```

You need Python 3.10 or newer. There are no other dependencies, but the GUI needs tkinter (on Debian/Ubuntu that's `sudo apt install python3-tk`).

### Windows app

A `.exe` of the GUI is available on the [GitHub Releases page](https://github.com/AdJakub/Markov-text-generator/releases), no Python needed.

The exe is unsigned, so Windows SmartScreen may warn you when you open it. Click "More info", then "Run anyway".

## GUI

```bash
python -m markovka.gui
```

- **Choose book...** picks a plain-text book (`.txt`).
- **Choose chat...** picks a Messenger export (`.json`). Type the name into "Sender name" first, and it must match exactly as in the export.
- **Combining sources:** every book or chat you pick gets added to the mix. To start over, restart the app.
- **Length box:** how many words to write, 5 to 300 (default 30). It's approximate, since the text keeps going until a sentence ends.
- **Generate** writes a new text.
- **Talk...** opens a chat window. Press Enter or Send, and it tries to start its reply from the longest word in your message that it knows.

Books use 3-word memory. As soon as a chat is loaded, everything uses 2-word memory. Saving tables and copy scores are CLI only.

## CLI

Books are read from `books/` and chats from `chats/`, relative to the folder you run it in. Just give the file name.

```bash
# one book
markovka crimeandpunishment.txt

# three texts of about 50 words
markovka crimeandpunishment.txt --count 3 --length 50

# multiple books
markovka crimeandpunishment.txt frankenstein.txt

# a chat (the sender name must match the export exactly)
markovka --chat message_1.json --sender "Your Friend" --max-n 2 --override-sentences

# books and a chat together (books go first, --chat takes every file after it)
markovka frankenstein.txt --chat message_1.json --sender "Your Friend"

# talk to it (/quit or Ctrl+C to leave)
markovka crimeandpunishment.txt --talk

# save the tables, then reuse them without rereading the book
markovka crimeandpunishment.txt --save tables.json
markovka --load tables.json --length 50

# how much of the output is copied word for word
markovka crimeandpunishment.txt --score

# same, but 3 words in a row count as copied (better for chats)
markovka --chat message_1.json --sender "Your Friend" --max-n 2 --score --score-k 3

# copy-score tests and the min_options experiment
markovka crimeandpunishment.txt --experiment
```

| Flag                   | Default | Description                                                                    |
| ---------------------- | ------- | ------------------------------------------------------------------------------ |
| `book` (positional)    | none    | One or more book file names in `books/`                                        |
| `--length`             | 30      | How many words to generate                                                     |
| `--max-n`              | 3       | Biggest memory size (order of the chain). 3 is best for books, try 2 for chats |
| `--min-options`        | 2       | Backoff threshold. 1 copies the source, above 2 gets more gibberish            |
| `--count`              | 1       | How many texts to generate                                                     |
| `--experiment`         | off     | Run the copy-score tests and the min_options experiment                        |
| `--override-sentences` | off     | Don't force texts to start with a capital and end with `.`, `!` or `?`         |
| `--score`              | off     | Show how much of each text is copied from the source                           |
| `--score-k`            | 5       | How many words in a row count as copied, try 3 for chats                       |
| `--save`               | none    | Save the tables to this JSON file                                              |
| `--load`               | none    | Load tables from this JSON file instead of reading books                       |
| `--chat`               | none    | One or more chat export files in `chats/`                                      |
| `--sender`             | none    | Whose messages to learn from (exact name as in the export)                     |
| `--talk`               | off     | Talk with the generator                                                        |

Some rules:

- You need at least one book, `--chat` or `--load`.
- `--chat` and `--sender` only work together.
- `--load` can't be combined with books, `--chat`, `--score` or `--experiment`, because those need the original text.
- `--experiment` assumes the defaults for `--max-n` and `--score-k`, and its sanity test is a line from _Crime and Punishment_, so it only scores 1.0 on that book.

### Sample outputs

```bash
markovka crimeandpunishment.txt
```

```text
wretched little beast was still life and strength that moment without this three roubles; I may have had nothing to do with you. I do no exactly.” “Do tell you something more essential
```

```bash
markovka crimeandpunishment.txt --count 3 --length 50
```

```text
spoke rather loud noise and animated conversation with a sharp little nose off with my sister--the day before yesterday.’ ‘And where did you go, will all keep him on the score of the old, dirty, by this. Then he remembered quite different. “Yes, Mr. Captain, and I am an ass; forgive myself for
why he went,” Raskolnikov by way will sing ‘My Village’ only, for the smart lady who was so unfortunate girl were asking your _fiancé_ in and weighed upon him. Here is some water. The feeling that it was like the latch on an empty tea-glass on a staircase, he mounted to tell you
scripture, too,” she was growing up, moved a night cap with new mourning had done _that_, could never bear that hardly audibly and God has smitten you, has no skill in such attire. Suddenly he withdrew his short-sighted eyes. You might well not such a fool I was afraid of!” Porfiry Petrovitch, receiving
```

```bash
markovka crimeandpunishment.txt --experiment
```

```text
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

```bash
markovka crimeandpunishment.txt --score
```

```text
After brief hesitation at the police office? Where’s the greatest suspicion of any folly.” They simply looked rather irregular for that moment when he stood with the axe in the noose, he tried to hang himself, and that I did not ask forgiveness, but he was in a fever of dust of the street.
copied: 18%
```

## Getting a Messenger export

On Facebook, go to Settings, then "Download your information". Pick your messages and set the format to **JSON** (not HTML). Once the download is ready, unzip it and find the chat's folder under `messages/inbox/`. The file you want looks like `message_1.json`.

For the sender name, use the name as it appears in the chat, with normal letters. Accented characters look garbled in the raw file, but markovka fixes that when it reads them. A wrong name means no messages get loaded.

## Privacy

Chat exports contain private messages, and saved tables do too, since they're built from those messages. Never commit or share them. This repo's `.gitignore` covers `*.json`, so give saved tables a `.json` name or they won't be ignored.

## Results

Tested on _Crime and Punishment_ (about 200k words).

**Memory size vs copying.** The longer the memory, the more often there's only one possible next word, so the generator just copies the book:

| Memory  | Keys with only one possible next word |
| ------- | ------------------------------------- |
| 1 word  | 59%                                   |
| 2 words | 82%                                   |
| 3 words | 94%                                   |

**Backoff vs copying.** Copy score = share of 5-word chunks in the output that appear word for word in the book (average of 30 texts per setting):

| min_options    | 3-word memory used | Copy score |
| -------------- | ------------------ | ---------- |
| 1 (no backoff) | 100%               | 91%        |
| 2              | 16%                | 7.5%       |
| 3              | 10%                | 6.1%       |
| 4              | 5%                 | 2.6%       |
| 5              | 6%                 | 2.6%       |

Backoff cuts the copying from 91% to about 7.5%. Above 2 the copying barely drops and the text gets more mashed up, which is why 2 is the default.

## Known limitations

- Sentence ends inside quotes like "Good-bye!" aren't recognised as sentence ends
- A sentence start is detected by a capital letter, so names in the middle of a sentence can also be picked as starts
- In rare cases no sentence end is found within the limit and the program prints a warning
- For text without capitals or punctuation, like chats, use `--override-sentences`

## Running tests

From a clone of the repo:

```bash
pip install pytest
pytest
```

The tests cover tables, backoff generation, copy score, header removal, cleaning, chat loading and saving/loading tables.

## Project structure

```
markovka/
  __init__.py     package marker (empty)
  main.py         CLI and argparse flags
  gui.py          tkinter GUI
  markov.py       builds the tables and generates text
  chat.py         reads Messenger exports and fixes their encoding
  utils.py        reads books, strips Gutenberg headers, cleans text
  stats.py        copy score and table stats
  storage.py      saves and loads tables as JSON
  experiments.py  the min_options experiment
```

## License

Public domain ([The Unlicense](LICENSE)). Book source: Project Gutenberg, shoutout :)
