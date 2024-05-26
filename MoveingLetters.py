# Nithiya
# 08/04/24
# Move first letter to last
from holoviews import output


def is_vowel(char):
    """
    Checks if a character is a vowel.
    :param char: Character to check
    :return: True if vowel, False otherwise
    """
    return char in 'AEIOUaeiou'


def convert_to_pig_latin(word):
    """
    Converts a word to Pig Latin.
    :param word: Word to convert
    :return: Pig Latin version of the word
    """
    if is_vowel(word[0]):
        return word + 'way'
    else:
        # List of common consonant clusters
        clusters = ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr',
                    'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw',
                    'th', 'tr', 'tw', 'wh', 'wr']
        if len(word) > 1 and word[:2] in clusters:
            return word[2:] + word[:2] + 'ay'
        else:
            return word[1:] + word[0] + 'ay'


def read_file(file_path):
    """
    Reads content from a text file.
    :param file_path: Path to the file
    :return: Content of the file as a string
    """
    with open(file_path, 'r') as file:
        data = file.read()
    return data


def write_file(file_path, data):
    """
    Writes content to a text file.
    :param file_path: Path to the file
    :param data: Content to write
    """
    with open(file_path, 'w') as file:
        file.write(data)


def main(input_file: object, output_file: object) -> object:
    """
    Main function to convert words from an input file to Pig Latin
    and write the results to an output file.
    :param input_file: Path to the input file
    :param output_file: Path to the output file
    """
    data = read_file(input_file)
    words = data.split()

    pig_latin_words = []
    for word in words:
        pig_latin_word = convert_to_pig_latin(word)
        pig_latin_words.append(pig_latin_word)

    pig_latin_text = ' '.join(pig_latin_words)
    write_file(output_file, pig_latin_text)


if __name__ == '__NithiyaProjectFiles__':
    input_file_path = 'input.txt.txt'
    output_file_path = 'output.txt.txt'
    main(input.txt.txt,output.txt.txt)
