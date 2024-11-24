#!/usr/bin/env python3
"""
ccwc - A simple version of wc that counts bytes, lines, or words in a file.

Usage:
    ccwc <file>
    ccwc -c <file>
    ccwc -l <file>
    ccwc -m <file>
    ccwc -w <file>

Options:
    -c        Count bytes in the file.
    -l        Count lines in the file.
    -w        Count words in the file.
    -h --help Show this screen.
"""

from docopt import docopt
import locale


def count_bytes(file_content):
        return len(file_content)

def count_lines(file_content):
        return file_content.count('\n')

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
        file_path = arguments['<file>']
        
        if arguments['-c']:
            file_content = read_file(file_path, 'rb')
            if file_content is not None:
                    byte_count = count_bytes(file_content)
                    print(f"{byte_count} {file_path}")
        elif arguments['-w']:
            file_content = read_file(file_path, 'r')
            if file_content is not None:
                word_count = count_words(file_content)
                print(f"{word_count} {file_path}")
        elif arguments['-l']:
            file_content = read_file(file_path, 'r')
            if file_content is not None:
                line_count = count_lines(file_content)
                print(f"{line_count} {file_path}")
        elif arguments['-m']:
            file_content = read_file(file_path, 'rb')
            if file_content is not None:
                character_count = count_characters(file_content)
                print(f"{character_count} {file_path}")
        elif arguments['<file>']:
            file_content = read_file(file_path, 'r')
            if file_content is not None:
                line_count = count_lines(file_content)
                word_count = count_words(file_content)
            file_content = read_file(file_path, 'rb')
            if file_content is not None:
                byte_count = count_bytes(file_content)
            print(f"{line_count} {word_count} {byte_count} {file_path}")

if __name__ == '__main__':
    main()