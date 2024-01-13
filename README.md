# TXT-Compression

This Python script will use Huffman Coding to compress files. It also provides functionality to decompress .bin files assuming they are compressed with this program. The script includes methods to build a Huffman Tree based on the frequency of characters in a text, encode the text using Huffman Codes, and compress the data into a binary file.

## Usage

    python3 huffman_compression.py <file_name> <c/d>

- `<file_name>`: The name of the input file
  - Use a .txt file for compression
  - Use a .bin file for decompression
- `<c/d>`: Use "c" for compression, "d" for decompression

### Compression Example

    python3 huffman_compression.py input.txt c

This command compresses the "input.txt" file and generates a binary compressed file named "input_compressed.bin".

### Decompression Example

    python3 huffman_compression.py input.bin d

This command decompresses the "input.bin" file and generates a text decompressed file named "input_decompressed.txt".

## Huffman Code Storage

The Huffman Codes are stored at the beginning of the binary compressed file during compression using the `pickle` module. The compressed file format includes the Huffman Codes as a dictionary, a separator byte (`0x00`), 4 bytes containing the length of the encoded text, and the encoded text itself.