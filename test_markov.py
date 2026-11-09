from markov import (
    build_ngram_counts,
    generate_text_backoff,
    get_tables,
    get_tables_from_texts,
    normalize,
)
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
    assert len(generated_words) >= 12
    assert sum(counts.values()) >= 10


def test_copy_score_too_short():
    test_sentence = "the cat"
    chunks = book_chunks(words, k=3)

    score = copy_score(test_sentence, chunks, k=3)
    assert score == 0.0


sentence_text = "The cat sat on the mat. The dog ate the fish. A bird sang loudly! Did the cat sleep? The dog barked at the bird."
sentence_words = sentence_text.split()


def test_ends_with_sentence_end():
    tables = get_tables(sentence_words, 2)
    for _ in range(20):
        text, counts = generate_text_backoff(tables, 2, 5)
        results = text.split()
        assert results[-1].endswith((".", "!", "?")) or len(results) - 2 == 5 * 3, (
            results
        )


def test_starts_with_capital():
    tables = get_tables(sentence_words, 2)
    for _ in range(20):
        text, counts = generate_text_backoff(tables, 2, 5)
        results = text.split()
        assert results[0][0].isupper() == True, results


def test_message_boundaries():
    texts = [["a", "b", "c"], ["d", "e", "f"]]
    tables = get_tables_from_texts(texts, 1)
    assert tables[1][("a",)] == {"b": 1}
    assert ("c",) not in tables[1]


def test_start_word():
    tables = get_tables(sentence_words, 2)
    for _ in range(20):
        text, count = generate_text_backoff(tables, 2, 5, start_word="dog")
        result = text.split()
        assert result[0] == "dog"


def test_start_word_unknown():
    tables = get_tables(sentence_words, 2)
    for _ in range(20):
        text, count = generate_text_backoff(tables, 2, 5, start_word="zebra")
        result = text.split()
        assert len(result) > 0


def test_normalize():
    text = "Piwo?"
    text2 = "piwo"
    text3 = "...Dog!"
    expected = "piwo"
    expected2 = "dog"
    assert normalize(text) == expected
    assert normalize(text2) == expected
    assert normalize(text3) == expected2
