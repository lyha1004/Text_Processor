import unittest
from unittest.mock import Mock
from src.text_processor import process_text


class Tests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_empty_string_returns_empty_string(self):
       check_spelling = Mock(return_value=True)

       self.assertEqual('', process_text('', check_spelling))

    def test_hello_returns_hello(self):
        check_spelling = Mock(return_value=True)

        self.assertEqual('hello', process_text('hello', check_spelling))
  
    def test_incorrect_spelling_returns_brackets(self):
        check_spelling = Mock(return_value=False)
        
        self.assertEqual("[blah]", process_text('blah', check_spelling))


if __name__ == '__main__': 
  unittest.main()
       