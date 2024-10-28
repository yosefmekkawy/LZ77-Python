def lz77_compress_string(data, window_size=10):
    i = 0
    compressed_data = []

    while i < len(data):  # Start of the look-ahead window
        match = (0, 0, data[i])  # Default match 

        # Search within the search window for the best match
        for j in range(max(0, i - window_size), i):
            length = 0

            # Find the length of the match
            while (i + length < len(data) and
                   data[j + length] == data[i + length] and
                   length < window_size):
                length += 1

            # If we found a match with the same length but a smaller offset, prioritize it
            if length > match[1] or (length == match[1] and (i - j) < match[0]):
                match = (i - j, length, data[i + length] if i + length < len(data) else '')

        # Add the best match found to the compressed data
        compressed_data.append(match)

        # Move the pointer to the next unmatched position
        i += match[1] + 1

    return compressed_data

def lz77_decompress_string(compressed_data):
    result = []  # Use a list to build the string efficiently (strings are immutable)

    # Loop through each triplet (offset, length, next_char)
    for offset, length, next_char in compressed_data:
        # Extract the matching part from the previously decompressed data
        start_index = len(result) - offset

        # Handle overlaps: copy the matching part progressively
        for i in range(length):
            result.append(result[start_index + i])

        # Append the next character (if it's not an empty string)
        if next_char:
            result.append(next_char)

    # Join the list into a final decompressed string
    return ''.join(result)


def main():
    # Test cases to validate compression and decompression
    test_strings = [
        "ABAABABAABBBBBBBBBBBBA",  # Slides testcase
        "ABABABABAB",             # Repetitive pattern
        "AAAAAA",                 # Single character repeated
        "ABCDE",                  # No repetition
        "AABAABCAABC",            # Partial repetitions
        "",                       # Empty string
        "A",                      # Single character
        "Eslam Sayed Younus"
    ]

    # Test each string and validate the compression and decompression
    for i, test_str in enumerate(test_strings):
        print(f"Test {i + 1}: Input = '{test_str}'")

        # Step 1: Compress the input string
        compressed = lz77_compress_string(test_str)
        print("Compressed Output:", compressed)

        # Step 2: Decompress the compressed data
        decompressed = lz77_decompress_string(compressed)

        # Step 3: Verify if decompressed output matches the original input
        print("Decompressed Output:", decompressed)

        # Step 4: Check if the decompressed string is the same as the original input
        if decompressed == test_str:
            print("Test Passed! 🎉")
        else:
            print("Test Failed! ❌")

        print("-" * 50)


if __name__ == "__main__":
    main()
