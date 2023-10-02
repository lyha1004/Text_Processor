import requests

def process_file(text):
    url = f'http://agilec.cs.uh.edu/spell?check={text}'
    response = requests.get(url)
    return f'[{text}]'if response.text == 'false' else text


