import pytest
from seasons import AgeInMinutes
from datetime import date
import inflect

p = inflect.engine()

def calculate_expected_minutes(dob_date):
    today = date.today()
    timedelta = today - dob_date
    expected_min = timedelta.days * 24 * 60
    return p.number_to_words(expected_min, andword="").capitalize() + " minutes"

def test_valid_date():
    # Test for a valid date (e.g., January 1, 2000)
    age_calculator = AgeInMinutes("2000-01-01")
    result = age_calculator.process()
    assert result == calculate_expected_minutes(date(2000, 1, 1))

def test_random_date():
    # Test for a random date (June 23, 1999)
    age_calculator = AgeInMinutes("1999-06-23")
    result = age_calculator.process()
    assert result == calculate_expected_minutes(date(1999, 6, 23))

def test_special_date():
    # Test for a special date (September 16, 2019)
    age_calculator = AgeInMinutes("2019-09-16")
    result = age_calculator.process()
    assert result == calculate_expected_minutes(date(2019, 9, 16))

def test_leap_year_date():
    # Test for a leap year date (February 29, 2000)
    age_calculator = AgeInMinutes("2000-02-29")
    result = age_calculator.process()
    assert result == calculate_expected_minutes(date(2000, 2, 29))

def test_invalid_date():
    with pytest.raises(SystemExit):
        age_calculator = AgeInMinutes("2024-14-01")
        age_calculator.process()

    with pytest.raises(SystemExit):
        age_calculator = AgeInMinutes("2018-02-31")
        age_calculator.process()
