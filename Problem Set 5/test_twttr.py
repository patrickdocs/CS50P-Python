from twttr import shorten

def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("patrick") == "ptrck"


def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("PATRICK") == "PTRCK"

def test_mix():
    assert shorten("Patrick learn CS50") == "Ptrck lrn CS50"
    assert shorten("I love you") == " lv y"

def test_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"
    assert shorten("What's up?") == "Wht's p?"
