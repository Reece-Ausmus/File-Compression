import sys
import pickle
from TreeNode import TreeNode
from Heap import Heap
 
def build_frequency_table(data):
    """This method creates a frequency table for the data"""
    frequency_table = {}
    for byte in data:
        if byte in frequency_table:
            frequency_table[byte] += 1
        else:
            frequency_table[byte] = 1
    return frequency_table

def build_huffman_tree(frequency_table):
    """This method builds a tree out of TreeNode objects based on the frequency_table"""
    min_heap = Heap([TreeNode(byte, frequency) for byte, frequency in frequency_table.items()])
    min_heap.heapify()

    while len(min_heap) > 1:
        left = min_heap.pop()
        right = min_heap.pop()
        merged = TreeNode(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        min_heap.push(merged)

    return min_heap.nodes[0]

def build_huffman_codes(node, current_code="", huffman_codes=None):
    """This method creates a dictionary of huffman_codes based on the Huffman Tree"""
    if huffman_codes is None:
        huffman_codes = {}

    if node:
        if node.byte is not None:
            huffman_codes[node.byte] = current_code
        build_huffman_codes(node.left, current_code + "0", huffman_codes)
        build_huffman_codes(node.right, current_code + "1", huffman_codes)
    
    return huffman_codes

def encode_text(data, huffman_codes):
    """This method encodes the text according to the huffman_codes"""
    encoded_text = ""
    for byte in data:
        encoded_text += huffman_codes[byte]
    return encoded_text

def compress(input_file, output_file, file_type):
    """This method reads the data from the input_file, uses helper methods to obtain the encoded text, and writes it to the output_file"""
    with open(input_file, "rb") as file:
        binary_data = file.read()
    
    frequency_table = build_frequency_table(binary_data)
    huffman_tree = build_huffman_tree(frequency_table)
    huffman_codes = build_huffman_codes(huffman_tree)

    encoded_text = encode_text(binary_data, huffman_codes)

    with open(output_file, "wb") as file:
        pickle.dump(huffman_tree, file)

        file.write(b"\0")

        file_type_binary = file_type.encode()
        file_type_string = ''.join(format(byte, '08b') for byte in file_type_binary)
        file.write(len(file_type_string).to_bytes(4, byteorder='big'))
        file.write(int(file_type_string, 2).to_bytes((len(file_type_string) + 7) // 8, byteorder='big'))
        
        file.write(len(encoded_text).to_bytes(4, byteorder='big'))
        file.write(int(encoded_text, 2).to_bytes((len(encoded_text) + 7) // 8, byteorder='big'))

def decode_text(encoded_text, huffman_tree, output_file):
    """This method decodes the text according to the huffman_tree"""
    bit_counter = 0
    current_node = huffman_tree

    with open(output_file, 'wb') as file:
        for bit in encoded_text:
            if bit == '0':
                current_node = current_node.left
                bit_counter += 1

            elif bit == '1':
                current_node = current_node.right
                bit_counter += 1

            if current_node.byte is not None:
                file.write(current_node.byte.to_bytes(bit_counter, byteorder='big'))
                bit_counter = 0
                current_node = huffman_tree

def decompress(input_file):
    """This method reads the data from the input_file, uses helper methods to obtain the decoded text, and writes it to the output_file"""
    with open(input_file, "rb") as file:
        huffman_tree = pickle.load(file)

        separator = file.read(1)
        if separator != b"\0":
            raise ValueError("Invalid compressed file format")
        
        file_type_length = int.from_bytes(file.read(4), byteorder='big')    
        file_type_data = bin(int.from_bytes(file.read((file_type_length + 7) // 8), byteorder='big'))[2:]

        encoded_text_length = int.from_bytes(file.read(4), byteorder='big') 
        encoded_data = bin(int.from_bytes(file.read((encoded_text_length + 7) // 8), byteorder='big'))[2:]

    file_type = file_type_data.zfill(file_type_length)
    file_type_binary = int(file_type, 2).to_bytes((len(file_type) + 7) // 8, byteorder='big')
    file_type_text = file_type_binary.decode('utf-8')
    
    encoded_text = encoded_data.zfill(encoded_text_length)
    output_file = input_file.replace(".bin", "_decompressed." + file_type_text)
    decode_text(encoded_text, huffman_tree, output_file)


if __name__ == "__main__":
    """Provides error handling for usage of script and calls appropriate method if no errors"""
    if (len(sys.argv) != 3) or not \
        ((sys.argv[1].endswith(".txt") or sys.argv[1].endswith(".bin")) or sys.argv[1].endswith(".html")) or \
            (sys.argv[2] != "c" and sys.argv[2] != "d"):
        print("Usage: python huffman_compression.py <file_name> <c/d>")
    elif sys.argv[2] == "c":
        input_file = sys.argv[1]
        if sys.argv[1].endswith(".txt"):
            compressed_file = input_file.replace(".txt", "_compressed.bin")
            file_type = "txt"
        elif sys.argv[1].endswith(".html"):
            compressed_file = input_file.replace(".html", "_compressed.bin")
            file_type = "html"
        compress(input_file, compressed_file, file_type)
    elif sys.argv[2] == "d":
        input_file = sys.argv[1]
        decompress(input_file)