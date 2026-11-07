import sys

from experiments import print_result, tune_min_options
from markov import generate_text_backoff, get_tables
from stats import book_chunks
from utils import get_book_text, remove_header

if len(sys.argv) != 2:
    print("usage: python3 main.py bookname.txt")
else:
    book_name = sys.argv[1]
    book_path = f"books/{book_name}"

    book_text = get_book_text(book_path)
    no_header = remove_header(book_text)
    book_words = no_header.split()
    book_chunk_set = book_chunks(book_words, 5)
    print(len(book_chunk_set))
    print(len(book_words))

    tables = get_tables(book_words, 3)
    text, counts = generate_text_backoff(tables, 3, 30)
    # tune_min_options(tables, range(1, 6), 30)
