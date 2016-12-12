"""Trigrams."""

import io
import random
import sys


def create_dct(text_list):
    """Turn text_list into a dictionary of key value pairs.

    Every two consecutive words is a key for the value of the following word.
    """
    dct = {}
    for idx in range(len(text_list) - 2):
        key = "_".join([text_list[idx], text_list[idx + 1]])
        dct[key] = dct.setdefault(key, [])
        dct[key].append(text_list[idx + 2])
    return dct


def assemble(dct, num=200, text="", first="", second=""):
    """Recursively creates a new story that is num words long.

    Adding a word to text associated with the key created by first and second.
    """
    if num <= 0:
        return text[:-1]
    key = "_".join([first, second])
    if key in dct:
        vals = dct[key]
    else:
        rand_key = random.choice(list(dct.keys()))
        vals = dct[rand_key]
    rand_val = random.choice(vals)
    return assemble(dct, num - 1, text + rand_val + " ", second, rand_val)


def create_story(input_file=None, words=200):
    """Convert an input file into a text string.

    Calls the other functions in trigrams to create a new 200 word story
    in the same style as the original.
    """
    file_text = read_file(input_file)
    clean_file_text = file_text.replace("\n", " ").replace("\r", "")
    dct = create_dct(clean_file_text.split())
    story = assemble(dct, words)
    return story


def read_file(input_file):
    """Uses io to read a text file and return a string"""
    if not input_file:
        input_file = sys.argv[1]
    with io.open(input_file) as story_file:
        return story_file.read()


# if __name__ == "__main__":
#     print create_story(sys.argv[1], sys.argv[2])
