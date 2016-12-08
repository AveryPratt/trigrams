"""Trigrams."""
PARSE_TABLE = [
    [
        "Howdily doodily, neigborooski. My name is Ned Flanders.",
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
            "Howdily_doodily,": "neighborooski.",
            "doodily,_neighborooski.": "My",
            "neighborooski._My": "name",
            "My_name": "is",
            "name_is": "Ned",
            "is_Ned": "Flanders.",
        },
    ],
    [
        ["Toodle", "dooski!", ],
        {},
    ],
    [
        ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "ass", "dogs.", ],
        {
            "The_quick": "brown",
            "quick_brown": "fox",
            "brown_fox": "jumped",
            "fox_jumped": "over",
            "jumped_over": "the",
            "over_the": "lazy",
            "the_lazy": "ass",
            "lazy_ass": "dogs.",
        },
    ],
]


TEXT = [
    [
        {
            "Howdily_doodily,": "neighborooski.",
            "doodily,_neighborooski.": "My",
            "neighborooski._My": "name",
            "My_name": "is",
            "name_is": "Ned",
            "is_Ned": "Flanders.",
        },
    ],
    [
        {},
    ],
    [
        {
            "The_quick": "brown",
            "quick_brown": "fox",
            "brown_fox": "jumped",
            "fox_jumped": "over",
            "jumped_over": "the",
            "over_the": "lazy",
            "the_lazy": "ass",
            "lazy_ass": "dogs.",
        },
    ],
]


ASSEMBLE_TABLE = [
    ["first", "second", 1, {"first_second": "third"}, "", "third", ],
    ["first", "second", 0, {"first_second": "third"}, "", "", ],
    ["first", "second", 0, {"first_second": "third"}, "random jibberish", "random jibberish", ],
    ["first", "second", 3, {"first_second": "third"}, "random jibberish", "random jibberish third third third", ],
]


ASSEMBLE_TABLE_RANDOM = [
    ["first", "second", 3, {
        "The_quick": "brown",
        "quick_brown": "fox",
        "brown_fox": "jumped",
        "fox_jumped": "over",
        "first_second": "The",
        "second_the": "quick",
        "jumped_over": "the",
        "over_the": "lazy",
        "the_lazy": "ass",
        "lazy_ass": "dogs.",
    },
        "", [], ],
    ["first", "second", 80, {
        "The_quick": "brown",
        "quick_brown": "fox",
        "brown_fox": "jumped",
        "fox_jumped": "over",
        "second_the": "quick",
        "jumped_over": "the",
        "over_the": "lazy",
        "the_lazy": "ass",
        "lazy_ass": "dogs.",
    },
        "random jibberish", [], ],
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


@pytest.mark.parametrize("first, second, len, dict, text, result", ASSEMBLE_TABLE)
def test_assemble(first, second, len, dict, text, result):
    """Test assemble function to recursively generate random words from dictionary."""
    import trigrams
    assert trigrams.assemble(first, second, len, dict, text) == result


@pytest.mark.parametrize("first, second, len, dict, text, result", ASSEMBLE_TABLE_RANDOM)
def test_assemble_random(first, second, len, dict, text, result):
    """Test assemble function to recursively generate random words from dictionary."""
    import trigrams
    assert trigrams.assemble(first, second, len, dict, text) == result
