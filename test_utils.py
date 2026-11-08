from utils import remove_header


def test_text_without_markets():
    test_text = "The quick brown fox jumped over the lazy cat"
    test = remove_header(test_text)
    assert test == test_text


def test_text_with_markers():
    test_text = "*** START OF THE PROJECT GUTENBERG EBOOK TEST BOOK *** hello world *** END OF THE PROJECT GUTENBERG EBOOK TEST BOOK ***"
    test = remove_header(test_text)
    assert test.strip() == "hello world"
