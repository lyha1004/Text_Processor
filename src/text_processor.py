
def is_valid_word(valid_word):
    return True


def process_file(text, is_valid_word):
    return text if is_valid_word(text) else f"[{text}]"


