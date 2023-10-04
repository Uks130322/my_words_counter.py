import dataclasses
import pytest
import testlib

from my_words_counter import clean, word_counter, words_occurrences, common_words, rare_words, bytes_counter


@dataclasses.dataclass
class Case:
    file: str
    cleared_file: str
    counted: tuple[str: int]
    occurrences: tuple[str: int]
    common: list[str]
    rare: list[str]
    byte: int

    def __str__(self) -> str:
        return "count_{}".format(self.file)


TEST_CASES = [
    Case(
        file='counter/files/empty.txt',
        cleared_file='counter/files/cleaned_empty.txt',
        counted={'lines:': 1, 'words:': 0, 'chars:': 0, 'longest line:': 0},
        occurrences={},
        common=[],
        rare=[],
        byte=0
    ),
    Case(
        file='counter/files/spam.txt',
        cleared_file='counter/files/cleaned_spam.txt',
        counted={'lines:': 1, 'words:': 73, 'chars:': 442, 'longest line:': 442},
        occurrences={'the': 7, 'term': 1, 'spam': 8, 'is': 1, 'derived': 1, 'from': 1, '1970': 1, 'sketch': 3, 'of': 2,
                     'bbc': 1, 'comedy': 1, 'television': 1, 'series': 1, 'monty': 1, "python's": 1, 'flying': 1,
                     'circus': 1, '5': 1, '6': 1, 'set': 1, 'in': 1, 'a': 5, 'cafe': 1, 'has': 1, 'waitress': 2,
                     'reading': 1, 'out': 2, 'menu': 2, 'where': 1, 'every': 1, 'item': 1, 'but': 1, 'one': 1,
                     'includes': 1, 'canned': 1, 'luncheon': 1, 'meat': 1, 'as': 1, 'recites': 1, 'spam-filled': 1,
                     'chorus': 1, 'viking': 1, 'patrons': 1, 'drown': 1, 'all': 1, 'conversations': 1, 'with': 1,
                     'song': 1, 'repeating': 1, 'spamвђ¦': 1, 'lovely': 1, 'wonderful': 1, '7': 1},

        common=['spam'],
        rare=['term', 'is', 'derived', 'from', '1970', 'bbc', 'comedy', 'television', 'series', 'monty', "python's",
              'flying', 'circus', '5', '6', 'set', 'in', 'cafe', 'has', 'reading', 'where', 'every', 'item', 'but',
              'one', 'includes', 'canned', 'luncheon', 'meat', 'as', 'recites', 'spam-filled', 'chorus', 'viking',
              'patrons', 'drown', 'all', 'conversations', 'with', 'song', 'repeating', 'spamвђ¦', 'lovely',
              'wonderful', '7'],
        byte=445
    ),

    Case(
        file='counter/files/symbols.txt',
        cleared_file='counter/files/cleaned_symbols.txt',
        counted={'lines:': 6, 'words:': 2, 'chars:': 9, 'longest line:': 3},
        occurrences={'': 5},
        common=[''],
        rare=[''],
        byte=14
    ),

    Case(
        file='counter/files/tyger.txt',
        cleared_file='counter/files/cleaned_tyger.txt',
        counted={'lines:': 33, 'words:': 146, 'chars:': 786, 'longest line:': 39},
        occurrences={'the': 14, 'tyger': 5, 'by': 1, 'william': 1, 'blake': 1, 'burning': 2, 'bright': 2, 'in': 4,
                     'forests': 2, 'of': 4, 'night': 2, 'what': 14, 'immortal': 2, 'hand': 4, 'or': 3, 'eye': 2,
                     'could': 2, 'frame': 2, 'thy': 5, 'fearful': 2, 'symmetry': 2, 'distant': 1, 'deeps': 1,
                     'skies': 1, 'burnt': 1, 'fire': 2, 'thine': 1, 'eyes': 1, 'on': 1, 'wings': 1, 'dare': 4, 'he': 3,
                     'aspire': 1, 'seize': 1, 'and': 3, 'shoulder': 1, '&': 2, 'art': 1, 'twist': 1, 'sinews': 1,
                     'heart': 2, 'when': 2, 'began': 1, 'to': 2, 'beat': 1, 'dread': 3, 'feet': 1, 'hammer': 1,
                     'chain': 1, 'furnace': 1, 'was': 1, 'brain': 1, 'anvil': 1, 'grasp': 1, 'its': 1, 'deadly': 1,
                     'terrors': 1, 'clasp': 1, 'stars': 1, 'threw': 1, 'down': 1, 'their': 2, 'spears': 1, "water'd": 1,
                     'heaven': 1, 'with': 1, 'tears': 1, 'did': 2, 'smile': 1, 'his': 1, 'work': 1, 'see': 1, 'who': 1,
                     'made': 1, 'lamb': 1, 'make': 1, 'thee': 1},
        common=['the', 'what'],
        rare=['by', 'william', 'blake', 'distant', 'deeps', 'skies', 'burnt', 'thine', 'eyes', 'on', 'wings', 'aspire',
              'seize', 'shoulder', 'art', 'twist', 'sinews', 'began', 'beat', 'feet', 'hammer', 'chain', 'furnace',
              'was', 'brain', 'anvil', 'grasp', 'its', 'deadly', 'terrors', 'clasp', 'stars', 'threw', 'down', 'spears',
              "water'd", 'heaven', 'with', 'tears', 'smile', 'his', 'work', 'see', 'who', 'made', 'lamb', 'make',
              'thee'],
        byte=818
    ),

    Case(
        file='counter/files/vokras.txt',
        cleared_file='counter/files/cleaned_vokras.txt',
        counted={'lines:': 24, 'words:': 103, 'chars:': 587, 'longest line:': 37},
        occurrences={'in': 4, 'grayish': 3, 'mists': 3, 'the': 8, 'slimy': 3, 'beasts': 3, 'vokras': 3, 'can': 2,
                     'be': 2, 'found': 2, 'they': 7, 'slowly': 6, 'float': 1, 'drift': 1, 'above': 1, 'sopping': 1,
                     'ground': 1, 'feed': 1, 'on': 1, 'rotten': 2, 'weed': 1, 'extending': 1, 'limbs': 2, 'to': 2,
                     'earth': 1, 'mate': 1, 'breed': 1, 'new': 1, 'ones': 1, 'giving': 1, 'birth': 1, 'decently': 1,
                     'converse': 1, 'of': 2, 'happiness': 1, 'and': 3, 'vice': 1, 'hunt': 2, 'for': 2, 'frogs': 2,
                     'slide': 1, 'them': 1, 'buccal': 1, 'orifice': 1, "they're": 1, 'worming': 1, 'their': 1,
                     'pliant': 1, 'through': 1, 'heaps': 1, 'logs': 1, 'away': 2, 'from': 2, "people's": 1, 'noisy': 1,
                     'feasts': 1, 'light': 1, 'sound': 1},
        common=['the'],
        rare=['float', 'drift', 'above', 'sopping', 'ground', 'feed', 'on', 'weed', 'extending', 'earth', 'mate',
              'breed', 'new', 'ones', 'giving', 'birth', 'decently', 'converse', 'happiness', 'vice', 'slide', 'them',
              'buccal', 'orifice', "they're", 'worming', 'their', 'pliant', 'through', 'heaps', 'logs', "people's",
              'noisy', 'feasts', 'light', 'sound'],
        byte=610
    ),
]


###################
# Structure asserts
###################


def test_docs() -> None:
    assert testlib.is_function_docstring_exists(clean)
    assert testlib.is_function_docstring_exists(word_counter)
    assert testlib.is_function_docstring_exists(words_occurrences)
    assert testlib.is_function_docstring_exists(common_words)
    assert testlib.is_function_docstring_exists(rare_words)
    assert testlib.is_function_docstring_exists(bytes_counter)


###################
# Tests
###################


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_clean(t: Case) -> None:
    with open(t.file) as file:
        text = file.read()
        text_copy = text

    clean(t.file)

    with open('cleaned_text.txt') as new_file, open(t.cleared_file) as cleared_file:
        cleared_text = cleared_file.read()
        new_text = new_file.read()
        assert new_text == cleared_text

    with open(t.file) as file:
        text = file.read()
        assert text_copy == text, "You shouldn't change input"


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_word_counter(t: Case) -> None:
    with open(t.file) as file:
        text = file.read()
        text_copy = text

    assert word_counter(t.file) == t.counted

    with open(t.file) as file:
        text = file.read()
        assert text_copy == text, "You shouldn't change input"


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_words_occurrences(t: Case) -> None:
    with open(t.file) as file:
        text = file.read()
        text_copy = text

    assert words_occurrences(t.file) == t.occurrences

    with open(t.file) as file:
        text = file.read()
        assert text_copy == text, "You shouldn't change input"


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_common_words(t: Case) -> None:
    with open(t.file) as file:
        text = file.read()
        text_copy = text

    assert common_words(t.file) == t.common

    with open(t.file) as file:
        text = file.read()
        assert text_copy == text, "You shouldn't change input"


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_rare_words(t: Case) -> None:
    with open(t.file) as file:
        text = file.read()
        text_copy = text

    assert rare_words(t.file) == t.rare

    with open(t.file) as file:
        text = file.read()
        assert text_copy == text, "You shouldn't change input"


@pytest.mark.parametrize('t', TEST_CASES, ids=str)
def test_bytes(t: Case) -> None:
    with open(t.file, 'br') as file:
        text = file.read()
        text_copy = text

    assert bytes_counter(t.file) == t.byte

    with open(t.file, 'br') as file:
        text = file.read()
        assert text_copy == text, "You shouldn't change input"
