import json


def fix_encoding(text):
    raw_bytes = text
    fixed = raw_bytes.encode("latin1")
    result = fixed.decode("utf-8")
    return result


def load_chat_messages(path, sender):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    messages = list()
    for message in data["messages"]:
        if "sender_name" in message:
            name = fix_encoding(message["sender_name"])
            text = message.get("content")
            if text != None:
                text = fix_encoding(text)
        else:
            name = message.get("senderName")
            text = message.get("text")
        if name == sender and text:
            messages.append(text)
    return messages
