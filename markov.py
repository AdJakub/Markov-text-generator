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
