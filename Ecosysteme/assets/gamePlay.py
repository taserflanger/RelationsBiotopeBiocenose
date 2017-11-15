"""Definition for gameplay functions"""

import random
from assets.mechanics.mapRange import mapRange

def testInterval(ref, val, epsilon):
    """Tests if the value *var* variates too much from a reference value"""
    if val < ref - epsilon:
        print("Too low, must be between {a} and {b}".format(a = ref - epsilon, b = ref + epsilon))
        return False
    elif val > ref + epsilon:
        print("Too high, must be between {a} and {b}".format(a = ref - epsilon, b = ref + epsilon))
        return False
    else:
        return True

def printFieldAttributes(fieldAttributes, plants):
    """Prints all the field characteristics"""
    [print(key, fieldAttributes[key], sep=":") for key in fieldAttributes.keys()]
    print("\nCroissance des plantes: \n")
    [print(key, plants[key], sep=': ') for key in plants]


def askParameters(params, epsilon):
    """Asks for new paramters given a plant's 
    parameter dict *params* and a variance value *epsilon*"""
    for key in params.keys():
        test = False
        while not test:
            val = float(input(key + ": {current}=> ".format(current = params[key])))
            test = testInterval(params[key], val, epsilon)
            if test:
                params[key] = val


def testWinner(surfaceA, surfaceB):
    """Tests and prints out if there is a winner"""
    if surfaceA > 100 and surfaceB > 100:
        if surfaceA > surfaceB:
            print("Winner is plant A, {surfaceA} to {surfaceB}...".format(surfaceA=surfaceA, surfaceB=surfaceB))
        elif surfaceB > surfaceA:
            print("Winner is plant B, {surfaceB} to {surfaceA}...".format(surfaceA=surfaceA, surfaceB=surfaceB))
        else:
            print("Draw! {surfaceB} to {surfaceA}...".format(surfaceA=surfaceA, surfaceB=surfaceB))
    if surfaceA > 100:
        print("Winner is plant A, with {surface} units".format(surface=surfaceA))
        return True
    if surfaceB > 100:
        print("Winner is plant B, with {surface} units.".format(surface=surfaceB))
        return True
    return False

#|-------------------|
#|GamePlay functions |
#|-------------------|

def newRound(fieldAttributes, plants, paramsA, paramsB, epsilon, season):
    """Asks for each plant's (paramsA and paramsB) parameter, and print's out
    the field attributes again."""

    print("\n")
    #Season
    print("It's {season}".format(season=season))

    #Field
    print("\nField Attributes:\n")
    printFieldAttributes(fieldAttributes, plants)

    #plantA
    print("{plant}'s new parameters\n".format(plant=list(plants.keys())[0]))
    askParameters(paramsA, epsilon)

    # plantB
    print("\n{plant}'s new parameters\n".format(plant=list(plants.keys())[1]))
    askParameters(paramsB, epsilon)


def applyEvent(events, fieldAttributes, plants, season):
    """Tests *events* eligible to *season* and chooses a random season,
    applying the effects to the *fieldAttributes* and the individual *plants* growing"""
    
    possibleEvents = [event for event in events if season in event.seasons]
    event = random.choice(possibleEvents)
    print("\n")

    fieldAttributes, plants = event(fieldAttributes, plants)
    fieldAttributes['salinity'] = 100 - fieldAttributes['water']

    print("New field Attributes:\n")
    printFieldAttributes(fieldAttributes, plants)
    return fieldAttributes, plants


def printGrowing(croissanceA, croissanceB, plants):
    """Prints out how much plant did grow and which case to add (int)"""

    print("\n{plant} grandit de ".format(plant=list(plants.keys())[0]) + str(round(croissanceA, 2)))
    print("Taille à rajouter: " + str(round(mapRange(croissanceA, 0, 100, 0, 4))))

    print("\n{plant} grandit de ".format(plant=list(plants.keys())[1]) + str(round(croissanceB, 2)))
    print("Taille à rajouter: " + str(round(mapRange(croissanceB, 0, 100, 0, 4))))
    print("\n------------------------------\n")


def initParams(fieldAttributes):
    """Return new plantParameters given the *fieldAttributes*"""
    params = {}
    for key in fieldAttributes.keys():
        params[key] = 0
    return params