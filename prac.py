from collections import Counter

def file_stats_and_ops(filename):
    # Read the file
    with open(filename, 'r') as f:
        lines = f.readlines()
        text = ''.join(lines)
        words = text.split()

    # a. Print count of characters, words, and lines
    num_chars = len(text)
    num_words = len(words)
    num_lines = len(lines)
    print(f"Total characters: {num_chars}")
    print(f"Total words: {num_words}")
    print(f"Total lines: {num_lines}")

    # b. Frequency of each character
    char_freq = Counter(text)
    print("Character frequencies:", dict(char_freq))

    # c. Print words in reverse order
    reversed_words = words[::-1]
    print("Words in reverse order:", reversed_words)

    # d. Copy even and odd lines to File1 and File2
    with open('File1', 'w') as f1, open('File2', 'w') as f2:
        for i, line in enumerate(lines):
            if (i + 1) % 2 == 0:
                f1.write(line)
            else:
                f2.write(line)

# Usage:
file_stats_and_ops('sample.txt')
