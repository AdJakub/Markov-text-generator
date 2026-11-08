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


def copy_score(text, chunk_set, k):
    text_words = text.split()
    all_chunks = 0
    found_chunk = 0
    last_start = len(text_words) - k
    for i in range(last_start + 1):
        chunk = tuple(text_words[i : i + k])
        all_chunks += 1
        if chunk in chunk_set:
            found_chunk += 1
    if all_chunks == 0:
        return 0.0
    return found_chunk / all_chunks
