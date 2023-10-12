import unittest
from unittest.mock import patch
from src.spell_checker import parse_Text, check_spelling, get_Response


class SpellCheckerTests(unittest.TestCase):
    def test_getResponse_takes_word_returns_response_from_webservice_greater_than_0(self):
        word = "hello"
        response = get_Response(word)
        self.assertTrue(len(response) > 0)
         

    def test_parseText_takes_True_returns_True(self):
  
       self.assertTrue(parse_Text('true'))
       

    def test_parseText_takes_False_returns_False(self):
   
       self.assertFalse(parse_Text('false'))

    @patch('spell_checker.get_Response')
    @patch('spell_checker.parse_Text')
    def test_spell_check_to_getResponse_to_parseText_returns_response(self, mock_parse_Text, mock_get_Response):
       word = "hello"
       mock_get_Response.return_value = 'true'
       mock_parse_Text.return_value = True

       result = check_spelling(word)

       mock_get_Response.assert_called_once_with(word)
       mock_parse_Text.assert_called_once_with(mock_get_Response.return_value)

       self.assertEqual(mock_parse_Text.return_value, result)

    @patch('spell_checker.get_Response' , side_effect = Exception)
    def test_spell_check_throws_Exception_when_getResponse_throws_Exception(self, mock_get_Response):
        word = "hello"
        
        with self.assertRaises(Exception):
            check_spelling(word)

       
if __name__ == '__main__': 
    unittest.main()
