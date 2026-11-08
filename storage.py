import json


def save_tables(tables, path):
    json_ready = dict()
    key_seperator = " "
    for n in tables:
        table = tables[n]
        string_table = dict()
        for key in table:
            string_key = key_seperator.join(key)
            string_table[string_key] = table[key]
        json_ready[n] = string_table
    with open(path, "w", encoding="utf-8") as f:
        json.dump(json_ready, f, ensure_ascii=False)


def load_tables(path):
    with open(path, encoding="utf-8") as f:
        loaded = json.load(f)
    tables = dict()
    for n_string in loaded:
        n = int(n_string)
        string_table = loaded[n_string]
        table = dict()
        for string_key in string_table:
            key = tuple(string_key.split())
            table[key] = string_table[string_key]
        tables[n] = table
    return tables
