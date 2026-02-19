#!/usr/bin/env python3
import sys
#PR rule test2 - Simulate a review comment
#PR rule test3
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = 0
            word_count = 0
            char_count = 0
            for line in file:
                line_count += 1
                word_count += len(line.split())
                char_count += len(line)
        print(f"Number of lines in '{filename}': {line_count}")
        print(f"Number of words in '{filename}': {word_count}")
        print(f"Number of characters in '{filename}': {char_count}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_lines.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    count_lines(filename)
