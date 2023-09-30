import unittest
from text_processor import TextProcessor

class Tests(unittest.TestCase):
    def test_canary(self):
        self.assertTrue(True)

    def test_read_file_correctly(self):
        print("Running correctly")
        test_file_path = 'test_input.txt'
        with open(test_file_path, 'w') as file:
            file.write("The cow jumped over the moln and the little dog laghed to see such sport and the dih ran away with the spon")
        
        text_processor = TextProcessor()
        actual_output = text_processor.process_file(test_file_path)
        expected_output = "The cow jumped over the moln and the little dog laghed to see such sport and the dih ran away with the spon"

        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__': 
  unittest.main()