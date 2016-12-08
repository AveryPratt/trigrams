"""Trigrams."""

import io
import random


def parse(text):
    """Docstring."""
    return text.split()


def create_kvp(text_list):
    """Docstring."""
    dct = {}
    for idx in range(len(text_list) - 2):
        key = text_list[idx] + "_" + text_list[idx + 1]
        if key not in dct.keys():
            dct[key] = [text_list[idx + 2]]
        else:
            dct[key].append(text_list[idx + 2])
    return dct


def generate_text(dct):
    """Docstring."""
    # import pdb;pdb.set_trace()
    rand_key = random.choice(list(dct.keys()))
    rand_val1 = random.choice(dct[rand_key])

    rand_key = random.choice(list(dct.keys()))
    rand_val2 = random.choice(dct[rand_key])
    return assemble(rand_val1, rand_val2, 200, dct, "")


def assemble(first, second, num, dct, text=""):
    """Docstring."""
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
    """Docstring."""
    file = io.open(input_file)
    file_text = file.read()
    file.close()
    return generate_text(create_kvp(parse(file_text.replace("\n", " ").replace("\r", ""))))
