
def process_text(text, check_spelling):
    return text if check_spelling(text) else f"[{text}]"


