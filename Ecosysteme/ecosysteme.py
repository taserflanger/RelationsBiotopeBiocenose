"""Ecosystem Python Version"""
import os
from assets.calculateCroissance import *
from assets.events import *
from assets.gamePlay import *
from assets.mechanics.mapRange import mapRange
from itertools import cycle
surfaceA = 0
surfaceB = 0

fieldAttributes = {'temp': 20, 'sun': 2, 'water': 0, 'salinity': 0}

seasons = ['winter', 'spring', 'summer', 'automn']
SeasonGenerator = cycle(seasons)

events = [snow, mosquito, orage, sunHeat, overflowing]


paramsA = initParams(fieldAttributes)
paramsB = initParams(fieldAttributes)

isWinner = False

croissanceGenerale = random.randint(-10, 10)
epsilon = 10

# Main Loop

turn = 0

while not isWinner:
    season = next(SeasonGenerator)
    newRound(fieldAttributes, croissanceGenerale, paramsA, paramsB, epsilon, season)

    fieldAttributes, croissanceGenerale = applyEvent(events, fieldAttributes, croissanceGenerale, season)


    croissanceA = calculateCroissance(paramsA, fieldAttributes, croissanceGenerale, mapRange, 'sansouire')
    croissanceB = calculateCroissance(paramsB, fieldAttributes, croissanceGenerale, mapRange, 'obione')

    printGrowing(croissanceA, croissanceB)

    croissanceGenerale += random.randint(-5, 5)
    input("Press any key to continue...")

    os.system('cls')
    isWinner = testWinner(surfaceA, surfaceB)
        
    
    