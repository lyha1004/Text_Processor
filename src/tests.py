import unittest
from unittest.mock import Mock
from textwrap import dedent
from text_processor import process_text, parseText, check_spelling, getResponse

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
        check_spelling = Mock(side_effect = lambda word: word not in['tyop', 'misp'] )
        
        self.assertEqual("hello [tyop] there [misp]", process_text("hello tyop there misp", check_spelling))

    def test_two_lines_returns_two_lines(self):
        text = dedent("""\
            line one
            line two""")
        check_spelling = Mock(return_value = True)

        self.assertEqual(text, process_text(text, check_spelling))

    def test_two_lines_with_incorrect_spelling_returns_two_lines_with_brackets(self):
        text = dedent("""\
            cool ctas
            ctue dogs""")

        expected_result = dedent("""\
                                cool [ctas]
                                [ctue] dogs""")

        check_spelling = Mock(side_effect = lambda word: word not in ['ctas', 'ctue'])

        self.assertEqual(expected_result, process_text(text, check_spelling))

    def test_three_lines_returns_three_lines(self):
        text = dedent("""\
            line one
            line two
            line three""")

        check_spelling = Mock(return_value = True)

        self.assertEqual(text, process_text(text, check_spelling))

    def test_three_lines_with_incorrect_spelling_returns_correct_results(self):
        text = dedent("""\
            cool ctas
            ctue dogs
            crazy horzes""")

        expected_result = dedent("""\
                         cool [ctas]
                         [ctue] dogs
                         crazy [horzes]""")
        
        check_spelling = Mock(side_effect = lambda word: word not in ['ctas', 'ctue', 'horzes'])
        
        self.assertEqual(expected_result, process_text(text, check_spelling))
        
    def test_processtext_exception_from_spellchecker(self):
        text = "hello there how aare you"

        def side_effect_function(word):
            if word == 'there':
                raise Exception
            
            return True
        
        check_spelling = Mock(side_effect = side_effect_function)
        
        self.assertEqual("hello ?there? how aare you", process_text(text, check_spelling))

    def test_hello_hwo_aare_you_returns_exception_and_wrong_spelling(self):
        text = "hello there hwo aare you"

        def side_effect_function(word):
            if word == 'there' or word == 'aare':
                raise Exception 
            
            return word not in ["hwo"]
        
        check_spelling = Mock(side_effect = side_effect_function)
        
        self.assertEqual("hello ?there? [hwo] ?aare? you", process_text(text, check_spelling))
    
    def test_getResponse_takes_word_returns_response_from_webservice(self):
        word = "hello"

        self.assertEqual(getResponse(word).status_code, 200)
         

    def test_parseText_takes_True_returns_True(self):
       self.assertEqual(True, parseText(True))
       

    def test_parseText_takes_False_returns_False(self):
       self.assertEqual(False, parseText(False))

    def test_spell_check_to_getResponse_to_parseText_returns_response(self):
       pass

    def test_spall_check_throws_Exception_when_getResponse_throws_Exception(self):
        pass



        
if __name__ == '__main__': 
  unittest.main()