from plates import is_valid

def test_startswith():
    assert is_valid("B52") == False
    assert is_valid("CS50") == True

def test_length():
    assert is_valid("H") == False
    assert is_valid("Hello") == True

def test_number():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_other():
    assert is_valid("PI3.14") == False
    assert is_valid("HI, DAN") == False



