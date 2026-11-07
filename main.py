import sys

from markov import (
    build_follower_counts,
    build_ngram_counts,
    build_pair_counts,
    generate_text,
    generate_text_pairs,
    generate_text_ngram
)
from stats import share_single_options
from utils import get_book_text, remove_header

if len(sys.argv) != 2:
    print("usage: python3 main.py bookname.txt")
else:
    book_name = sys.argv[1]
    book_path = f"books/{book_name}"

    book_text = get_book_text(book_path)
    no_header = remove_header(book_text)
    book_words = no_header.split()

    pair_counts = build_pair_counts(book_words)
    print(len(pair_counts))
    print(list(pair_counts)[:5])
    print(share_single_options(pair_counts))
    follower_counts = build_follower_counts(book_words)
    print("--- VERSION A ---")
    print(generate_text(follower_counts, "The", 20))
    print("---VERSION B ---")
    print(generate_text_pairs(pair_counts, 20))
    print(share_single_options(follower_counts))

