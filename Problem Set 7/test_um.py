from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM?") == 1

def test_multiple_um():
    assert count("um, um, um") == 3
    assert count("Um, um, UM") == 3

def test_no_um():
    assert count("hello") == 0
    assert count("yummy") == 0
    assert count("umbrella") == 0

def test_um_with_punctuation():
    assert count("um...") == 1
    assert count("Um? Um!") == 2
