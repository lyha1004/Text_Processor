import unittest
from text_processor import process_file
from text_processor import is_valid_word

class Tests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_empty_string_returns_empty_string(self):
       valid = is_valid_word(True)
       actual_output = process_file("", valid)
       self.assertEqual("", actual_output)

    def test_hello_returns_hello(self):
        valid = is_valid_word(True)
        actual_output = process_file("hello", valid)
        self.assertEqual("hello", actual_output)
       
    def test_incorrect_spelling_returns_brackets(self):
        valid = is_valid_word(False)
        actual_output = process_file("blah", valid)
        self.assertEqual("[blah]", actual_output)


if __name__ == '__main__': 
  unittest.main()
       