# ZODIAC SIGN GENERATOR
## Video Demo:  <[LINK](https://youtu.be/uJeT1Bi7TGQ)>
## Description:

Zodiac Sign Generator is an interactive Python terminal program, which runs and provides a variety of information related to your zodiac sign. The program will firstly prompt users to provide their birth date, and use this to determine their zodiac sign. They can also get other information such as see predictions for their zodiac sign, see their sign's description and get today's lucky number.

## User Experience

### Target Audience

* People interested in astrology and zodiac signs - Those who follow horoscopes and believe planetary positions at birth impact personality.
* Casual astrology fans - Those who may not fully believe in astrology but think zodiac signs are fun and enjoy reading horoscopes.
* Teenagers and young adults - Astrology and zodiac signs are popular among young demographics. This type of app could appeal to them.

### Key Project Goals

* Provide accurate zodiac sign information - Ensure astrological data and predictions meet quality criteria.
* Develop an engaging, interactive experience - Allow users to explore and learn about signs through a conversational interface.

### User Stories

* As a program creator, I want to:

    + Build an interactive app for the users to learn more about their zodiac signs.
    + Make the app easy to navigate.

* As a new visitor, I want to be able to:

    + Understand the purpose of the program.
    + Get feedback at all times.
    + Navigate easily through the program.

## Design Stage

### Colours
* The colours for the project were added using [Python Colorama](https://pypi.org/project/colorama/)

### Instructions/Explanation

Instructions or explanation for the user have white colour throughout the program.

* Input

Inputs have green colour throughout the program.

* Output

Every feature output have blue colour throughout the program.

## Features

### Existing Features

* __1. Choose your zodiac sign__

  * The feature has two input fields, one for birth day and one for birth month.
  * This feature will allow the user to find out their zodiac sign.

* __2. Giving some descriptions for your zodiac sign__
    * Based on users zodiac sign, this function gives a little description about it.
    * Mainly focus on positive traits (like enthusiasm and passion) and negative traits (like impatience or impulsiveness).
* __3. See predictions for your zodiac sign__

  * Based on users zodiac sign, this feature can tell some predictions in the near future.
  * This feature will allow the user to see 2-3 predictions for their zodiac sign.

* __4. See your lucky number for today__

  * This feature will allow the user to get their lucky number for today and show them the current date.


### Error Handling
- The user is required to enter numbers between 1 and 31 for the birth day and between 1 and 12 for the birth month. Entering any other values will result in an error.

This program offers a flexible user experience, adapting based on the user's knowledge.

## Technologies Used

### Languages

* Python

### Additional

* [Random](https://docs.python.org/3/library/random.html?highlight=random#module-random) - retuns a random number and was used to show compatibility rate between zodiac signs as well as to generate a lucky number
* [Colorama](https://pypi.org/project/colorama/) - makes lines in a terminal appear in different colours
* [Datetime](https://docs.python.org/3/library/datetime.html) - returns today's full date and was used to show today's lucky number for user's zodiac sign
* [Github](https://github.com/) - was used for storing the code


