# ccwc

`ccwc` is a simple command-line utility that counts bytes, lines, words, or characters in a file. It is similar to the Unix `wc` command.

## Usage

```sh
ccwc [options] [FILE]

Options:
    -c        Count bytes in the file.
    -l        Count lines in the file.
    -w        Count words in the file.
    -m        Count characters in the file.
    -h --help Show this screen.
```


## Development
### Prerequisites
+ Python 3.x
+ docopt library

Install the docopt library:
`pip install docopt`

Running the Script

You can run the script directly from the command line:

```sh
$ ./ccwc.py -l test.txt
```

```
7145 test.txt
```

### Testing
The tests are written using the unittest framework and subprocess module. The test file is test_ccwc.py.

To run the tests, use the following command:
`pytest`

## License
This project is licensed under the MIT License.