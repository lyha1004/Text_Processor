import unittest
from text_processor import process_file

class Tests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_empty_string_returns_empty_string(self):
       actual_output = process_file("")
       
       self.assertEqual("", actual_output)

    def test_hello_returns_hello(self):
        actual_output = process_file("hello")
        
        self.assertEqual("hello", actual_output)
       
    def test_incorrect_spelling_returns_brackets(self):
        actual_output = process_file("moln")

        self.assertEqual("[moln]", actual_output)


if __name__ == '__main__': 
  unittest.main()
       