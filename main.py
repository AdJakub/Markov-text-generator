import argparse

from experiments import print_result, tune_min_options
from markov import generate_text_backoff, get_tables
from stats import book_chunks, copy_score
from utils import get_book_text, remove_header

parser = argparse.ArgumentParser()
parser.add_argument("book", help="file name of the book in books/")
parser.add_argument("--length", type=int, default=30, help="How many words to generate")
parser.add_argument(
    "--max-n",
    type=int,
    default=3,
    help="Biggest memory size (order of markov chain) (not stable above 3)",
)
parser.add_argument(
    "--min-options",
    type=int,
    default=2,
    help="best leave at default, copies the source text at 1 and is more gibberish at more than 2",
)
parser.add_argument(
    "--count", type=int, default=1, help="Ammount of sentences to generate"
)
parser.add_argument(
    "--experiment",
    action="store_true",
    help="run the copy-score tests and the min_options experiment",
)
args = parser.parse_args()


book_name = args.book
book_path = f"books/{book_name}"

book_text = get_book_text(book_path)
no_header = remove_header(book_text)
book_words = no_header.split()


tables = get_tables(book_words, args.max_n)
for _ in range(args.count):
    text, counts = generate_text_backoff(
        tables, args.max_n, args.length, min_options=args.min_options
    )
    print(text)
if args.experiment:
    book_chunk_set = book_chunks(book_words, 5)
    print(len(book_chunk_set))
    print(len(book_words))
    test_text = """On an exceptionally hot evening early in July a young man came out of
    the garret in which he lodged in S. Place and walked slowly, as though
    in hesitation,"""
    print("--- SANITY TEST ---")
    print(copy_score(test_text, book_chunk_set, 5))
    print("--- ACTUAL TEST --- ")
    print(copy_score(text, book_chunk_set, 5))
    tune_min_options(tables, range(1, 6), 30, book_chunk_set)
