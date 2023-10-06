import unittest
from unittest.mock import patch
from src.text_processor import process_text
from src.spell_checker import check_spelling

class Tests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_empty_string_returns_empty_string(self):
       actual_output = process_text("", check_spelling)
       self.assertEqual("", actual_output)

    def test_hello_returns_hello(self):
        actual_output = process_text("hello", check_spelling)
        self.assertEqual("hello", actual_output)
  
    @patch('src.spell_checker.check_spelling')
    def test_incorrect_spelling_returns_brackets(self, mock_check_spelling):
        mock_check_spelling.return_value = False
        actual_output = process_text("blah", mock_check_spelling)
        self.assertEqual("[blah]", actual_output)


if __name__ == '__main__': 
  unittest.main()
       