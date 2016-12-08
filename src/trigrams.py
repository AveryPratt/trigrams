"""Trigrams."""


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
    keys = dct.keys()
    key = keys  # <-----------KEY IS ASSIGNED BUT NEVER USED


def assemble(first, second, num, dct, text=""):
    """Docstring."""
    import random
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
