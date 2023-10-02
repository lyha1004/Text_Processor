import unittest
from text_processor import TextProcessor

class Tests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

def test_empty_string_returns_empty_string(self):
    text_processor = TextProcessor()
    text = ""
    actual_ouput = text_processor.process_file(text)

    self.assertEqual(text, actual_ouput)

def test_hello_returns_hello(self):
    text_processor = TextProcessor()
    text = "hello"
    actual_ouput = text_processor.process_file(text)

    self.assertEqual(text, actual_ouput)
       

if __name__ == '__main__': 
  unittest.main()