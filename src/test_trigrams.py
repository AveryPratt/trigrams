"""Trigrams."""

import pytest

PARSE_TABLE = [
    [
        "Howdily doodily, neighborooski. My name is Ned Flanders.",
        ["Howdily", "doodily,", "neighborooski.", "My", "name", "is", "Ned", "Flanders.", ],
    ],
    [
        "Toodle dooski!",
        ["Toodle", "dooski!", ],
    ],
    [
        "The quick brown fox jumped over the lazy ass dogs.",
        ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "ass", "dogs.", ],
    ],
]


CREATE_KVP = [
    [
        ["Howdily", "doodily,", "neighborooski.", "My", "name", "is", "Ned", "Flanders.", ],
        {
            "Howdily_doodily,": ["neighborooski."],
            "doodily,_neighborooski.": ["My"],
            "neighborooski._My": ["name"],
            "My_name": ["is"],
            "name_is": ["Ned"],
            "is_Ned": ["Flanders."],
        },
    ],
    [
        ["Toodle", "dooski!", ],
        {},
    ],
    [
        ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "ass", "dogs.", ],
        {
            "The_quick": ["brown"],
            "quick_brown": ["fox"],
            "brown_fox": ["jumped"],
            "fox_jumped": ["over"],
            "jumped_over": ["the"],
            "over_the": ["lazy"],
            "the_lazy": ["ass"],
            "lazy_ass": ["dogs."],
        },
    ],
]


ASSEMBLE_TABLE = [
    ["first", "second", 1, {"first_second": ["third"]}, "", "third", ],
    ["first", "second", 0, {"first_second": ["third"]}, "", "", ],
    ["first", "second", 0, {"first_second": ["third"]}, "random jibberish ", "random jibberish", ],
    ["first", "second", 3, {"first_second": ["third"]}, "random jibberish ", "random jibberish third third third", ],
]


ASSEMBLE_TABLE_RANDOM = [
    ["first", "second", 3, {
        "The_quick": ["brown", "quick", "lazy"],
        "quick_brown": ["fox", "ass"],
        "brown_fox": ["jumped", "the", "lazy", "fox"],
        "fox_jumped": ["over", "The", "the"],
        "first_second": ["The", "dogs."],
        "second_the": ["quick", "brown", "lazy"],
        "jumped_over": ["the"],
        "over_the": ["lazy", "over"],
        "the_lazy": ["ass", "jumped"],
        "lazy_ass": ["dogs.", "The", "lazy", "ass"],
    },
        "", ],
    ["first", "second", 80, {
        "The_quick": ["brown", "quick", "lazy"],
        "quick_brown": ["fox", "ass"],
        "brown_fox": ["jumped", "the", "lazy", "fox"],
        "fox_jumped": ["over", "The", "the"],
        "jumped_over": ["the"],
        "over_the": ["lazy", "over"],
        "the_lazy": ["ass", "jumped"],
        "lazy_ass": ["dogs.", "The", "lazy", "ass"],
    },
        "random jibberish ", ],
]

SIMPLE_INPUT_FILES = [
    [
        "./test_story1",
        "sad. ",
    ],
]

COMPLEX_INPUT_FILES = [
    [
        "./test_story2",
        "One night--it was on the twentieth of March, 1888--I was returning from a journey to a patient (for I had now returned to civil practice), when my way led me through Baker Street. As I passed the well-remembered door, which must always be associated in my mind with my wooing, and with the dark incidents of the Study in Scarlet, I was seized with a keen desire to see Holmes again, and to know how he was employing his extraordinary powers. His rooms were brilliantly lit, and, even as I looked up, I saw his tall, spare figure pass twice in a dark silhouette against the blind. He was pacing the room swiftly, eagerly, with his head sunk upon his chest and his hands clasped behind him. To me, who knew his every mood and habit, his attitude and manner told their own story. He was at work again. He had risen out of his drug-created dreams and was hot upon the scent of some new problem. I rang the bell and was shown up to the chamber which had formerly been in part my own."
    ]
]


@pytest.mark.parametrize("text, result", PARSE_TABLE)
def test_parse(text, result):
    """Test parse function to return a list of words from text."""
    from trigrams import parse
    assert parse(text) == result


@pytest.mark.parametrize("result, dct", CREATE_KVP)
def test_create_kvp(result, dct):
    """Test create_kvp function to return a trigram dictionary from list of words."""
    from trigrams import create_kvp
    assert create_kvp(result) == dct


@pytest.mark.parametrize("first, second, num, dct, text, result", ASSEMBLE_TABLE)
def test_assemble(first, second, num, dct, text, result):
    """Test assemble function to recursively generate random words from dictionary."""
    from trigrams import assemble
    assert assemble(first, second, num, dct, text) == result


@pytest.mark.parametrize("first, second, num, dct, text", ASSEMBLE_TABLE_RANDOM)
def test_assemble_random(first, second, num, dct, text):
    """Test assemble function to recursively generate random words from dictionary."""
    from trigrams import assemble
    result = assemble(first, second, num, dct, text)
    all_values = []
    for key in dct:
        all_values.extend(dct[key])
    all_values.extend(text.split())
    assert set(result.split()).issubset(set(all_values))


@pytest.mark.parametrize("input_file, result", SIMPLE_INPUT_FILES)
def test_read_story(input_file, result):
    """Test read_story function with simple files to create a specific new story using trigrams."""
    import trigrams
    output = trigrams.read_story(input_file)
    match = trigrams.assemble("", "", 200, (trigrams.create_kvp(trigrams.parse(result * 200))))
    assert output == match


@pytest.mark.parametrize("input_file, result", COMPLEX_INPUT_FILES)
def test_read_story2(input_file, result):
    """Test read_story function with complex files to create a new story of the same style using trigrams."""
    from trigrams import read_story
    output = read_story(input_file).split()
    match = result.split()
    assert set(list(output)).issubset(set(list(match)))
