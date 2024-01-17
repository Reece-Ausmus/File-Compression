# TXT-Compression

This Python script will use Huffman Coding to compress files. It also provides functionality to decompress .bin files assuming they are compressed with this program. The script includes methods to build a Huffman Tree based on the frequency of characters in a text, encode the text using Huffman Codes, and compress the data into a binary file.

## Disclaimer

This script does not guarantee a compressed file that is smaller in size than the original input file. This script utilizes Huffman Coding as the only form of compression. Due to the nature of Huffman Coding, a file is not guaranteed to be smaller once encoded. If the output file would be larger than the input file, no additional output file will be created or written to.

## Usage

    python3 huffman_compression.py <file_name> -c/-d [<output_file>]

- `<file_name>`: The name of the input file
  - Use a .txt file for compression
  - Use a .bin file for decompression
- `-c/-d`: Use "-c" for compression, "-d" for decompression
- `<output_file>`: The name of the output file (optional)

### Compression Example

    python3 huffman_compression.py input.txt c

This command compresses the "input.txt" file and generates a binary compressed file named "input_compressed.bin".

#### With Fourth Argument

    python3 huffman_compression.py input.txt c output.bin

This command compresses the "input.txt" file and writes to a binary compressed file named "output.bin".

### Decompression Example

    python3 huffman_compression.py input.bin d

This command decompresses the "input.bin" file and generates a text decompressed file named "input_decompressed.txt".

#### With Fourth Argument

    python3 huffman_compression.py input.bin d output.txt

This command decompresses the "input.bin" file and writes to a text decompressed file named "output.txt".

## Huffman Code Storage

The Huffman Codes are stored at the beginning of the binary compressed file during compression using the `pickle` module. The compressed file format includes the Huffman Codes as a dictionary, a separator byte (`0x00`), 4 bytes containing the length of the encoded text, and the encoded text itself.