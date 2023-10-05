import unittest
from src.text_processor import Text_Processor

class Tests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_empty_string_returns_empty_string(self):
       text = Text_Processor()
       actual_output = text.process_file("")
       self.assertEqual("", actual_output)

    def test_hello_returns_hello(self):
        text = Text_Processor()
        actual_output = text.process_file("hello")
        self.assertEqual("hello", actual_output)
       
    def test_incorrect_spelling_returns_brackets(self):
        text = Text_Processor()
        text.set_valid_word(False)
        actual_output = text.process_file("blah")
        self.assertEqual("[blah]", actual_output)


if __name__ == '__main__': 
  unittest.main()
       