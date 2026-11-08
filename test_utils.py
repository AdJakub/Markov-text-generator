from utils import clean_text, remove_header


def test_text_without_markets():
    test_text = "The quick brown fox jumped over the lazy cat"
    test = remove_header(test_text)
    assert test == test_text


def test_text_with_markers():
    test_text = "*** START OF THE PROJECT GUTENBERG EBOOK TEST BOOK *** hello world *** END OF THE PROJECT GUTENBERG EBOOK TEST BOOK ***"
    test = remove_header(test_text)
    assert test.strip() == "hello world"


def test_clean_text_removes_chapter():
    test_text = "He went out into the street.\nCHAPTER II\nHe had never been in a tavern before."
    expected = "He went out into the street.\nHe had never been in a tavern before."
    assert clean_text(test_text) == expected


def test_clean_text_removes_part():
    test_text = "That was the end of it.\nPART I\nIt was a hot evening in July."
    expected = "That was the end of it.\nIt was a hot evening in July."
    assert clean_text(test_text) == expected


def test_clean_text_removes_underscores():
    test_text = "I told her about _that_ letter."
    expected = "I told her about that letter."
    assert clean_text(test_text) == expected


def test_clean_text_unchanged():
    test_text = "The old woman opened the door.\nShe looked at him suspiciously."
    expected = test_text
    assert clean_text(test_text) == expected
