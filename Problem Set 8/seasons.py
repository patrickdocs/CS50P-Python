from datetime import date
import sys
import inflect

p = inflect.engine()
class AgeInMinutes:
    def __init__(self, dob_str):
        self.dob_str = dob_str

    def convert(self, minutes):
        word_mins = p.number_to_words(minutes, andword="")
        return f"{word_mins.capitalize()} minutes"

    def process(self):
        try:
            dob = date.fromisoformat(self.dob_str)
            today = date.today()
            timedelta = today - dob
            total_mins = timedelta.days * 24 * 60
            return self.convert(total_mins)
        except ValueError:
             sys.exit("Invalid input")

def main():
    dob_str = input("Date of Birth: ")
    total_mins = AgeInMinutes(dob_str)
    print(total_mins.process())

if __name__ == "__main__":
    main()


#check50 cs50/problems/2022/python/seasons
