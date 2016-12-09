"""Trigrams."""

import pytest

PARSE_TABLE = [
    [
        "./test_story3", 
        "Howdily doodily, neighborooski. My name is Ned Flanders.",
    ],
    [
        "./test_story4", 
        "Toodle dooski!",
    ],
    [
        "./test_story5", 
        "The quick brown fox jumped over the lazy ass dogs.",
    ],
]


CREATE_DCT = [
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


@pytest.mark.parametrize("file_name, result", PARSE_TABLE)
def test_read_file(file_name, result):
    """Test create_dct function to return a trigram dictionary from list of words."""
    from trigrams import read_file
    assert read_file(file_name) == result


@pytest.mark.parametrize("dct, result", CREATE_DCT)
def test_create_dct(dct, result):
    """Test create_dct function to return a trigram dictionary from list of words."""
    from trigrams import create_dct
    assert create_dct(dct) == result


@pytest.mark.parametrize("first, second, num, dct, text, result", ASSEMBLE_TABLE)
def test_assemble(first, second, num, dct, text, result):
    """Test assemble function to recursively generate random words from dictionary."""
    from trigrams import assemble
    assert assemble(dct, num, text, first, second) == result


@pytest.mark.parametrize("first, second, num, dct, text", ASSEMBLE_TABLE_RANDOM)
def test_assemble_random(first, second, num, dct, text):
    """Test assemble function to recursively generate random words from dictionary."""
    from trigrams import assemble
    ouput = assemble(dct, num, text, first, second)
    match = []
    for key in dct:
        match.extend(dct[key])
    match.extend(text.split())
    assert set(ouput.split()).issubset(set(match))


@pytest.mark.parametrize("input_file, result", SIMPLE_INPUT_FILES)
def test_create_story(input_file, result):
    """Test create_story function with simple files to create a specific new story using trigrams."""
    import trigrams
    output = trigrams.create_story(input_file)
    match = trigrams.assemble(trigrams.create_dct((result * 200).split()))
    assert output == match


@pytest.mark.parametrize("input_file, result", COMPLEX_INPUT_FILES)
def test_create_story_complex(input_file, result):
    """Test create_story function with complex files to create a new story of the same style using trigrams."""
    from trigrams import create_story
    output = create_story(input_file).split()
    match = result.split()
    assert set(list(output)).issubset(set(list(match)))
