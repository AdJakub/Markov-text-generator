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


print(test_words, len(test_words))
print(follower_lists)
print(follower_counts)
