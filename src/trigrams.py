"""Trigrams."""

import io
import random


def parse(text):
    """Turns text into a list of words."""
    return text.split()


def create_kvp(text_list):
    """Turns text_list into a dictionary of key value pairs in which every two consecutive words is a key for the value of the following word."""
    dct = {}
    for idx in range(len(text_list) - 2):
        key = text_list[idx] + "_" + text_list[idx + 1]
        if key not in dct.keys():
            dct[key] = [text_list[idx + 2]]
        else:
            dct[key].append(text_list[idx + 2])
    return dct


def assemble(first, second, num, dct, text=""):
    """Recursively creates a new story that is num words long by adding a word to text associated with the key created by first and second."""
    if num <= 0:
        return text[:-1]
    key = first + "_" + second
    if key in dct:
        vals = dct[key]
    else:
        rand_key = random.choice(list(dct.keys()))
        vals = dct[rand_key]
    rand_val = random.choice(vals)
    text += rand_val + " "
    return assemble(second, rand_val, num - 1, dct, text)


def read_story(input_file):
    """converts an input file into a text string and calls the other functions in trigrams to create a new 200 word story in the same style as the original."""
    file = io.open(input_file)
    file_text = file.read()
    file.close()
    clean_file_text = file_text.replace("\n", " ").replace("\r", "")
    parsed_file_text = parse(clean_file_text)
    dct = create_kvp(parsed_file_text)
    story = assemble("", "", 200, dct)
    return story


if __name__ == "__main__":
	import sys
	print(read_story(sys.argv[1]))