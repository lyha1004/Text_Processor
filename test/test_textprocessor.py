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

    def test_hello_there_returns_hello_there(self):
        check_spelling1 = Mock(return_value=True)
        check_spelling2 = Mock(return_value=True)
        
        self.assertEqual("hello there", process_text("hello there", check_spelling1, check_spelling2))

    def test_hello_tyop_returns_hello_with_bracket_tyop(self):
        check_spelling1 = Mock(return_value=True)
        check_spelling2 = Mock(return_value=False)
        
        self.assertEqual("hello [tyop]", process_text("hello tyop", check_spelling1,check_spelling2))

    
    def test_misp_hello_returns_bracket_misp_hello(self):
        check_spelling1 = Mock(return_value=False)
        check_spelling2 = Mock(return_value=True)
        
        self.assertEqual("[misp] hello", process_text("misp hello", check_spelling1,check_spelling2))


if __name__ == '__main__': 
  unittest.main()
       