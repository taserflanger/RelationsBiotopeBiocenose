"""Ecosystem Python Version"""
import os
from assets.calculateCroissance import *
from assets.events import *
from assets.gamePlay import applyEvent, initParams, mapRange, printFieldAttributes, printGrowing, testWinner, newRound
from assets.mechanics.mapRange import mapRange
from itertools import cycle

#Initialise les surfaces 
surfaceA = 0
surfaceB = 0

#Initialise les caractéristiques du sansouire et des plantes
fieldAttributes = {'temp': 20, 'sun': 2, 'water': 0, 'salinity': 0}
paramsA = initParams(fieldAttributes)
paramsB = initParams(fieldAttributes)

#Initialise un générateur de saisons
seasons = ['winter', 'spring', 'summer', 'automn']
SeasonGenerator = cycle(seasons)

#Liste des events, chaque élément est une fonction définie dans assets.events
events = [snow, mosquito, orage, sunHeat, overflowing]

#Variables générales
isWinner = False
croissanceGenerale = random.randint(-10, 10)
epsilon = 10
turn = 0

# Main Loop
while not isWinner:
    # Changement de saison tous les trois tours
    if turn % 3 == 0:
        season = next(SeasonGenerator)

    #Demande les nouvelles valeurs
    newRound(fieldAttributes, croissanceGenerale, paramsA, paramsB, epsilon, season)

    #Applique l'événement
    fieldAttributes, croissanceGenerale = applyEvent(events, fieldAttributes, croissanceGenerale, season)

    #calcule les croissances des plantes
    croissanceA = calculateCroissance(paramsA, fieldAttributes, croissanceGenerale, mapRange, 'sansouire')
    croissanceB = calculateCroissance(paramsB, fieldAttributes, croissanceGenerale, mapRange, 'obione')

    #affiche la croissance
    printGrowing(croissanceA, croissanceB)

    #Attent le prochain tour (en modifiant la croissance)
    croissanceGenerale += random.randint(-5, 5)
    input("Press any key to continue...")

    #Clear + teste si il y a un gagnant + change le nombre de tours
    os.system('cls')
    isWinner = testWinner(surfaceA, surfaceB)
    turn += 1
    
    