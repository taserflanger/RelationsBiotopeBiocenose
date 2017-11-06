"""Ecosystem Python Version"""
import random, os
from assets.events import *
from assets.mapRange import *
from assets.testInterval import *
from assets.calculateCroissance import *

surfaceA = 0
surfaceB = 0

fieldAttributes = {'temp': 20, 'sun': 2, 'water': 0}


events = [snow, mosquito, orage, sunHeat, overflowing]

paramsA = {'temp': 0, 'sun': 0, 'water': 0}
paramsB = {'temp': 0, 'sun': 0, 'water': 0}

winner = False


croissanceGenerale = random.randint(-10, 10)
epsilon = 100

# Main Loop
while not winner:
    print("New field Attributes:\n")
    [print(key, fieldAttributes[key], sep=":") for key in fieldAttributes.keys()]
    print("Croissance Générale: " + str(croissanceGenerale) + "\n")
    print("Player A's new parameters\n")
    for key in paramsA.keys():
        test = False
        while not test:
            val = float(input(key + ": {current}=> ".format(current = paramsA[key])))
            test = testInterval(paramsA[key], val, epsilon)
            if test:
                paramsA[key] = val

    print("\nPlayer B's new parameters\n")
    for key in paramsB.keys():
        test = False
        while not test:
            val = float(input(key + " {current}=> ".format(current = paramsB[key])))
            test = testInterval(paramsB[key], val, epsilon)
            if test:
                paramsB[key] = val

    print("\n")
    event = random.choice(events)
    temp, sun, water = fieldAttributes["temp"], fieldAttributes["sun"], fieldAttributes["water"]

    fieldAttributes["temp"], fieldAttributes["sun"], fieldAttributes["water"], croissanceGenerale = event(temp, sun, water, croissanceGenerale)

    croissanceA = calculateCroissance(paramsA, croissanceGenerale)
    croissanceB = calculateCroissance(paramsB, croissanceGenerale)

    print("Plante A grandit de " + str(round(croissanceA, 2)))
    print("Taille à rajouter: " + str(round(mapRange(croissanceA, 0, 100, 0, 4))))

    print("\nPlante B grandit de " + str(round(croissanceB, 2)))
    print("Taille à rajouter: " + str(round(mapRange(croissanceB, 0, 100, 0, 4))))
    print("\n------------------------------\n")

    croissanceGenerale += random.randint(-5, 5)
    input("Press any key to continue...")

    os.system('cls')
    if testSurface(surfaceA):
        print("Winner is plant A, with {surface} units".format(surface = surfaceA))
        winner = True
    elif testSurface(surfaceB):
        print("Winner is plant B, with {surface} units.".format(surface = surfaceB))
        winner = True
        
    
    