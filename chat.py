def fix_encoding(text):
    raw_bytes = text
    fixed = raw_bytes.encode("latin1")
    result = fixed.decode("utf-8")
    return result
