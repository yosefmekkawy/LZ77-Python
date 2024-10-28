def lz77_compress_string(data, window_size=10):
    i = 0
    compressed_data = []

    while i < len(data):
        match = (0, 0, data[i])

        for j in range(max(0, i - window_size), i):  # searching for the longest match
            length = 0
            while (i + length < len(data) and
                   data[j + length] == data[i + length] and
                   length < window_size):
                length += 1

            if length > match[1]:
                match = (i - j, length, data[i + length] if i + length < len(data) else '')

        compressed_data.append(match)
        i += match[1] + 1

    return compressed_data
