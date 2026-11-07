import sys

from markov import (
    build_ngram_counts,
    generate_text_backoff,
    generate_text_ngram,
    get_tables,
    print_result,
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

    print_result(book_words, 3)
    tables = get_tables(book_words, 3)
    print(generate_text_backoff(tables, 3, 30))
    print(generate_text_backoff(tables, 3, 30))
    print(generate_text_backoff(tables, 3, 30))
    # table = build_ngram_counts(book_words, n)
    # print(f"--- SIZE {n} ---")
    # print(share_single_options(table))
    # print(generate_text_ngram(table, 20))
