import sys
import random
from pyfiglet import Figlet
figlet = Figlet()

def get_font():
    if len(sys.argv) == 1:
        return random.choice(figlet.getFonts())
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        if sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")
        return sys.argv[2]
    else:
        sys.exit("Invalid usage")

def main():
    font = get_font()
    figlet.setFont(font = font) #Set the Font
    user_text = input("Input: ") # Prompt user's text
    # Render and print the text in the chosen font
    print(figlet.renderText(user_text))

if __name__ == "__main__":
    main()
#check50 cs50/problems/2022/python/figlet
