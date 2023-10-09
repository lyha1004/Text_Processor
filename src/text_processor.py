SPACE = " "

def process_word(word, check_spelling):
 return word if check_spelling(word) else f"[{word}]"

def process_text(text, check_spelling):
    return SPACE.join([process_word(word, check_spelling) if word != '\n' else word for word in text.split(SPACE)])
