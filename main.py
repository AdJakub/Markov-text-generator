import sys

from markov import build_follower_counts, generate_text
from utils import get_book_text, remove_header

book_name = sys.argv[1]
book_path = f"books/{book_name}"


book_text = get_book_text(book_path)
no_header = remove_header(book_text)
book_words = no_header.split()


follower_counts = build_follower_counts(book_words)


print(generate_text(follower_counts, "The", 20))
