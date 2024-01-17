import unittest
import os
from huffman_compression import compress, decompress
from unittest.mock import patch
import io

class TestHuffmanCompression(unittest.TestCase):

    def test_compress_and_decompress(self):
        input_file = 'Test_Files/html_example.html'
        compressed_file = 'Test_Files/html_example_output.bin'
        decompressed_file = 'Test_Files/html_example_decompressed.html'

        # Suppress print statements in compress and decompress methods
        with patch('sys.stdout', new_callable=io.StringIO):
            # Compress the file
            compress(input_file, compressed_file)

            # Decompress the file
            decompress(compressed_file, decompressed_file)

        # Check if the decompressed file content is the same as the original input
        with open(decompressed_file, 'rb') as file:
            decompressed_data = file.read()

        with open(input_file, 'rb') as file:
            original_data = file.read()

        self.assertEqual(decompressed_data, original_data)
        self.assertTrue(os.path.getsize(compressed_file) <= os.path.getsize(input_file))

        # Clean up test files
        os.remove(compressed_file)
        os.remove(decompressed_file)

if __name__ == '__main__':
    unittest.main()