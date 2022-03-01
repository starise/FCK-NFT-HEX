# Darn simple script to convert Hex strings to Binary strings
# Verify if a string is 100% true to the FCKNFT original code
# Written in 2022 by Andrea Brandi

import sys

BASE_VALUE = 16
INPUT_CODE = sys.argv[1:]
FCKNFT_CODE = [
    "0,0,0,0,1,0,1,1,0,1,0,1,0,0,0,0,",
    "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,",
    "0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,0,",
    "1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,",
    "0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,",
    "1,0,1,0,0,0,1,0,0,0,1,0,1,0,0,1,",
    "0,0,1,0,0,0,1,1,1,0,1,0,0,1,0,0,",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,",
    "1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,",
    "0,0,1,0,0,1,0,1,1,1,0,1,1,1,0,0,",
    "1,0,1,1,0,1,0,1,0,0,0,0,1,0,0,1,",
    "1,0,1,0,1,1,0,1,1,1,0,0,1,0,0,0,",
    "0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,",
    "0,0,1,0,0,1,0,1,0,0,0,0,1,0,0,0,",
    "0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,",
    "0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0."
]

def convert_hex_to_bin(hex_value):
    return bin(int(hex_value, BASE_VALUE))[2:].zfill(BASE_VALUE)

def sanitize_list(raw_list):
    clean_list = []
    for line in range(len(raw_list)):
        element = raw_list[line].replace(",", "").replace(".", "")
        clean_list.append(element)
    return clean_list

def main():
    # Remove noise: strip commas and dots from original code
    fcknft_clean_matrix = sanitize_list(FCKNFT_CODE)
    
    # Convert hex strings and generate a list of binary strings
    input_bin_matrix = []
    for hex_value in INPUT_CODE:
        element = convert_hex_to_bin(hex_value)
        input_bin_matrix.append(element)

    # Check if the converted list match the original code
    if (input_bin_matrix == fcknft_clean_matrix):
        print("CHECK PASSED: \t Match FCK NFT code: ")
        for line in FCKNFT_CODE: print(line)
    else:
        print("CHECK FAILED: \t Does not match FCK NFT code. Try again.")

if __name__ == "__main__":
    main()
