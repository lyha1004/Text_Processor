SPACE = ' '
LINEBREAK = """
"""

def process_word(word, check_spelling):
 return word if check_spelling(word) else f"[{word}]"

def process_line(line, check_spelling):
   return SPACE.join([process_word(word, check_spelling) for word in line.split()])

def process_text(text, check_spelling): 
   return LINEBREAK.join([process_line(line, check_spelling) for line in text.splitlines()])

