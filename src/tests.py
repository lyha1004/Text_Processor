import unittest
from unittest.mock import Mock
from text_processor import process_text


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
        check_spelling = Mock(side_effect = [True, True])
        
        self.assertEqual("hello there", process_text("hello there", check_spelling))

    def test_hello_tyop_returns_hello_with_bracket_tyop(self):
        check_spelling = Mock(side_effect = [True, False])
        
        self.assertEqual("hello [tyop]", process_text("hello tyop", check_spelling))

    
    def test_misp_hello_returns_bracket_misp_hello(self):
        check_spelling = Mock(side_effect = [False, True])

        self.assertEqual("[misp] hello", process_text("misp hello", check_spelling))

    def test_hello_tyop_there_misp_returns_two_brackets(self):
        check_spelling = Mock(side_effect = [True, False, True, False])
        
        self.assertEqual("hello [tyop] there [misp]", process_text("hello tyop there misp", check_spelling))

    def test_two_lines_returns_two_lines(self):
        check_spelling = Mock(side_effect = [True, True, True, True])
        
        self.assertEqual("line one \n line two", process_text("line one \n line two", check_spelling))

    def test_two_lines_with_incorrect_spellling_returns_two_lines_with_brackets(self):
        check_spelling = Mock(side_effect = [True, False, False, True])
        
        self.assertEqual("cool [ctas] \n [ctue] dogs", process_text("cool ctas \n ctue dogs", check_spelling))


if __name__ == '__main__': 
  unittest.main()
       