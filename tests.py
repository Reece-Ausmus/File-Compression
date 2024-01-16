import unittest
import os
from huffman_compression import compress, decompress

class TestHuffmanCompression(unittest.TestCase):

    def test_compress_and_decompress(self):
        input_file = 'Test_Files/txt_example.txt'
        output_file = 'Test_Files/txt_example_output.bin'

        # Compress the file
        compress(input_file, output_file)

        # Decompress the file
        decompress(output_file, 'Test_Files/txt_example_decompressed.txt')

        # Check if the decompressed file content is the same as the original input
        with open('Test_Files/txt_example_decompressed.txt', 'rb') as file:
            decompressed_data = file.read()

        with open(input_file, 'rb') as file:
            original_data = file.read()

        self.assertEqual(decompressed_data, original_data)

        # Clean up test files
        os.remove(output_file)
        os.remove('Test_Files/txt_example_decompressed.txt')

if __name__ == '__main__':
    unittest.main()