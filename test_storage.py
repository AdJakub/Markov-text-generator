from markovka.markov import get_tables
from markovka.storage import load_tables, save_tables

test_sentence = "the cat sat on the mat. the cat ate the fish. the dog sat on the cat."
test_sentence_PL = "Pchnąć w tę łódź jeża lub ośm skrzyń fig."


def test_round_trip(tmp_path):
    ammo = test_sentence.split()
    path = tmp_path / "tables.json"
    locked = get_tables(ammo, 3)
    save_tables(locked, path)
    loaded = load_tables(path)
    assert locked == loaded


def test_round_trip_polish(tmp_path):
    ammo = test_sentence_PL.split()
    path = tmp_path / "tables.json"
    locked = get_tables(ammo, 3)
    save_tables(locked, path)
    loaded = load_tables(path)
    assert locked == loaded
