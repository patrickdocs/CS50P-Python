from description import descriptions
from colorama import Fore
from datetime import date
from prediction import horoscope_predictions
import random


def main():
    max_days_per_month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    while True:
        try:
            day_of_birth = int(input(Fore.GREEN + "What day were you born?   (1 - 31): "))
            month_of_birth = int(input("What month were you born? (1 - 12): "))

            if not 1 <= month_of_birth <= 12:
                raise ValueError("Month must be between 1 and 12.")

            if not 1 <= day_of_birth <= max_days_per_month[month_of_birth]:
                raise ValueError(f"Day must be between 1 and {max_days_per_month[month_of_birth]} for month {month_of_birth}.")

            # Generate zodiac sign:
            zodiacSign = getZodiacSign(day_of_birth, month_of_birth)
            if not zodiacSign:
                raise ValueError("Could not determine zodiac sign.")

            #Show description:
            print(Fore.BLUE + f"Your zodiac sign is {zodiacSign}.")
            description = giveDescription(zodiacSign)
            print(Fore.BLUE + f"{description}.")

            #Show lucky number:
            today = date.today()
            lucky_number = luckyNumber(zodiacSign)
            print(f"Today is {today}. {zodiacSign}'s lucky number is {lucky_number}.")

            #Show predictions:
            prediction = showPrediction(zodiacSign)
            print("Horoscope Predictions: ")
            print(Fore.BLUE + "- " + prediction)

            break

        except ValueError as e:
            print(Fore.RED + f"Invalid input: {e}")

        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}")



def getZodiacSign(day_of_birth, month_of_birth):
    """
    Determines and prints the zodiac sign based on a given birth day and month.
    Checks the birth day and month against the date ranges for each sign.
    Prints the sign, symbol, and traits if a match is found.
    """
    zodiacSign = None
    if (month_of_birth == 3 and 21 <= day_of_birth <= 31) or (month_of_birth == 4 and 1 <= day_of_birth <= 19):
        zodiacSign = "Aries"
    elif (month_of_birth == 4 and 20 <= day_of_birth <= 30) or (month_of_birth == 5 and 1 <= day_of_birth <= 20):
        zodiacSign = "Taurus"
    elif (month_of_birth == 5 and 21 <= day_of_birth <= 31) or (month_of_birth == 6 and 1 <= day_of_birth <= 20):
        zodiacSign = "Gemini"
    elif (month_of_birth == 6 and 21 <= day_of_birth <= 30) or (month_of_birth == 7 and 1 <= day_of_birth <= 22):
        zodiacSign = "Cancer"
    elif (month_of_birth == 7 and 23 <= day_of_birth <= 31) or (month_of_birth == 8 and 1 <= day_of_birth <= 22):
        zodiacSign = "Leo"
    elif (month_of_birth == 8 and 23 <= day_of_birth <= 31) or (month_of_birth == 9 and 1 <= day_of_birth <= 22):
        zodiacSign = "Virgo"
    elif (month_of_birth == 9 and 23 <= day_of_birth <= 30) or (month_of_birth == 10 and 1 <= day_of_birth <= 22):
        zodiacSign = "Libra"
    elif (month_of_birth == 10 and 23 <= day_of_birth <= 31) or (month_of_birth == 11 and 1 <= day_of_birth <= 21):
        zodiacSign = "Scorpio"
    elif (month_of_birth == 11 and 22 <= day_of_birth <= 30) or (month_of_birth == 12 and 1 <= day_of_birth <= 21):
        zodiacSign = "Sagittarius"
    elif (month_of_birth == 12 and 22 <= day_of_birth <= 31) or (month_of_birth == 1 and 1 <= day_of_birth <= 19):
        zodiacSign = "Capricorn"
    elif (month_of_birth == 1 and 20 <= day_of_birth <= 31) or (month_of_birth == 2 and 1 <= day_of_birth <= 18):
        zodiacSign = "Aquarius"
    elif (month_of_birth == 2 and 19 <= day_of_birth <= 29) or (month_of_birth == 3 and 1 <= day_of_birth <= 20):
        zodiacSign = "Pisces"

    return zodiacSign



def giveDescription(zodiacSign):
    return descriptions[zodiacSign]
    #print(Fore.BLUE + descriptions[zodiacSign])

def showPrediction(zodiacSign):
    #return horoscope_predictions.get(zodiacSign, "No prediction available for this zodiac sign.")
    prediction = horoscope_predictions.get(zodiacSign)
    if isinstance(prediction, list):
        return " ".join(prediction)
    return prediction or "No prediction available for this zodiac sign."

def luckyNumber(zodiacSign):
    luckynum = random.randint(1, 30) + len(zodiacSign)
    return luckynum


if __name__ == "__main__":
    main()
