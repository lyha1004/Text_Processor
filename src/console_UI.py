#prompt user for file name +
#take name of file as input +
#read text from file +
#print spellchecked text to console +
#provide task to run from build
from text_processor import process_text
from spell_checker import check_spelling
import sys

def read_file(file_name):
    with open(f"src/input_files/{file_name}", "r") as file: 
        text = file.read()
        return text

if __name__ == "__main__":
    file_name = input("Enter file name:\n")
    
    # if len(sys.argv) != 2:
    #     print("Usage: python your_program.py <file_name>")
    #     sys.exit(1)

    # file_name = sys.argv[1]
    text = read_file(file_name)
    print(process_text(text, check_spelling))


    