import unittest
from text_processor import process_file

class Tests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_empty_string_returns_empty_string(self):
<<<<<<< Updated upstream
        text_processor = TextProcessor()
        text = ""
        actual_ouput = text_processor.process_file(text)

        self.assertEqual(text, actual_ouput)

    def test_hello_returns_hello(self):
        text_processor = TextProcessor()
        text = "hello"
        actual_ouput = text_processor.process_file(text)

        self.assertEqual(text, actual_ouput)
        
=======
       actual_output = process_file("")
       self.assertEqual("", actual_output)

    def test_hello_returns_hello(self):
        actual_output = process_file("hello")
        self.assertEqual("hello", actual_output)
       
>>>>>>> Stashed changes

if __name__ == '__main__': 
  unittest.main()