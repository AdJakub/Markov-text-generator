import random
import sys

from utils import remove_header

book_name = sys.argv[1]
test_text = "the cat sat on the mat. the cat ate the fish. the dog sat on the cat."
book_path = f"books/{book_name}"


def get_book_text(path):
    with open(path) as f:
        return f.read()


book_text = get_book_text(book_path)
no_header = remove_header(book_text)
# print(no_header[:200])
book_words = no_header.split()


# version A
def build_follower_lists(words):
    follower_lists = {}

    for i in range(0, len(words) - 1):
        current_word = words[i]
        next_word = words[i + 1]
        if current_word not in follower_lists:
            follower_lists[current_word] = list()
        follower_lists[current_word].append(next_word)
    return follower_lists


follower_lists = build_follower_lists(book_words)


# version B
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


follower_counts = build_follower_counts(book_words)
# print(test_words, len(test_words))
# print(follower_lists)
# print(follower_counts)
print(len(follower_counts))
print(len(follower_lists["the"]))
print(len(follower_counts["the"]))
print(sum(follower_counts["the"].values()))


def get_count(pair):
    return pair[1]


the_pairs = list(follower_counts["the"].items())
the_pairs.sort(key=get_count, reverse=True)
print(the_pairs[:10])
weights_list = list(follower_counts["the"].values())
options = list(follower_counts["the"].keys())
# print(picked[0])
pick_counts_b = dict()
# version B picking
for i in range(600):
    picked = list(random.choices(options, weights=weights_list))
    word = picked[0]
    if word not in pick_counts_b:
        pick_counts_b[word] = 0
    pick_counts_b[word] += 1

# version A picking
pick_counts_a = dict()
for i in range(600):
    picked = random.choice(follower_lists["the"])
    word = picked
    if word not in pick_counts_a:
        pick_counts_a[word] = 0
    pick_counts_a[word] += 1
