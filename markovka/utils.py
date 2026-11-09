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


def clean_text(text):
    lines = text.splitlines()
    kept = list()
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("CHAPTER") or stripped.startswith("PART"):
            continue
        kept.append(stripped)
    result = "\n".join(kept)
    no_april_underscores = result.replace("_", "")
    return no_april_underscores
