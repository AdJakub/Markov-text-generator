from markov import (
    build_ngram_counts,
    generate_text_backoff,
    generate_text_ngram,
    get_tables,
)
from stats import share_single_options


def print_result(words, max_n):
    result = get_tables(words, max_n)
    print(len(result[1]))
    print(len(result[2]))
    print(len(result[3]))


def tune_min_options(tables, settings, runs):
    for opt in settings:
        totals = dict()
        for _ in range(runs):
            text, counts = generate_text_backoff(tables, 3, 30, min_options=opt)
            for size in counts:
                if size not in totals:
                    totals[size] = 0
                totals[size] += counts[size]
        print(f"--- {opt} ---")
        print(totals)
        print(text)
