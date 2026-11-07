def share_single_options(table):
    single_count = 0
    for followers in table.values():
        if len(followers) == 1:
            single_count += 1
    return single_count / len(table)


def book_chunks(words, k):
    chunks = set()
    last_start = len(words) - k
    for i in range(last_start + 1):
        chunk = tuple(words[i : i + k])
        chunks.add(chunk)
    return chunks
