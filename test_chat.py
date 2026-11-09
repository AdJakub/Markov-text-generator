import json

from chat import fix_encoding, load_chat_messages


def test_fix_encoding_name():
    assert fix_encoding("Micha\u00c5\u0082") == "Michał"


def test_fix_encoding_sentence():
    assert fix_encoding("Pojeba\u00c5\u0082o ci\u00c4\u0099") == "Pojebało cię"


def test_load_old_format(tmp_path):
    data = {
        "messages": [
            {"sender_name": "Micha\u00c5\u0082", "content": "Siema"},
            {"sender_name": "Person A", "content": "Ide do sklepu"},
            {"sender_name": "Person A"},
        ]
    }
    path = tmp_path / "chat.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f)
    messages = load_chat_messages(path, "Person A")
    assert messages == ["Ide do sklepu"]
