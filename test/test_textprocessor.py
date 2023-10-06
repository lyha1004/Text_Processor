import unittest
from unittest.mock import patch
from src.text_processor import process_file
from src.text_processor import is_valid_word

class Tests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_empty_string_returns_empty_string(self):
       actual_output = process_file("", is_valid_word)
       self.assertEqual("", actual_output)

    def test_hello_returns_hello(self):
        actual_output = process_file("hello", is_valid_word)
        self.assertEqual("hello", actual_output)
  
    def test_incorrect_spelling_returns_brackets(self):
        with patch('text_processor.is_valid_word') as mock_is_valid_word:
            mock_is_valid_word.side_effect = lambda text: False if text == "blah" else True
            actual_output = process_file("blah", is_valid_word)
            self.assertEqual("[blah]", actual_output)


if __name__ == '__main__': 
  unittest.main()
       