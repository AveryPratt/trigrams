
@pytest.mark.parametrize("text, result", FIBONACCI_TABLE)
def test_parse(text, result):
	"""Test parse function to return a list of words from text."""
	import trigrams
	assert trigrams.parse(text) = result

@pytest.mark.parametrize("result, dct", FIBONACCI_TABLE)
def test_parse(result, dct):
	"""Test create_kvp function to return a trigram dictionary from list of words"""
	import trigrams
	assert trigrams.create_kvp(result) = dct

@pytest.mark.parametrize("dct, txt", FIBONACCI_TABLE)
def test_parse(dct, txt):
	"""Test generate_text function to return new text based on the trigram dictionary"""
	import trigrams
	assert trigrams.generate_text(dct) = txt

@pytest.mark.parametrize("first, second, len, dict, text, result", FIBONACCI_TABLE)
def test_parse(first, second, len, dict, text, result):
	"""Test assemble function to recursively generate random words from dictionary"""
	import trigrams
	assert trigrams.parse(first, second, len, dict, text) = result

