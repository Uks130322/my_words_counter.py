import sys
from argparse import ArgumentParser


def clean(file: str) -> None:
    """
    :param file: file with some text
    :return: None
    create new file "cleaned_text.txt" in root directory with cleaned text, without punctuation marks
    and in low register; each word on the new line
    If file does not exist, print your own text
    """
    try:
        with open(file) as file:
            text = file.readlines()
    except FileNotFoundError:
        print('This file does not exist. Print your text; push Enter and Ctrl+D to stop')
        text = sys.stdin.read()

    with open("cleaned_text.txt", 'w') as cleaned_text:
        for line in text:
            if line.isspace():
                continue
            cleared_line = line.lower()
            table = line.maketrans(',.?:;!"()[]', "           ")
            cleared_line = cleared_line.translate(table)
            cleared_line = cleared_line.split()
            cleared_line = "\n".join(cleared_line)
            cleaned_text.write(cleared_line + "\n")


def word_counter(file: str) -> dict:
    """
    :param file: file with some text
    :return: dict[str: int] with number of lines, words and chars in file; length of the longest line
    punctuation marks and special symbols do not count as a word
    If file does not exist, print your own text
    """
    import string

    try:
        with open(file) as file:
            text = file.read().split('\n')
    except FileNotFoundError:
        print('This file does not exist. Print your text; push Enter and Ctrl+D to stop')
        text = sys.stdin.readlines()

    line_count = len(text)
    word_count = 0

    for line in text:
        line = line.split()
        line = [item for item in line if item not in string.punctuation]
        word_count += len(line)

    char_count = sum([len(line) for line in text])
    try:
        max_length = max([len(line) for line in text])
    except ValueError:
        max_length = 0

    return {'lines:': line_count, 'words:': word_count, 'chars:': char_count, 'longest line:': max_length}


def bytes_counter(file: str) -> int:
    """
    :param file: file with some text
    :return: number of bytes in file
    """
    try:
        with open(file) as file:
            return len(file.read().encode('utf-8'))
    except FileNotFoundError:
        print('This file does not exist. Print your text; push Enter and Ctrl+D to stop')
        return len(sys.stdin.read().encode('utf-8'))


def words_occurrences(file: str) -> dict:
    """
    :param file: file with some text
    :return: dict[str: int] with words and its occurrence
    punctuation marks and special symbols do not count as a word
    If file does not exist, print your own text
    """
    clean(file)

    with open("cleaned_text.txt") as text:
        occurrences = {}
        for word in text:
            word = word.rstrip()
            occurrences[word] = occurrences.get(word, 0) + 1

    return occurrences


def common_words(file: str) -> list:
    """
    :param file: file with some text
    :return: list[str] with commonest words
    punctuation marks and special symbols do not count as a word
    If file does not exist, print your own text
    """
    occurrences = words_occurrences(file)
    try:
        common = max(occurrences.values())
        return [word for word in occurrences.keys() if occurrences[word] == common]
    except ValueError:
        return []


def rare_words(file: str) -> list:
    """
    :param file: file with some text
    :return: list[str] with rarest words
    punctuation marks and special symbols do not count as a word
    If file does not exist, print your own text
    """
    occurrences = words_occurrences(file)
    try:
        rare = min(occurrences.values())
        return [word for word in occurrences.keys() if occurrences[word] == rare]
    except ValueError:
        return []


def main():
    parser = ArgumentParser()
    parser.add_argument('input_file', help='read text from this file')
    parser.add_argument('--clean', action='store_true', default=False, help='create cleaned file "cleaned_text.txt"')
    parser.add_argument('--counter', action='store_true', default=False,
                        help='count lines, words and chars; longest line')
    parser.add_argument('--occurrences', action='store_true', default=False, help='count occurrence of each word')
    parser.add_argument('--common', action='store_true', default=False, help='print commonest words')
    parser.add_argument('--rare', action='store_true', default=False, help='print rarest words')
    parser.add_argument('-l', '--lines', action='store_true', default=False, help='print number of lines')
    parser.add_argument('-w', '--words', action='store_true', default=False, help='print number of words')
    parser.add_argument('-c', '--chars', action='store_true', default=False, help='print number of char')
    parser.add_argument('-b', '--bytes', action='store_true', default=False, help='print number of bytes')
    parser.add_argument('--longest_line', action='store_true', default=False, help='print length of longest line')

    args = parser.parse_args()

    if 'True' not in str(args):
        print('\ncleaned file created', '\n\n', word_counter(args.input_file),
              '\n\nbytes: ', bytes_counter(args.input_file),
              '\n\nwords occurrences: ', words_occurrences(args.input_file),
              '\n\ncommonest words: ', common_words(args.input_file),
              '\n\nrarest words: ', rare_words(args.input_file))
    if args.clean:
        clean(args.input_file)
        print('cleaned file created')
    if args.counter:
        print('\n', word_counter(args.input_file))
    if args.occurrences:
        print('\nwords occurrences: ', words_occurrences(args.input_file))
    if args.common:
        print('\ncommonest words: ', common_words(args.input_file))
    if args.rare:
        print('\nrarest words: ', rare_words(args.input_file))
    if args.lines:
        print('\nnumber of lines: ', word_counter(args.input_file)['lines:'])
    if args.words:
        print('\nnumber of words: ', word_counter(args.input_file)['words:'])
    if args.chars:
        print('\nnumber of chars: ', word_counter(args.input_file)['chars:'])
    if args.bytes:
        print('\nnumber of bytes: ', bytes_counter(args.input_file))
    if args.longest_line:
        print('\nlongest line: ', word_counter(args.input_file)['longest line:'], ' chars')


if __name__ == '__main__':
    main()
else:
    print('my_word_counter loaded as a module')
