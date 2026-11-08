from markov import build_ngram_counts, generate_text_backoff, get_tables
from stats import book_chunks, copy_score

text = "the cat sat on the mat. the cat ate the fish. the dog sat on the cat."
words = text.split()


def test_pairs_cat_text():
    test = build_ngram_counts(words, n=2)
    assert test[("the", "cat")] == {"sat": 1, "ate": 1}


def test_single_word_the():
    test2 = build_ngram_counts(words, n=1)
    assert test2[("the",)] == {"cat": 2, "mat.": 1, "fish.": 1, "dog": 1, "cat.": 1}


def test_copy_score():
    chunks = book_chunks(words, k=3)
    test = copy_score(text, chunks, k=3)
    assert test == 1
    test_sentence = "zebra banana purple"
    test2 = copy_score(test_sentence, chunks, k=3)


def test_backoff_length():
    tables = get_tables(words, 2)
    generated, counts = generate_text_backoff(tables, 2, 10)
    generated_words = generated.split()
    assert len(generated_words) == 12
    assert sum(counts.values()) == 10
