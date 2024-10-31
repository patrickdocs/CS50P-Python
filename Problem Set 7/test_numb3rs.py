
from numb3rs import validate

def test_valid_ip():
    assert validate("192.168.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("10.0.0.1") == True

def test_invalid_ip():
    assert validate("256.100.50.25") == False
    assert validate("192.168.1.300") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.1.1") == False
    assert validate("abc.def.ghi.jkl") == False
    assert validate("192.168.-1.1") == False
    assert validate("192.168.1.1/24") == False
    assert validate("10.10.10.10.10") == False
