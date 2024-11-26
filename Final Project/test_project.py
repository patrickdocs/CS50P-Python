import pytest
import random

from project import getZodiacSign, giveDescription, showPrediction, luckyNumber

def test_getZodiacSign():
    #Valid cases:
    assert getZodiacSign(2,3) == 'Pisces'
    assert getZodiacSign(27,10) == 'Scorpio'

    #Invalid case:
    assert getZodiacSign(30, 2) is None

def test_giveDescription():

    assert giveDescription('Pisces') == ('You have a tolerant, modest, dreamy, romantic, humorous, generous, emotional and receptive character. \nBut sometimes, you are also prone to exaggeration, fickleness, passiveness, and hypersensitivity.')
    assert giveDescription('Aquarius') == ('You have a modest, creative, inquisitive, progressive, stimulating, nocturnal, and independent character. \nBut sometimes, you are also prone to rebelliousness, coldness, indecisiveness, and impracticality.')

def test_showPrediction():
    assert showPrediction('Pisces') == ('Be sincere in the relationship today and skip unwanted debates. Official responsibilities will keep you busy throughout the day.')
    assert showPrediction('Gemini') == ('A diligent love affair is what the horoscope predicts for you Multitask to accomplish every task within the time limit. Financial health will be good today.')

def test_luckyNumber():

    assert 10 <= luckyNumber('Pisces') + len('Pisces') < 50
    assert 10 <= luckyNumber('Scorpio') + len('Scorpio') < 50
