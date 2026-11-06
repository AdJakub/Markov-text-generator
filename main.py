import random
import sys

book_name = sys.argv[1]
test_text = "the cat sat on the mat. the cat ate the fish. the dog sat on the cat."
book_location = f"books/{book_name}"

# with open(bookLocation) as f:
#    print(f.read())


test_words = test_text.split()

# version A
follower_lists = {}

for i in range(0, len(test_words) - 1):
    current_word = test_words[i]
    next_word = test_words[i + 1]
    if current_word not in follower_lists:
        follower_lists[current_word] = list()
    follower_lists[current_word].append(next_word)

    print(f"{current_word} -> {next_word}")

# version B
follower_counts = {}
for i in range(0, len(test_words) - 1):
    current_word = test_words[i]
    next_word = test_words[i + 1]
    if current_word not in follower_counts:
        follower_counts[current_word] = dict()
    if next_word not in follower_counts[current_word]:
        follower_counts[current_word][next_word] = 0

    follower_counts[current_word][next_word] += 1


# print(test_words, len(test_words))
# print(follower_lists)
# print(follower_counts)

weights_list = list(follower_counts["the"].values())
options = list(follower_counts["the"].keys())
# print(picked[0])
pick_counts = dict()
# version B picking
# for i in range(600):
#   picked = list(random.choices(options, weights=weights_list))
#  word = picked[0]
# if word not in pick_counts:
#    pick_counts[word] = 0
# pick_counts[word] += 1

# print(pick_counts)

# version A picking
pick_counts_b = dict()
for i in range(600):
    picked = random.choice(follower_lists["the"])
    word = picked
    if word not in pick_counts_b:
        pick_counts_b[word] = 0
    pick_counts_b[word] += 1

print(pick_counts_b)
