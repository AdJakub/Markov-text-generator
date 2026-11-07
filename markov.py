import random


#  build the table
def build_follower_counts(words):
    follower_counts = {}
    for i in range(0, len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word not in follower_counts:
            follower_counts[current_word] = dict()
        if next_word not in follower_counts[current_word]:
            follower_counts[current_word][next_word] = 0

        follower_counts[current_word][next_word] += 1
    return follower_counts


def build_pair_counts(words):
    pair_counts = {}
    for i in range(0, len(words) - 2):
        first_word = words[i]
        second_word = words[i + 1]
        current_pair = (first_word, second_word)
        next_word = words[i + 2]
        if current_pair not in pair_counts:
            pair_counts[current_pair] = dict()
        if next_word not in pair_counts[current_pair]:
            pair_counts[current_pair][next_word] = 0

        pair_counts[current_pair][next_word] += 1
    return pair_counts


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
def generate_text(table, start_word, length):
    current = start_word
    generated = [start_word]
    all_words = list(table.keys())
    for i in range(length):
        if current not in table:
            current = random.choice(all_words)
        options = list(table[current].keys())
        weights = list(table[current].values())
        next_word = random.choices(options, weights=weights)[0]
        generated.append(next_word)
        current = next_word
    result_seperator = " "
    result = result_seperator.join(generated)
    return result


def generate_text_pairs(table, length):
    all_pairs = list(table.keys())
    current = random.choice(all_pairs)
    generated = list((current[0], current[1]))

    for i in range(length):
        if current not in table:
            current = random.choice(all_pairs)
        options = list(table[current].keys())
        weights = list(table[current].values())
        next_word = random.choices(options, weights=weights)[0]
        generated.append(next_word)
        current = (current[1], next_word)
    result_seperator = " "
    result = result_seperator.join(generated)
    return result


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
