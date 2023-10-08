def process_text(text, check_spelling):
    result = [word if check_spelling(word) else f"[{word}]" for word in text.split()]
    return " ".join(result)
