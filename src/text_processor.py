
def process_text(text, *check_spelling):
    result = [word if check(word) else f"[{word}]" for word, check in zip(text.split(), check_spelling)]
    return " ".join(result)
