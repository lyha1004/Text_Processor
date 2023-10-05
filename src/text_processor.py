class Text_Processor:
    def __init__(self):
        self.valid_word = True

    def set_valid_word(self, valid_word):
        self.valid_word = valid_word
    
    def process_file(self,text):
        return text if self.valid_word else f"[{text}]"


