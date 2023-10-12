import requests

def get_Response(word):
   url = f'http://agilec.cs.uh.edu/spell?check={word}'
   response = requests.get(url)
   return response

def parse_Text(response):
   if response == 'true':
      return True
   elif response == 'false':
      return False

def check_spelling(word):
   response = get_Response(word)
   parsed_response = parse_Text(response)
   return parsed_response
