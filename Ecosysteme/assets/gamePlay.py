import random
from assets.mechanics.mapRange import mapRange

def testInterval(ref, val, epsilon):
    if val < ref - epsilon:
        print("Too low, must be between {a} and {b}".format(a = ref - epsilon, b = ref + epsilon))
        return False
    elif val > ref + epsilon:
        print("Too high, must be between {a} and {b}".format(a = ref - epsilon, b = ref + epsilon))
        return False
    else:
        return True

def printFieldAttributes(fieldAttributes, croissanceGenerale):
    [print(key, fieldAttributes[key], sep=":") for key in fieldAttributes.keys()]
    print("Croissance Générale: " + str(croissanceGenerale) + "\n")


def askParameters(params, epsilon):
    for key in params.keys():
        test = False
        while not test:
            val = float(input(key + ": {current}=> ".format(current = params[key])))
            test = testInterval(params[key], val, epsilon)
            if test:
                params[key] = val


def testWinner(surfaceA, surfaceB):
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

def newRound(fieldAttributes, croissanceGenerale, paramsA, paramsB, epsilon, season):
    print("\n")
    print("It's {season}".format(season=season))
    print("\nField Attributes:\n")
    printFieldAttributes(fieldAttributes, croissanceGenerale)
    print("Sansouire's new parameters\n")
    askParameters(paramsA, epsilon)

    print("\nObione's new parameters\n")
    askParameters(paramsB, epsilon)


def applyEvent(events, fieldAttributes, croissanceGenerale, season):
    
    possibleEvents = [event for event in events if season in event.seasons]
    event = random.choice(possibleEvents)

    fieldAttributes, croissanceGenerale = event(fieldAttributes, croissanceGenerale)
    fieldAttributes['salinity'] = 100 - fieldAttributes['water']

    print("New field Attributes:\n")
    printFieldAttributes(fieldAttributes, croissanceGenerale)
    return fieldAttributes, croissanceGenerale


def printGrowing(croissanceA, croissanceB):
    print("Sansouire grandit de " + str(round(croissanceA, 2)))
    print("Taille à rajouter: " + str(round(mapRange(croissanceA, 0, 100, 0, 4))))

    print("\nObione grandit de " + str(round(croissanceB, 2)))
    print("Taille à rajouter: " + str(round(mapRange(croissanceB, 0, 100, 0, 4))))
    print("\n------------------------------\n")


def initParams(fieldAttributes):
    params = {}
    for key in fieldAttributes.keys():
        params[key] = 0
    return params