
def process_text(text, *check_spelling):
    result = []
    words = text.split()
    for word, check_spelling in zip(words, check_spelling):
        if check_spelling(word):
            result.append(word)
        else:
            result.append(f"[{word}]")
    return " ".join(result)

