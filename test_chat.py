from chat import fix_encoding


def test_fix_encoding_name():
    assert fix_encoding("Micha\u00c5\u0082") == "Michał"


def test_fix_encoding_sentence():
    assert fix_encoding("Pojeba\u00c5\u0082o ci\u00c4\u0099") == "Pojebało cię"
