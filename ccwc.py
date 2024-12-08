#!/usr/bin/env python3
"""
ccwc - A simple version of wc that counts bytes, lines, or words in a file.

Usage:
    ccwc [options] [FILE]

Options:
    -c        Count bytes in the file.
    -l        Count lines in the file.
    -w        Count words in the file.
    -m        Count characters in the file.
    -h --help Show this screen.
"""

import sys
from docopt import docopt


def count_bytes(file_content):
    return len(file_content)

def count_lines(file_content):
    return sum(1 for line in file_content.splitlines())

def count_words(file_content):
    return len(file_content.split())

def count_characters(file_content):
    return len(file_content.decode('utf-8'))

def read_file(file_path, mode='rb'):
    try:
        with open(file_path, mode) as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def main():
    arguments = docopt(__doc__)
    file_path = arguments['FILE']
    
    if arguments['-c']:
        if file_path:
            file_content = read_file(file_path, 'rb')
        else:
            file_content = sys.stdin.buffer.read()
        if file_content is not None:
            byte_count = count_bytes(file_content)
            print(f"{byte_count} {file_path or ''}")
    elif arguments['-w']:
        if file_path:
            file_content = read_file(file_path, 'r')
        else:
            file_content = sys.stdin.read()
        if file_content is not None:
            word_count = count_words(file_content)
            print(f"{word_count} {file_path or ''}")
    elif arguments['-l']:
        if file_path:
            file_content = read_file(file_path, 'r')
        else:
            file_content = sys.stdin.read()
        if file_content is not None:
            line_count = count_lines(file_content)
            print(f"{line_count} {file_path or ''}")
    elif arguments['-m']:
        if file_path:
            file_content = read_file(file_path, 'rb')
        else:
            file_content = sys.stdin.buffer.read()
        if file_content is not None:
            char_count = count_characters(file_content)
            print(f"{char_count} {file_path or ''}")
    else:
        if file_path:
            file_content = read_file(file_path, 'rb')
        else:
            file_content = sys.stdin.buffer.read()
        if file_content is not None:
            line_count = count_lines(file_content)
            word_count = count_words(file_content)
            char_count = count_bytes(file_content)
            print(f"{line_count} {word_count} {char_count} {file_path or ''}")

if __name__ == "__main__":
    main()