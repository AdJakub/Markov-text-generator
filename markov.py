import random


#  build the table
def build_ngram_counts(words, n, counts=None):
    if counts == None:
        ngram_counts = {}
    else:
        ngram_counts = counts
    for i in range(0, len(words) - n):
        current_key = tuple(words[i : i + n])
        next_word = words[i + n]
        if current_key not in ngram_counts:
            ngram_counts[current_key] = dict()
        if next_word not in ngram_counts[current_key]:
            ngram_counts[current_key][next_word] = 0

        ngram_counts[current_key][next_word] += 1
    return ngram_counts


# generating text
def generate_text_ngram(table, length):
    all_keys = list(table.keys())
    current = random.choice(all_keys)
    generated = list(current)
    n = len(current)

    for i in range(length):
        if current not in table:
            current = random.choice(all_keys)
        options = list(table[current].keys())
        weights = list(table[current].values())
        next_word = random.choices(options, weights=weights)[0]
        generated.append(next_word)
        current = tuple(generated[-n:])
    result_seperator = " "
    result = result_seperator.join(generated)
    return result


def generate_text_backoff(tables, max_n, length, min_options=2, sentences=True):
    all_keys = list(tables[max_n].keys())
    start_keys = list()
    for key in all_keys:
        if key[0][0].isupper():
            start_keys.append(key)
    if len(start_keys) == 0:
        start_keys = all_keys
    if sentences == False:
        start_keys = all_keys
    current = random.choice(start_keys)
    generated = list(current)
    sizes_used = dict()
    if sentences == True:
        max_rounds = length * 3
    else:
        max_rounds = length
    for i in range(max_rounds):
        picked = None
        for n in range(max_n, 0, -1):
            key = tuple(generated[-n:])
            table = tables[n]
            if key in table and (len(table[key]) >= min_options or n == 1):
                options = list(table[key].keys())
                weights = list(table[key].values())
                picked = random.choices(options, weights=weights)[0]
                if n not in sizes_used:
                    sizes_used[n] = 0
                sizes_used[n] += 1
                break
        if picked is None:
            single_word_table = tables[1]
            keys = single_word_table.keys()
            key_list = list(keys)
            random_key = random.choice(key_list)
            picked = random_key[0]
            if "jump" not in sizes_used:
                sizes_used["jump"] = 0
            sizes_used["jump"] += 1
        generated.append(picked)
        if sentences and i + 1 >= length and generated[-1].endswith((".", "!", "?")):
            break
    result_seperator = " "
    result = result_seperator.join(generated)
    return result, sizes_used


def get_tables(words, max_n):
    tables = dict()
    for n in range(1, max_n + 1):
        tables[n] = build_ngram_counts(words, n)
    return tables


def get_tables_from_texts(texts, max_n):
    tables = dict()
    for n in range(1, max_n + 1):
        tables[n] = dict()
    for words in texts:
        for n in range(1, max_n + 1):
            build_ngram_counts(words, n, tables[n])
    return tables


def print_result(words, max_n):
    result = get_tables(words, max_n)
    print(len(result[1]))
    print(len(result[2]))
    print(len(result[3]))
