from text_processor import process_text
from spell_checker import check_spelling

def read_file(file_name):
    with open(f"src/input_files/{file_name}", "r") as file: 
        text = file.read()
        return text

if __name__ == "__main__":
    file_name = input("Enter file name:\n")

    text = read_file(file_name)
    print(process_text(text, check_spelling))


    