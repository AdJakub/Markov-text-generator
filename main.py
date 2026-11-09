import argparse

from chat import load_chat_messages
from experiments import print_result, tune_min_options
from markov import generate_text_backoff, get_tables, get_tables_from_texts
from stats import book_chunks, copy_score
from storage import load_tables, save_tables
from utils import clean_text, get_book_text, remove_header

parser = argparse.ArgumentParser()
parser.add_argument("book", nargs="*", help="file name of the book in books/")
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
parser.add_argument(
    "--override-sentences",
    action="store_true",
    help="don't force texts to start with a capital and end with . ! or ?",
)
parser.add_argument(
    "--score",
    action="store_true",
    help="Show how much of each text is copied from the source material",
)
parser.add_argument("--save", help="Save the tables to this JSON file")
parser.add_argument(
    "--load", help="load tables from this JSON file instead of reading books"
)
parser.add_argument("--chat", nargs="+", help="one or more chat export files in chats/")
parser.add_argument(
    "--sender", help="whose messages to learn from (exact name as in the export"
)
args = parser.parse_args()
if not args.book and args.load is None and args.chat is None:
    parser.error("Give atleast one book, --chat FILES or --load FILE")
if args.chat and args.sender is None:
    parser.error("--chat needs --sender NAME")
if args.sender and args.chat is None:
    parser.error("Did you mean --chat?")

if args.load and (args.book or args.chat):
    parser.error("Use either books or --load, not both")
if args.load and (args.score or args.experiment):
    parser.error("--score and --experiment need the book text not just tables")
if args.load:
    try:
        tables = load_tables(args.load)
    except FileNotFoundError:
        parser.error(f"file {args.load} not found")
else:
    book_words = list()
    texts = list()
    for book_name in args.book:
        book_path = f"books/{book_name}"
        try:
            book_text = get_book_text(book_path)
        except FileNotFoundError:
            parser.error(f"Book {book_name} not found")
        no_header = remove_header(book_text)
        cleaned = clean_text(no_header)
        book_words.extend(cleaned.split())
        texts.append(cleaned.split())
    if args.chat:
        for chat_name in args.chat:
            chat_path = f"chats/{chat_name}"
            chat_messages = load_chat_messages(chat_path, args.sender)
            for message in chat_messages:
                book_words.extend(message.split())
                texts.append(message.split())
    tables = get_tables_from_texts(texts, args.max_n)
max_n = len(tables)
if args.save:
    save_tables(tables, args.save)


if args.score or args.experiment:
    book_chunk_set = book_chunks(book_words, 5)

for _ in range(args.count):
    text, counts = generate_text_backoff(
        tables,
        max_n,
        args.length,
        min_options=args.min_options,
        sentences=not args.override_sentences,
    )
    print(text)
    if not args.override_sentences and text[-1].endswith((".", "!", "?")) == False:
        print(
            "Error! Couldn't generate text ending with a sentence ending mark. Try again, or run with --override-sentences"
        )
        print("-------------")
    if args.score:
        score = copy_score(text, book_chunk_set, 5)
        percent = round(score * 100)
        print(f"copied: {percent}%")
if args.experiment:
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
