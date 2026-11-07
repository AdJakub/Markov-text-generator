from markov import (
    build_ngram_counts,
    generate_text_backoff,
    generate_text_ngram,
    get_tables,
)
from stats import copy_score, share_single_options


def print_result(words, max_n):
    result = get_tables(words, max_n)
    print(len(result[1]))
    print(len(result[2]))
    print(len(result[3]))


def tune_min_options(tables, settings, runs, chunk_set):
    for opt in settings:
        totals = dict()
        score_sum = 0
        for _ in range(runs):
            text, counts = generate_text_backoff(tables, 3, 30, min_options=opt)
            score_sum += copy_score(text, chunk_set, 5)
            for size in counts:
                if size not in totals:
                    totals[size] = 0
                totals[size] += counts[size]
        average = score_sum / runs

        print(f"--- {opt} ---")
        print(totals)
        print(average)
        print(text)
