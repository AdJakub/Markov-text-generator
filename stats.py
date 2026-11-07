def share_single_options(table):
    single_count = 0
    for followers in table.values():
        if len(followers) == 1:
            single_count += 1
    return single_count / len(table)
