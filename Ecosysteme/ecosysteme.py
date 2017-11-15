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
fieldAttributes = {'temp': 20, 'sun': 2, 'water': 50, 'salinity': 50}
paramsA = initParams(fieldAttributes)
paramsB = initParams(fieldAttributes)
plants = {"Salicorne": 0, "Obione": 0}

#Initialise un générateur de saisons
seasons = ['winter', 'spring', 'summer', 'automn']
SeasonGenerator = cycle(seasons)

#Liste des events, chaque élément est une fonction définie dans assets.events
events = [snow, mosquito, orage, sunHeat, overflowing]

#Variables générales
isWinner = False
epsilon = 10
turn = 0

# Main Loop
while not isWinner:
    # Changement de saison tous les trois tours
    if turn % 3 == 0:
        season = next(SeasonGenerator)

    #Demande les nouvelles valeurs
    newRound(fieldAttributes, plants, paramsA, paramsB, epsilon, season)

    #Applique l'événement
    fieldAttributes, plants = applyEvent(events, fieldAttributes, plants, season)

    #calcule les croissances des plantes
    croissanceA = calculateCroissance(paramsA, fieldAttributes, plants[list(plants.keys())[0]], mapRange, list(plants.keys())[0])
    croissanceB = calculateCroissance(paramsB, fieldAttributes, plants[list(plants.keys())[1]], mapRange, list(plants.keys())[1])

    #affiche la croissance
    printGrowing(croissanceA, croissanceB, plants)

    #Attent le prochain tour (en modifiant la croissance)
    for plant in plants:
        plants[plant] +=random.randint(5, 10)
    input("Press any key to continue...")

    #Clear + teste si il y a un gagnant + change le nombre de tours
    os.system('cls')
    isWinner = testWinner(surfaceA, surfaceB)
    turn += 1
    
    