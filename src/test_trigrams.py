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


TEXT = [
    [
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
        {},
    ],
    [
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
    [
        "first",
        "second",
        0,
        {
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
        "random jibberish ",
        "random jibberish",
    ],
    [
        "first",
        "second",
        3,
        {
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
        "random jibberish ",
        "random jibberish third third third",
    ],
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


@pytest.mark.parametrize("text, result", PARSE_TABLE)
def test_parse(text, result):
    """Test parse function to return a list of words from text."""
    import trigrams
    assert trigrams.parse(text) == result


@pytest.mark.parametrize("result, dct", CREATE_KVP)
def test_create_kvp(result, dct):
    """Test create_kvp function to return a trigram dictionary from list of words."""
    import trigrams
    assert trigrams.create_kvp(result) == dct


@pytest.mark.parametrize("dct", TEXT)
def test_generate_text(dct):
    """Test generate_text function to return new text based on the trigram dictionary."""
    import trigrams
    assert trigrams.generate_text(dct).split() == dct.values


@pytest.mark.parametrize("first, second, num, dct, text, result", ASSEMBLE_TABLE)
def test_assemble(first, second, num, dct, text, result):
    """Test assemble function to recursively generate random words from dictionary."""
    import trigrams
    assert trigrams.assemble(first, second, num, dct, text) == result


@pytest.mark.parametrize("first, second, num, dct, text", ASSEMBLE_TABLE_RANDOM)
def test_assemble_random(first, second, num, dct, text):
    """Test assemble function to recursively generate random words from dictionary."""
    import trigrams
    result = trigrams.assemble(first, second, num, dct, text)
    all_values = []
    for key in dct:
        all_values.extend(dct[key])

    # import pdb;pdb.set_trace()
    all_values.extend(text.split())
    assert set(result.split()).issubset(set(all_values))
