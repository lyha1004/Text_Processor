import requests
SPACE = ' '
LINEBREAK = """
"""

def process_word(word, check_spelling):
   try:
      if check_spelling(word):
         return word
   except Exception:
     return f"?{word}?"
   else: 
      return f"[{word}]"
   
def process_line(line, check_spelling):
   return SPACE.join([process_word(word, check_spelling) for word in line.split()])

def process_text(text, check_spelling): 
   return LINEBREAK.join([process_line(line, check_spelling) for line in text.splitlines()])

def getResponse(word):
   url = f'http://agilec.cs.uh.edu/spell?check={word}'
   response = requests.get(url)
   return response

def parseText(getResponse):
   if getResponse == True:
      return True
   elif getResponse == False:
      return False

def check_spelling(word):
   response = getResponse(word)
   parsed_response = parseText(response)
   return parsed_response
