import argparse

from experiments import print_result, tune_min_options
from markov import generate_text_backoff, get_tables
from stats import book_chunks, copy_score
from utils import get_book_text, remove_header

parser = argparse.ArgumentParser()
parser.add_argument("book", help="file name of the book in books/")
args = parser.parse_args()


book_name = args.book
book_path = f"books/{book_name}"

book_text = get_book_text(book_path)
no_header = remove_header(book_text)
book_words = no_header.split()
book_chunk_set = book_chunks(book_words, 5)
print(len(book_chunk_set))
print(len(book_words))

tables = get_tables(book_words, 3)
text, counts = generate_text_backoff(tables, 3, 30)
test_text = """On an exceptionally hot evening early in July a young man came out of
the garret in which he lodged in S. Place and walked slowly, as though
in hesitation,"""
print("--- SANITY TEST ---")
print(copy_score(test_text, book_chunk_set, 5))
print("--- ACTUAL TEST --- ")
print(copy_score(text, book_chunk_set, 5))
tune_min_options(tables, range(1, 6), 30, book_chunk_set)
