import random


#  build the table
def build_ngram_counts(words, n):
    ngram_counts = {}
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


def generate_text_backoff(tables, max_n, length, min_options=2):
    all_keys = list(tables[max_n].keys())
    current = random.choice(all_keys)
    generated = list(current)

    for i in range(length):
        picked = None
        for n in range(max_n, 0, -1):
            key = tuple(generated[-n:])
            table = tables[n]
            if key in table and (len(table[key]) >= min_options or n == 1):
                options = list(table[key].keys())
                weights = list(table[key].values())
                picked = random.choices(options, weights=weights)[0]
                break
        if picked is None:
            single_word_table = tables[1]
            keys = single_word_table.keys()
            key_list = list(keys)
            random_key = random.choice(key_list)
            picked = random_key[0]
        generated.append(picked)
    result_seperator = " "
    result = result_seperator.join(generated)
    return result


def get_tables(words, max_n):
    tables = dict()
    for n in range(1, max_n + 1):
        tables[n] = build_ngram_counts(words, n)
    return tables


def print_result(words, max_n):
    result = get_tables(words, max_n)
    print(len(result[1]))
    print(len(result[2]))
    print(len(result[3]))
