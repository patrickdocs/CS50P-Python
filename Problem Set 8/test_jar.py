import pytest
from jar import Jar

def test_jar_initialization():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("ten")

def test_jar_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(3)  # Exceeds capacity

    jar.deposit(2)
    assert jar.size == 5  # Now full

def test_jar_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.withdraw(4)  # Not enough cookies

def test_jar_string_representation():
    jar = Jar(5)
    assert str(jar) == ""
    jar.deposit(2)
    assert str(jar) == "🍪🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_jar_negative_operations():
    jar = Jar(5)

    with pytest.raises(ValueError):
        jar.deposit(-1)

    with pytest.raises(ValueError):
        jar.withdraw(-1)
