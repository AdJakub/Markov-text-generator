import random


def remove_header(text):
    try:
        start_book = text.index("START OF THE PROJECT GUTENBERG EBOOK")
        marker_end = text.index("***", start_book)
        end_book = text.index("*** END OF")
        no_header = text[marker_end + 3 : end_book]
        return no_header
    except ValueError:
        return text


def get_book_text(path):
    with open(path) as f:
        return f.read()
