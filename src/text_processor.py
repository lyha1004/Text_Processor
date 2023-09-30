import os

class TextProcessor:
    
    def process_file(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError("File not found")
        
        with open(file_path, 'r') as file:
            file_contents = file.read()

        return file_contents